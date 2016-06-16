TRANSACTION_NOT_FOUND1 = 1
TRANSACTION_NOT_FOUND2 = 2
NOT_AUTHORIZED_WITH_STATUS = 3
NOT_AUTHORIZED_IN_CONTEXT = 4
TRANSACTION_ALREADY_EXISTS = 5
INVALID_TRANSACTION_AMOUNT = 6
NOT_ANYMORE_POSSIBLE = 7
NOT_ALLOWED_WITH_DATE_EXPIRATION = 8
CVV_MANDATORY = 9

REFUND_GREATER = 10
TOTAL_REFUND_GREATER = 11
REFUND_DUPLICATION_NOT_ALLOWED = 12
TECHNICAL_PROBLEM1 = 13
TECHNICAL_PROBLEM2 = 14
TECHNICAL_PROBLEM3 = 15
TECHNICAL_PROBLEM4 = 16
FAILED_AURORE_MERCHANT_CONF = 17
FAILED_CETELEM = 18
UNKNOW_CURRENCY = 19

INVALID_CARD_TYPE = 20
MERCHANT_ID_NOT_FOUND = 21
SHOP_NOT_FOUND = 22
AMBIGUOUS_MERCHANT_ID = 23
INVALID_MERCHANT_ID = 24
TECHNICAL_PROBLEM5 = 25
INVALID_CARD_NUMBER1 = 26
INVALID_CARD_NUMBER2 = 27
INVALID_CARD_NUMBER3 = 28
INVALID_CARD_NUMBER4 = 29

INVALID_CARD_NUMBER_LUHN = 30
INVALID_CARD_NUMBER_LENGTH = 31
INVALID_CARD_NUMBER_NOT_FOUND1 = 32
INVALID_CARD_NUMBER_NOT_FOUND2 = 33
FAILED_CARD_SYSTEMATIC_VERIFICATION = 34
FAILED_ECARD_VERIFICATION = 35
REFUSED_BY_RISK_MANAGEMENT = 36
INTERRUPTION_NOT_PROCESSED_DURING_PAYMENT = 37
TECHNICAL_PROBLEM6 = 38
REFUSED_3DS = 39

TECHNICAL_PROBLEM7 = 40
TECHNICAL_PROBLEM8 = 41
INTERNAL_ERROR_CONSULTING_CARD_NUMBER1 = 42
INTERNAL_ERROR_CONSULTING_CARD_NUMBER2 = 43
UNABLE_TO_FORCE_AUTHORIZATION_1_EURO = 44
INVALID_CURRENCY_FOR_MODIFICATION = 45
AMOUNT_GREATER_THAN_AUTHORIZED = 46
CAPTURE_DATE_GREATER_THAN_EXPIRATION = 47
INVALID_MODIFICATION = 48
INVALID_INSTALLMENT_PAYMENT = 49

UNKNOWN_SHOP = 50
UNKNOWN_EXCHANGE_RATE = 51
MERCHANT_ID_TERMINATED = 52
SHOP_CLOSED = 53
REJECTED_PARAM_MAY_CONTAIN_SENSITIVE_DATA = 54
TECHNICAL_PROBLEM9 = 55
ERROR_WHILE_RETRIEVING_THE_TOKEN1 = 57
TOKEN_STATUS_INCOMPATIBLE_WITH_OPERATION = 58
ERROR_WHILE_RETRIEVING_THE_TOKEN2 = 59

TOKEN_ALREADY_EXISTS = 60
INVALID_TOKEN = 61
TOKEN_CREATION_FAILED = 62
SUBSCRIPTION_ALREADY_EXISTS = 63
SUBSCRIPTION_ALREADY_TERMINATED = 64
INVALID_SUBSCRIPTION = 65
INVALID_RECCURENT_RULE = 66
SUBSCRIPTION_CREATION_FAILED = 67
TECHNICAL_PROBLEM10 = 69
INVALID_COUNTRY_CODE = 70

INVALID_WEB_SERVICE_PARAM = 71
AUTHORIZATION_DECLINED_BY_COFINOGA = 72
DECLINED_AUTHORIZATION_1_EURO = 73
INVALID_PAYMENT_CONFIGURATION = 74
REJECTED_BY_PAYPAL = 75
TECHNICAL_PROBLEM11 = 76
TECHNICAL_PROBLEM12 = 77
TRANSACTION_ID_MISSING = 78
TRANSACTION_ID_ALREADY_USED = 79

TRANSACTION_ID_EXPIRED = 80
INVALID_CONTENT_OF_THEME_CONF = 81
REFUND_NOT_AUTHORIZED1 = 82
AMOUNT_NOT_IN_ALLOWED_VALUES = 83
TECHNICAL_PROBLEM13 = 84
TECHNICAL_PROBLEM14 = 85
TECHNICAL_PROBLEM15 = 86
TECHNICAL_PROBLEM16 = 87
TECHNICAL_PROBLEM17 = 88
MODIFICATION_NOT_AUTHORIZED = 89

ERROR_WHILE_REFUNDING = 90
NO_PAYMENT_OPTION_ENABLED = 91
ERROR_WHILE_CALCULATING_PAYMENT_CHANNEL = 92
ERROR_WHILE_REDIRECTING_CUST_TO_FINAL = 93
TECHNICAL_PROBLEM18 = 94
TECHNICAL_PROBLEM19 = 95
ERROR_WHILE_CAPTURING_TRANSACTION1 = 96
CAPTURE_DATE_TOO_LATE = 97
INVALID_TRANSACTION_DATE = 98
ERROR_WHILE_CALCULATING_PAYMENT_SOURCE = 99

FAILED_COMMERCIAL_CARD_VERIFICATION = 100
REJECTED_DUE_TO_FIRST_INSTALLMENT_REFUSAL = 101
DECLINED_BY_BUYSTER = 102
STATUS_SYNCHRO_WITH_EXTERNAL_SYSTEM_IMPOSSIBLE = 103
ERROR_WHILE_CAPTURING_TRANSACTION2 = 104
SECURITY_ERROR_WHILE_PROCESSING_3DS = 105
UNSUPPORTED_CURRENCY_FOR_MERCHANT = 106
CARD_NOW_INVALID = 107
TECHNICAL_PROBLEM20 = 108
TIMEOUT_WHILE_USER_REDIRECTION = 109

CARD_UNSUPPORTED_BY_MERCHANT = 110
TRANSACTION_DECLINED_WITHOUT_LIABILITY_SHIFT = 111
CANCELLATION_NOT_AUTHORIZED = 112
DUPLICATION_NOT_AUTHORIZED = 113
OVERRIDE_NOT_AUTHORIZED = 114
REFUND_NOT_AUTHORIZED2 = 115
MANUAL_PAYMENT_NOT_AUTHORIZED = 116
MANUAL_INSTALLMENT_PAYMENT_NOT_AUTHORIZED = 118
SUBMITTED_DATE_INVALID = 119

INITIAL_TRANSACTION_NOT_APPLICABLE = 120
INACTIVE_CARD = 124
PAYMENT_REFUSED_BY_ACQUIRER = 125
IMPOSSIBLE_ACTION_AS_PAYMENT_SEQUENCE_NOT_COMPLETED = 126
TECHNICAL_PROBLEM21 = 132
FORM_IN_IFRAME_FORBIDDEN = 135
DERIVATIVE_TRANSACTION_DECLINED_WITHTOUT_RESPONSABILITY_TRANSFER = 136
DUPLICATE_TRANSACTION = 137
PARTIAL_REFUND_IMPOSSIBLE = 138
REFUND_DECLINED = 139
TRANSACTION_REFUSED_DUE_TO_RISK_ANALYZER = 141
CARD_TYPE_INVALID_FOR_PAYMENT_MODE = 142
TECHNICAL_PROBLEM22 = 143
TRANSACTION_IN_PRODUCTION_MODE_MARKED_AS_TEST_BY_ACQUIRER = 143
TRANSACTION_IN_TEST_MODE_MARKED_AS_PRODUCTION_BY_ACQUIRER = 144
INVALID_SMS_CODE = 146
RISK_MANAGEMENT_ASK_TO_DECLINED = 147
TECHNICAL_PROBLEM23 = 148
EXPIRED_PAYMENT_SESSION = 149
TECHNICAL_PROBLEM24 = 150

LABELS = {
    TRANSACTION_NOT_FOUND1: 'Transaction not found',
    TRANSACTION_NOT_FOUND2: 'Transaction not found',
    NOT_AUTHORIZED_WITH_STATUS:
        'This action has not been authorized '
        'for a transaction with the {0} status',
    NOT_AUTHORIZED_IN_CONTEXT:
        'This transaction is not authorized in this context',
    TRANSACTION_ALREADY_EXISTS: 'This transaction already exists',
    INVALID_TRANSACTION_AMOUNT: 'Invalid transaction amount',
    NOT_ANYMORE_POSSIBLE:
        'This action is not possible anymore '
        'for a transaction created on that day',
    NOT_ALLOWED_WITH_DATE_EXPIRATION:
        'The card expiration date does not allow this action',
    CVV_MANDATORY: 'CVV mandatory for this card',
    REFUND_GREATER: 'The refund amount is greater than the initial amount',
    TOTAL_REFUND_GREATER:
        'The refunds total amount is greater than the initial amount',
    REFUND_DUPLICATION_NOT_ALLOWED:
        'Credit duplication (refund) is not authorized',
    TECHNICAL_PROBLEM1:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM2:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM3:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM4:
        'Due to a technical problem, we are unable to process your request',
    FAILED_AURORE_MERCHANT_CONF:
        'Aurore Merchant ID (MID) configuration has failed',
    FAILED_CETELEM: 'Cetelem response analysis has failed',
    UNKNOW_CURRENCY: 'Unknown currency',
    INVALID_CARD_TYPE: 'Invalid card type',
    MERCHANT_ID_NOT_FOUND:
        'No Merchant ID (MID) found for this payment. Please modify the data '
        'or contact your manager in case the error reoccurs',
    SHOP_NOT_FOUND: 'Shop not found',
    AMBIGUOUS_MERCHANT_ID: 'Ambiguous Merchant ID (MID)',
    INVALID_MERCHANT_ID: 'Invalid Merchant ID (MID)',
    TECHNICAL_PROBLEM5:
        'Due to a technical problem, we are unable to process your request',
    INVALID_CARD_NUMBER1: 'Invalid card number',
    INVALID_CARD_NUMBER2: 'Invalid card number',
    INVALID_CARD_NUMBER3: 'Invalid card number',
    INVALID_CARD_NUMBER4: 'Invalid card number',
    INVALID_CARD_NUMBER_LUHN: 'Invalid card number (Luhn)',
    INVALID_CARD_NUMBER_LENGTH: 'Invalid card number (length)',
    INVALID_CARD_NUMBER_NOT_FOUND1: 'Invalid card number (not found)',
    INVALID_CARD_NUMBER_NOT_FOUND2: 'Invalid card number (not found)',
    FAILED_CARD_SYSTEMATIC_VERIFICATION:
        'Failed verification of the card requiring systematic verification',
    FAILED_ECARD_VERIFICATION:
        'Failed e-Carte Bleue verification',
    REFUSED_BY_RISK_MANAGEMENT:
        'The transaction has been refused by risk management',
    INTERRUPTION_NOT_PROCESSED_DURING_PAYMENT:
        'Interruption not processed during the payment',
    TECHNICAL_PROBLEM6:
        'Due to a technical problem, we are unable to process your request',
    REFUSED_3DS: '3D Secure refusal for the transaction',
    TECHNICAL_PROBLEM7:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM8:
        'Due to a technical problem, we are unable to process your request',
    INTERNAL_ERROR_CONSULTING_CARD_NUMBER1:
        'An internal error occurred while consulting the card number',
    INTERNAL_ERROR_CONSULTING_CARD_NUMBER2:
        'An internal error occurred while consulting the card number',
    UNABLE_TO_FORCE_AUTHORIZATION_1_EURO: 'Unable to force an authorization for 1 euro',
    INVALID_CURRENCY_FOR_MODIFICATION: 'Invalid currency for the modification',
    AMOUNT_GREATER_THAN_AUTHORIZED:
        'The amount is greater than the authorized amount',
    CAPTURE_DATE_GREATER_THAN_EXPIRATION:
        'The desired capture date exceeds the authorization expiration date',
    INVALID_MODIFICATION: 'The requested modification is invalid',
    INVALID_INSTALLMENT_PAYMENT:
        'Invalid definition of the installment payment',
    UNKNOWN_SHOP: 'Unknown shop',
    UNKNOWN_EXCHANGE_RATE: 'Unknown exchange rate',
    MERCHANT_ID_TERMINATED:
        'The Merchant ID (MID) has been terminated since {0}',
    SHOP_CLOSED: 'The shop {0} has been closed since {1}',
    REJECTED_PARAM_MAY_CONTAIN_SENSITIVE_DATA:
        'Rejected parameter that may contain sensitive data {0}',
    TECHNICAL_PROBLEM9:
        'Due to a technical problem, we are unable to process your request',
    ERROR_WHILE_RETRIEVING_THE_TOKEN1:
        'An error occurred while retrieving the token',
    TOKEN_STATUS_INCOMPATIBLE_WITH_OPERATION:
        'The token status is not compatible with this operation',
    ERROR_WHILE_RETRIEVING_THE_TOKEN2:
        'An error occurred while retrieving the token',
    TOKEN_ALREADY_EXISTS: 'This token already exists',
    INVALID_TOKEN: 'Invalid token',
    TOKEN_CREATION_FAILED: 'Token creation failed',
    SUBSCRIPTION_ALREADY_EXISTS: 'This subscription already exists',
    SUBSCRIPTION_ALREADY_TERMINATED: 'This subscription is already terminated',
    INVALID_SUBSCRIPTION: 'Invalid subscription',
    INVALID_RECCURENT_RULE: 'Invalid recurrence rule',
    SUBSCRIPTION_CREATION_FAILED: 'Subscription creation failed',
    TECHNICAL_PROBLEM10:
        'Due to a technical problem, we are unable to process your request',
    INVALID_COUNTRY_CODE: 'Invalid country code',
    INVALID_WEB_SERVICE_PARAM: 'Invalid web service parameter',
    AUTHORIZATION_DECLINED_BY_COFINOGA:
        'The authorization has been declined by Cofinoga',
    DECLINED_AUTHORIZATION_1_EURO:
        'The authorization for 1 euro has been declined',
    INVALID_PAYMENT_CONFIGURATION: 'Invalid payment configuration',
    REJECTED_BY_PAYPAL: 'The operation has been rejected by PayPal',
    TECHNICAL_PROBLEM11:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM12:
        'Due to a technical problem, we are unable to process your request',
    TRANSACTION_ID_MISSING: 'Transaction ID missing',
    TRANSACTION_ID_ALREADY_USED: 'This transaction ID is already used',
    TRANSACTION_ID_EXPIRED: 'Transaction ID expired',
    INVALID_CONTENT_OF_THEME_CONF:
        'Invalid contents of the configuration theme',
    REFUND_NOT_AUTHORIZED1: 'The refund is not authorized',
    AMOUNT_NOT_IN_ALLOWED_VALUES:
        'The transaction amount does not respect the allowed values',
    TECHNICAL_PROBLEM13:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM14:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM15:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM16:
        'Due to a technical problem, we are unable to process your request',
    TECHNICAL_PROBLEM17:
        'Due to a technical problem, we are unable to process your request',
    MODIFICATION_NOT_AUTHORIZED: 'The modification is not authorized',
    ERROR_WHILE_REFUNDING: 'An error occurred during refund',
    NO_PAYMENT_OPTION_ENABLED:
        'No payment options have been enabled for this Merchant ID (MID)',
    ERROR_WHILE_CALCULATING_PAYMENT_CHANNEL:
        'An error occurred while calculating the payment channel',
    ERROR_WHILE_REDIRECTING_CUST_TO_FINAL:
        'An error occurred during buyer redirection '
        'to the page of payment finalization',
    TECHNICAL_PROBLEM18: 'A technical error has occurred',
    TECHNICAL_PROBLEM19:
        'Due to a technical problem, we are unable to process your request',
    ERROR_WHILE_CAPTURING_TRANSACTION1:
        'An error occurred at the moment of capture of this transaction',
    CAPTURE_DATE_TOO_LATE: 'The capture date is too late',
    INVALID_TRANSACTION_DATE: 'Invalid transaction date',
    ERROR_WHILE_CALCULATING_PAYMENT_SOURCE:
        'An error occurred while calculating the payment source',
    FAILED_COMMERCIAL_CARD_VERIFICATION: 'Failed commercial card verification',
    REJECTED_DUE_TO_FIRST_INSTALLMENT_REFUSAL:
        'Rejected due to the refusal of the first installment',
    DECLINED_BY_BUYSTER: 'The operation has been declined by Buyster',
    STATUS_SYNCHRO_WITH_EXTERNAL_SYSTEM_IMPOSSIBLE:
        'The transaction status could not be synchronized '
        'with the external system',
    ERROR_WHILE_CAPTURING_TRANSACTION2:
        'An error occurred at the moment of capture of this transaction',
    SECURITY_ERROR_WHILE_PROCESSING_3DS:
        'A security error occurred while processing 3DS '
        'authorization for this transaction',
    UNSUPPORTED_CURRENCY_FOR_MERCHANT:
        'Unsupported currency for this Merchant ID (MID) and/or shop',
    CARD_NOW_INVALID:
        'The card associated with the token is not valid anymore',
    TECHNICAL_PROBLEM20:
        'Due to a technical problem, we are unable to process your request',
    TIMEOUT_WHILE_USER_REDIRECTION:
        'The timeout has been exceeded during buyer redirection',
    CARD_UNSUPPORTED_BY_MERCHANT:
        'Payment card not supported by the Merchant ID (MID)',
    TRANSACTION_DECLINED_WITHOUT_LIABILITY_SHIFT:
        'The transactions have been declined without liability shift',
    CANCELLATION_NOT_AUTHORIZED: 'Cancellation is not authorized',
    DUPLICATION_NOT_AUTHORIZED: 'Duplication is not authorized',
    OVERRIDE_NOT_AUTHORIZED: 'Override is not authorized',
    REFUND_NOT_AUTHORIZED2: 'The refund is not authorized',
    MANUAL_PAYMENT_NOT_AUTHORIZED:
        'Manual payment not authorized for this card',
    MANUAL_INSTALLMENT_PAYMENT_NOT_AUTHORIZED:
        'Manual installment payment not authorized for this card',
    SUBMITTED_DATE_INVALID: 'The submitted date is invalid',
    INITIAL_TRANSACTION_NOT_APPLICABLE:
        'The initial transaction option is not applicable',
    INACTIVE_CARD: 'Inactive card',
    PAYMENT_REFUSED_BY_ACQUIRER: 'Payment refused by the acquirer',
    IMPOSSIBLE_ACTION_AS_PAYMENT_SEQUENCE_NOT_COMPLETED:
        'This action is impossible as the payment sequence '
        'has not been completed',
    TECHNICAL_PROBLEM21:
        'Due to a technical problem, we are unable to process your request',
    FORM_IN_IFRAME_FORBIDDEN:
        'Integration of a payment page into an iframe is not authorized',
    DERIVATIVE_TRANSACTION_DECLINED_WITHTOUT_RESPONSABILITY_TRANSFER:
        'The derivative transactions have been declined without a transfer '
        'of responsibility for the initial transaction',
    DUPLICATE_TRANSACTION: 'Duplicate transaction',
    PARTIAL_REFUND_IMPOSSIBLE:
        'Partial refund is impossible for this transaction',
    REFUND_DECLINED: 'Refund declined',
    TRANSACTION_REFUSED_DUE_TO_RISK_ANALYZER:
        'The transaction has been refused by the risk analyzer',
    CARD_TYPE_INVALID_FOR_PAYMENT_MODE:
        'The card type used is not valid for the requested payment mode',
    TECHNICAL_PROBLEM22:
        'Due to a technical problem, we are unable to process your request',
    TRANSACTION_IN_PRODUCTION_MODE_MARKED_AS_TEST_BY_ACQUIRER:
        'A transaction in production mode has been marked '
        'as in test mode by the acquirer',
    TRANSACTION_IN_TEST_MODE_MARKED_AS_PRODUCTION_BY_ACQUIRER:
        'A transaction in test mode has been marked '
        'as in production mode by the acquirer.',
    INVALID_SMS_CODE: 'Invalid SMS code',
    RISK_MANAGEMENT_ASK_TO_DECLINED:
        'The risk management module has requested '
        'for this transaction to be declined',
    TECHNICAL_PROBLEM23:
        'The risk management module has requested '
        'for this transaction to be declined',
    EXPIRED_PAYMENT_SESSION:
        'The payment session has expired (the buyer has been redirected '
        'to the ACS and has not finalized the 3D Secure authentication',
    TECHNICAL_PROBLEM24:
        'Due to a technical problem, we are unable to process your request. '
        'The transaction has not been created',
}
