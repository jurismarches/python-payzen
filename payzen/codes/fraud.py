# commons
INVALID_CREDENTIAL = 'INVALID_CREDENCIAL'
COMMUNICATION_PROBLEM = 'COMUNICATION_PROBLEM'
DATA_PROCESSING_PROBLEM = 'DATA_PROCESSING_PROBLEM'
MISSING_MANDATORY_ORDER_INFO = 'MISSING_MANDATORY_ORDER_INFO'
MISSING_MANDATORY_SHIPPING_INFO = 'MISSING_MANDATORY_SHIPPING_INFO'
MISSING_MANDATORY_SHIPPING_ADDRESS_INFO = 'MISSING_MANDATORY_SHIPPING_ADDRESS_INFO'
MISSING_MANDATORY_BILLING_INFO = 'MISSING_MANDATORY_BILLING_INFO'
MISSING_MANDATORY_BILLING_ADDRESS_INFO = 'MISSING_MANDATORY_BILLING_ADDRESS_INFO'
MISSING_MANDATORY_CARD_INFO = 'MISSING_MANDATORY_CARD_INFO'
MISSING_MANDATORY_CUSTOMER_INFO = 'MISSING_MANDATORY_CUSTOMER_INFO'

# clearsale
AUTOMATICALLY_APPROVED = 'APA'
MANUALLY_APPROVED = 'APM'
REPROVED_WITH_NO_SUSPECT = 'RPM'
WAITING_MANUAL_ANALYSIS = 'AMA'
ERROR = 'ERR'
WAITING_SCORE = 'NVO'
FRAUD_SUSPICION = 'SUS'
CANCELLED_BY_USER = 'CAN'
FRAUD = 'FRD'
AUTOMATICALLY_REPROVED_BY_RISK_ANALYZER = 'RPA'
AUTOMATICALLY_REPROVED_BY_CUSTOMER_OR_CLEARSALE = 'RPP'

# cybersource
SUCCESS = '100'
MISSING_FIELDS = '101'
INVALID_FIELDS = '102'
ERROR_GENERAL_SYSTEM_FAILURE = '150'
SERVER_TIME_OUT = '151'
SERVICE_TIME_OUT = '152'
CARD_EXPIRED = '202'
ACCOUNT_NUMBER_INVALID = '231'
ACCOUNT_PROBLEM = '234'
FRAUD_SCORE_TOO_HIGH = '400'
SUCCESS_TO_REVIEW = '480'
SUCCESS_TO_REJECT = '481'

LABELS = {
    INVALID_CREDENTIAL: 'Configuration problem of the risk analyzer contract',
    COMMUNICATION_PROBLEM: 'Miscommunication',
    DATA_PROCESSING_PROBLEM: 'Problem while processing the request data',
    MISSING_MANDATORY_ORDER_INFO: 'Order information missing',
    MISSING_MANDATORY_SHIPPING_INFO: 'Shipping information missing',
    MISSING_MANDATORY_SHIPPING_ADDRESS_INFO: 'Shipping address information'
                                             ' missing',
    MISSING_MANDATORY_BILLING_INFO: 'Billing information missing',
    MISSING_MANDATORY_BILLING_ADDRESS_INFO: 'Billing information missing',
    MISSING_MANDATORY_CARD_INFO: 'Payment method information missing',
    MISSING_MANDATORY_CUSTOMER_INFO: 'Buyer information missing',
    AUTOMATICALLY_APPROVED: 'Automatically approved',
    MANUALLY_APPROVED:
        'Manually approved - order manually approved by analyst\'s decision',
    REPROVED_WITH_NO_SUSPECT: 'Reproved with no suspect',
    WAITING_MANUAL_ANALYSIS: 'Waiting for manual analysis - order is in a'
                             ' queue waiting for analysis',
    ERROR: 'Error',
    WAITING_SCORE: 'New order - order waiting for score',
    FRAUD_SUSPICION: 'Suspended order - order suspended by fraud suspicion',
    CANCELLED_BY_USER: 'Canceled - order canceled by user',
    FRAUD: 'Order confirmed as a fraud',
    AUTOMATICALLY_REPROVED_BY_RISK_ANALYZER:
        'Automatically reproved based on parameters within risk analyzer',
    AUTOMATICALLY_REPROVED_BY_CUSTOMER_OR_CLEARSALE:
        'Automatically reproved based customer or ClearSale policy',
    SUCCESS: 'The transaction is successfully completed',
    MISSING_FIELDS:
        'The transaction has been declined.'
        ' One or more parameters are missing',
    INVALID_FIELDS:
        'The transaction has been declined.'
        ' One or more parameters contain invalid data',
    ERROR_GENERAL_SYSTEM_FAILURE: 'Error',
    SERVER_TIME_OUT:
        'Error. The request was received but the time limit has been exceeded.'
        ' This error does not include timeouts'
        ' between the client and the server',
    SERVICE_TIME_OUT:
        'Error. The request was received '
        'but a service was not completed in time',
    CARD_EXPIRED: 'Declined. Card expired',
    ACCOUNT_NUMBER_INVALID: 'Declined. Invalid card number',
    ACCOUNT_PROBLEM:
        'Declined. A problem occurred'
        ' with the merchant CyberSource configuration',
    FRAUD_SCORE_TOO_HIGH:
        'Declined. The score of the fraud exceeds the tolerance',
    SUCCESS_TO_REVIEW:
        'The order is marked and needs to be reviewed by the Decision Manager',
    SUCCESS_TO_REJECT:
        'The order has been declined by Decision Manager',
}