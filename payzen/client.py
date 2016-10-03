import base64
import hashlib
import hmac

import uuid
from datetime import datetime
from functools import wraps

import suds.client
from suds.sax.element import Element

from payzen.exceptions import PayzenError, PayzenPaymentRefused
from .codes import errors

PRODUCTION = 'PRODUCTION'
TEST = 'TEST'

EURO = 978


def check_response(f):
    """
    Wrapper to check the response and raise a Payzen Error if not a success
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        if response.commonResponse.responseCode != errors.SUCCESS:
            error_code = response.commonResponse.responseCode
            if hasattr(response.commonResponse, 'responseCodeDetail'):
                message = response.commonResponse.responseCodeDetail
            else:
                message = ''
            raise PayzenError(
                message=message,
                error_code=error_code,
                extended_error_code=None,
                response=response
            )
        return response
    return wrapper


class PayzenTokenMixin:
    """
    Handle request about payzen tokens
    """

    @check_response
    def cancel_token(self, token_id):
        """
        Cancel the token
        """
        client = self._get_client()
        common = client.factory.create('commonRequest')
        query = client.factory.create('queryRequest')
        query.paymentToken = token_id
        response = client.service.cancelToken(common, query)
        return response

    @check_response
    def get_token_details(self, token_id):
        """
        Retrieve informations about the given token
        """
        client = self._get_client()
        query = client.factory.create('queryRequest')
        query.paymentToken = token_id
        response = client.service.getTokenDetails(query)
        return response

    @check_response
    def update_token(self, token_id, email):
        """
        Update the current token email.
        Customer first and last name can't be modify as they are passed by the
        user when he registers his payment method
        """
        client = self._get_client()

        query_request = client.factory.create('queryRequest')
        query_request.paymentToken = token_id

        customer_request = client.factory.create('customerRequest')
        customer_request.billingDetails.email = email
        response = client.service.updateToken(
            client.factory.create('commonRequest'),
            query_request,
            client.factory.create('cardRequest'),
            customer_request,
        )

        return response


class PayzenPaymentMixin:
    """
    Handle request about payment
    """

    @check_response
    def create_payment(self, token_id, amount, order_id):
        """
        Create a payment for the given token (needs to be registered before),
        the given amount (in Euros) with the given order id
        """
        client = self._get_client()

        common_request = client.factory.create('commonRequest')
        common_request.submissionDate = self._get_iso_8601_datetime()

        three_ds_request = client.factory.create('threeDSRequest')
        three_ds_request.mode = 'DISABLED'

        payment_request = client.factory.create('paymentRequest')
        payment_request.amount = amount
        payment_request.currency = EURO

        order_request = client.factory.create('orderRequest')
        order_request.orderId = order_id

        card_request = client.factory.create('cardRequest')
        card_request.paymentToken = token_id

        customer_request = client.factory.create('customerRequest')
        tech_request = client.factory.create('techRequest')
        shopping_cart_request = client.factory.create('shoppingCartRequest')

        response = client.service.createPayment(
            common_request,
            three_ds_request,
            payment_request,
            order_request,
            card_request,
            customer_request,
            tech_request,
            shopping_cart_request,
        )

        if (response.commonResponse.responseCode == errors.SUCCESS and
           response.commonResponse.transactionStatusLabel and
           response.commonResponse.transactionStatusLabel != 'AUTHORISED'):
            raise PayzenPaymentRefused(response=response)

        return response

    @check_response
    def get_payment_details(self, transaction_uuid):
        """
        Retrieve informations about the given transaction
        """
        client = self._get_client()

        query_request = client.factory.create('queryRequest')
        query_request.uuid = transaction_uuid

        response = client.service.getPaymentDetails(query_request)
        return response


class PayzenBasicsMixin:
    """
    Utils to generate the Webservice client, the headers and the signature
    """

    def _get_client(self):
        """
        Build a SOAP webservice client.

        /!\ Can be use only one time because the headers (and especially the
        request id) needs to be regenerated for each request
        """
        client = suds.client.Client(url=self._url)
        client.set_options(soapheaders=self._get_headers())
        return client

    def _get_headers(self):
        """
        Build the headers needed by the webservice
        """
        header_ns = ('ns1', 'http://v5.ws.vads.lyra.com/Header/')
        shop_id_elem = Element('shopId', ns=header_ns).setText(self._shop_id)
        mode_elem = Element('mode', ns=header_ns).setText(self._context)

        request_id = uuid.uuid1()
        request_id_elem = Element('requestId', ns=header_ns).setText(request_id)

        timestamp = self._get_iso_8601_datetime()
        timestamp_elem = Element('timestamp', ns=header_ns).setText(timestamp)

        auth_token = self._get_auth_token(request_id, timestamp)
        auth_token_elem = Element('authToken', ns=header_ns).setText(auth_token)
        return shop_id_elem, mode_elem, request_id_elem, timestamp_elem, auth_token_elem

    def _get_iso_8601_datetime(self):
        """
        build an iso datetime
        """
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    def _get_auth_token(self, request_id, timestamp, type='request'):
        """
        Build the auth token (kind of signature)
        """
        if type == 'response':
            s = "{}{}".format(timestamp, request_id)
        else:
            s = "{}{}".format(request_id, timestamp)
        h = hmac.new(self._certificate.encode('utf-8'), s.encode('utf-8'), hashlib.sha256)
        return base64.b64encode(h.digest()).decode('utf-8')


class PayzenClient(PayzenTokenMixin, PayzenPaymentMixin, PayzenBasicsMixin):
    """
    Final Payzen client
    """

    def __init__(self, url, shop_id, certificate, context):
        super().__init__()
        self._url = url
        self._shop_id = shop_id
        self._certificate = certificate
        self._context = context
