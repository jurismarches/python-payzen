import hashlib
from decimal import Decimal, ROUND_HALF_UP
import operator
from datetime import datetime


class SEPAMandateFormData:
    """
    Utility to generate form data for the payzen payment registration form
    """

    def __init__(self, user, payzen_id, comeback_url, payzen_certificate,
                 payzen_shop_id, payzen_context, payzen_version, update=False):

        self._certificate = payzen_certificate

        self.vads_identifier = payzen_id
        self.vads_page_action = 'REGISTER_UPDATE' if update else 'REGISTER'
        self.vads_cust_id = str(user.id)
        self.vads_cust_title = user.title
        self.vads_cust_last_name = user.last_name
        self.vads_cust_first_name = user.first_name
        self.vads_cust_country = user.country.code if user.country else 'FR'
        self.vads_cust_email = user.email
        self.vads_site_id = payzen_shop_id
        self.vads_ctx_mode = payzen_context
        self.vads_trans_date = self.get_trans_date()
        self.vads_action_mode = 'INTERACTIVE'
        self.vads_version = payzen_version
        self.vads_payment_cards = ''

        self.vads_url_cancel = comeback_url
        self.vads_url_error = comeback_url
        self.vads_url_refused = comeback_url
        self.vads_url_return = comeback_url
        self.vads_url_success = comeback_url

    @staticmethod
    def get_trans_date():
        """
        :return: AAAAMMJJHHMMSS
        """
        utcnow = datetime.utcnow()
        return utcnow.strftime('%Y%m%d%H%M%S')

    @property
    def signature(self):
        """
        return the signature for the class data
        """
        data_to_sign = {
            a: getattr(self, a)
            for a in dir(self)
            if a.startswith('vads_')}
        return get_payzen_signature(data_to_sign, self._certificate)


class SEPAMandateAndPayFormData(SEPAMandateFormData):

    def __init__(self, user, payzen_id, comeback_url, payzen_certificate,
                 payzen_shop_id, payzen_context, payzen_version, amount,
                 trans_id, payment_config, update=False):
        super().__init__(
            user, payzen_id, comeback_url, payzen_certificate,
            payzen_shop_id, payzen_context, payzen_version, update)
        self.vads_page_action = 'REGISTER_PAY'
        a = amount.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
        self.vads_amount = str(a).replace('.', '')
        self.vads_currency = '978'
        self.vads_trans_id = str(trans_id)
        self.vads_payment_config = payment_config


def get_payzen_signature(data, certificate):
    """
    The signature is build following those steps :
      * get all the attribute starting by 'vads_'
      * order the attributes
      * build a list with the value of each attribute
      * append the certificate to the list of values
      * join all the values with '+'
      * hash the string with sha1
    """
    ordered_items = sorted(data.items(), key=operator.itemgetter(0))
    values = [v for k, v in ordered_items if k.startswith('vads_')]
    values.append(certificate)
    chain_to_hash = "+".join(values)
    return hashlib.sha1(chain_to_hash.encode('utf-8')).hexdigest()
