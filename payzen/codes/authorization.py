SUCCESSFUL = 0
CONTACT_THE_CARD_ISSUER = 2
INVALID_ACCEPTOR = 3
KEEP_THE_CARD = 4
DO_NOT_HONOR = 5
KEEP_THE_CARD_SPECIAL = 7
CONFIRM_AFTER_IDENTIFICATION = 8
INVALID_TRANSACTION = 12
INVALID_AMOUNT = 13
INVALID_CARDHOLDER_NB = 14
UNKNOWN_ISSUER = 15
CANCELED_BY_BUYER = 17
RETRY_LATER = 19
INCORRECT_RESPONSE = 20
UNSUPPORTED_FILE_UPDATE = 24
UNABLE_TO_LOCATE_REGISTERED_ELM = 25
DUPLICATE_REGISTRATION = 26
FILE_UPDATE_EDIT_ERROR = 38
DENIED_ACCESS_TO_FILE = 28
UNABLE_TO_UPDATE = 29
FORMAT_ERROR = 30
UNKNOWN_ACQUIRER_COMPANY_ID = 31
EXPIRED_CARD1 = 33
FRAUD_SUSPECTED = 34
EXPIRED_CARD2 = 38
LOST_CARD = 41
STOLEN_CARD = 43
INSUFFICIENT_BALANCE = 51
EXPIRED_CARD3 = 54
INCORRECT_SECRET_CODE = 55
CARD_ABSENT_FROM_FILE = 56
TRANSACTION_NOT_ALLOWED1 = 57
TRANSACTION_NOT_ALLOWED2 = 58
SUSPECTED_FRAUD = 59
CARD_ACCEPTOR_MUST_CONTACT_ACQUIRER = 60
WITHDRAWAL_LIMIT_EXCEED = 61
SECURITY_RULES_UNFULFILLED = 63
RESPONSE_TIMEOUT = 68
NB_PIN_ATTEMPS_EXCEEDED = 75
CARDHOLDER_BLOCKED = 76
TEMPORARY_SHUTDOWN = 90
UNABLE_TO_REACH_CARD_USER = 91
DUPLICATE_TRANSACTION = 94
SYSTEM_MALFUNCTION = 96
OVERALL_MONITORING_TIMEOUT = 97
SERVER_NOT_AVAILABLE = 98
INITIATOR_DOMAIN_REQUEST = 99

LABELS = {
    SUCCESSFUL: 'Approved or successfully processed transaction',
    CONTACT_THE_CARD_ISSUER: 'Contact the card issuer',
    INVALID_ACCEPTOR: 'Invalid acceptor',
    KEEP_THE_CARD: 'Keep the card',
    DO_NOT_HONOR: 'Do not honor',
    KEEP_THE_CARD_SPECIAL: 'Keep the card, special conditions',
    CONFIRM_AFTER_IDENTIFICATION: 'Confirm after identification',
    INVALID_TRANSACTION: 'Invalid transaction',
    INVALID_AMOUNT: 'Invalid amount',
    INVALID_CARDHOLDER_NB: 'Invalid cardholder number',
    UNKNOWN_ISSUER: 'Unknown issuer',
    CANCELED_BY_BUYER: 'Canceled by the buyer',
    RETRY_LATER: 'Retry later',
    INCORRECT_RESPONSE: 'Incorrect response (error on the domain server)',
    UNSUPPORTED_FILE_UPDATE: 'Unsupported file update',
    UNABLE_TO_LOCATE_REGISTERED_ELM:
        'Unable to locate the registered elements in the file',
    DUPLICATE_REGISTRATION:
        'Duplicate registration, the previous record has been replaced',
    FILE_UPDATE_EDIT_ERROR: 'File update edit error',
    DENIED_ACCESS_TO_FILE: 'Denied access to file',
    UNABLE_TO_UPDATE: 'Unable to update',
    FORMAT_ERROR: 'Format error',
    UNKNOWN_ACQUIRER_COMPANY_ID: 'Unknown acquirer company ID',
    EXPIRED_CARD1: 'Expired card',
    FRAUD_SUSPECTED: 'Fraud suspected',
    EXPIRED_CARD2: 'Expired card',
    LOST_CARD: 'Lost card',
    STOLEN_CARD: 'Stolen card',
    INSUFFICIENT_BALANCE: 'Insufficient balance or exceeded credit limit',
    EXPIRED_CARD3: 'Expired card',
    INCORRECT_SECRET_CODE: 'Incorrect secret code',
    CARD_ABSENT_FROM_FILE: 'Card absent from the file',
    TRANSACTION_NOT_ALLOWED1: 'Transaction not allowed to this cardholder',
    TRANSACTION_NOT_ALLOWED2: 'Transaction not allowed to this cardholder',
    SUSPECTED_FRAUD: 'Suspected fraud',
    CARD_ACCEPTOR_MUST_CONTACT_ACQUIRER:
        'Card acceptor must contact the acquirer',
    WITHDRAWAL_LIMIT_EXCEED: 'Withdrawal limit exceeded',
    SECURITY_RULES_UNFULFILLED: 'Security rules unfulfilled',
    RESPONSE_TIMEOUT: 'Response not received or received too late',
    NB_PIN_ATTEMPS_EXCEEDED:
        'Number of attempts for entering the secret code has been exceeded',
    CARDHOLDER_BLOCKED:
        'The cardholder is already blocked, '
        'the previous record has been saved',
    TEMPORARY_SHUTDOWN: 'Temporary shutdown',
    UNABLE_TO_REACH_CARD_USER: 'Unable to reach the card issuer',
    DUPLICATE_TRANSACTION: 'Duplicate transaction',
    SYSTEM_MALFUNCTION: 'System malfunction',
    OVERALL_MONITORING_TIMEOUT: 'Overall monitoring timeout',
    SERVER_NOT_AVAILABLE: 'Server not available, new network route requested',
    INITIATOR_DOMAIN_REQUEST: 'Initiator domain incident',
}

GROUNDS_OF_FRAUD = [
    INVALID_ACCEPTOR,
    KEEP_THE_CARD,
    DO_NOT_HONOR,
    KEEP_THE_CARD_SPECIAL,
    INVALID_TRANSACTION,
    INVALID_AMOUNT,
    INVALID_CARDHOLDER_NB,
    UNKNOWN_ISSUER,
    UNKNOWN_ACQUIRER_COMPANY_ID,
    EXPIRED_CARD1,
    FRAUD_SUSPECTED,
    LOST_CARD,
    STOLEN_CARD,
    EXPIRED_CARD3,
    CARD_ABSENT_FROM_FILE,
    TRANSACTION_NOT_ALLOWED1,
    SUSPECTED_FRAUD,
    SECURITY_RULES_UNFULFILLED,
    CARDHOLDER_BLOCKED,
]
