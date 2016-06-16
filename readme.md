Payzen
======

https://payzen.eu/

Payzen client for SOAP API and utilities to generate the form

Examples
--------


**Retrieve information about a token**

``` python
from payzen.client import PayzenClient

payzen_client =  PayzenClient(
    url='https://secure.payzen.eu/vads-ws/v5?wsdl',
    shop_id='00000000',
    certificate='0000000000000000',
    context='TEST')

# returns the card or SEPA number associated with the token 0123456
response = payzen_client.get_token_details(0123456)
payment_method.number = response.cardResponse.number
```

**Build the data needed to generate the form to register a Credit Card or a SDD mandate**

``` python
data = SEPAMandateFormData(
    user=10,
    payzen_id=0123456,
    update=False,   # if true, update the payment method instead of creating one
    comeback_url=comeback_url,
    payzen_certificate='0000000000000000',
    payzen_shop_id='00000000',
    payzen_context='TEST',
    payzen_version='V2'
)

print(data.signature, data.vads_identifier)
```
