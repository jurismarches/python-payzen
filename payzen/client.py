import base64
import hashlib
import hmac
import logging
import uuid
from datetime import datetime

import suds.client
from suds.sax.element import Element

from payzen.exceptions import PayzenError
from .codes import errors

PRODUCTION = 'PRODUCTION'
TEST = 'TEST'

EURO = 978


class PayzenClient:

    def __init__(self, url, shop_id, certificate, context, tz):
        self._url = url
        self._shop_id = shop_id
        self._certificate = certificate
        self._context = context
        self._tz = tz
        self.logger = logging.getLogger(__name__)

    def _get_client(self):
        """ usage unique """
        client = suds.client.Client(url=self._url)
        client.set_options(soapheaders=self._get_headers())
        return client

    def _get_headers(self):
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
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    def _get_auth_token(self, request_id, timestamp, type='request'):
        if type == 'response':
            s = "{}{}".format(timestamp, request_id)
        else:
            s = "{}{}".format(request_id, timestamp)
        h = hmac.new(self._certificate.encode('utf-8'), s.encode('utf-8'), hashlib.sha256)
        return base64.b64encode(h.digest()).decode('utf-8')

    def _check_response_status(self, response):
        if response.commonResponse.responseCode != errors.SUCCESS:
            error_code = response.commonResponse.responseCode
            message = response.commonResponse.responseCodeDetail
            raise PayzenError(
                message=message,
                error_code=error_code,
                extended_error_code=None,
                response=response
            )
        return response

    def cancel_token(self, token_id):
        client = self._get_client()
        common = client.factory.create('commonRequest')
        query = client.factory.create('queryRequest')
        query.paymentToken = token_id
        response = client.service.cancelToken(common, query)
        self._check_response_status(response)
        return response

    def get_token_details(self, token_id):
        client = self._get_client()
        query = client.factory.create('queryRequest')
        query.paymentToken = token_id
        response = client.service.getTokenDetails(query)
        self._check_response_status(response)
        return response

    def create_payment(self, token_id, amount):
        client = self._get_client()

        common_request = client.factory.create('commonRequest')
        common_request.submissionDate = self._get_iso_8601_datetime()

        three_ds_request = client.factory.create('threeDSRequest')
        three_ds_request.mode = 'DISABLED'

        payment_request = client.factory.create('paymentRequest')
        payment_request.amount = amount
        payment_request.currency = EURO

        order_request = client.factory.create('orderRequest')
        order_request.orderId = 1000

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

        self._check_response_status(response)
        return response
