# Base error codes
SUCCESS = 0
NOT_AUTHORIZED = 1
BAD_PARAMETER = 2

TRANSACTION_NOT_FOUND = 10
BAD_TRANSACTION_STATUS = 11
TRANSACTION_ALREADY_EXISTS = 12
DATE_TOO_FAR = 13
NO_CHANGE = 14
TOO_MUCH_RESULTS = 15

BAD_AMOUNT = 20
UNKNOWN_CURRENCY = 21
UNKNOWN_CARD_TYPE = 22
INVALID_EXPIRATION_DATE = 23
CVV_MANDATORY = 24
CONTRACT_NOT_FOUND = 25
INVALID_CARD_NUMBER = 26

PAYMENT_TOKEN_NOT_FOUND = 30
INVALID_PAYMENT_TOKEN = 31
SUBSCRIPTION_ID_NOT_FOUND = 32
INVALID_SUBSCRIPTION = 33
PAYMENT_TOKEN_ALREADY_EXISTS = 34
PAYMENT_TOKEN_CREATION_DECLINED = 35
PAYMENT_TOKEN_PURGED = 36

AMOUNT_NOT_AUTHORIZED = 40
CARD_RANGE_NOT_FOUND = 41
NOT_ENOUGH_CREDIT = 42
NO_CREDIT = 43

BRAND_NOT_FOUND = 50
MERCHANT_NOT_ENROLLED = 51
INVALID_ACS_SIGNATURE = 52
TECHNICAL_ERROR_3DS = 53
WRONG_PARAMETER_3DS = 54
DISABLED_3DS = 55
PAN_NOT_FOUND = 56

ONEY_WS_ERROR = 97
BAD_REQUEST_ID = 98
UNDEFINED_ERROR = 99

LABELS = {
    SUCCESS: "Action successfully completed",
    NOT_AUTHORIZED: "Unauthorized request",
    BAD_PARAMETER: "Bad Parameter",
    TRANSACTION_NOT_FOUND: "Transaction was not found",
    BAD_TRANSACTION_STATUS: "Bad transaction status",
    TRANSACTION_ALREADY_EXISTS: "Transaction already exists",
    DATE_TOO_FAR: "Date is too far from current UTC date",
    NO_CHANGE: "Nothing has changed",
    TOO_MUCH_RESULTS: "Too much results",
    BAD_AMOUNT: "Bad amount",
    UNKNOWN_CURRENCY: "Unknown currency",
    UNKNOWN_CARD_TYPE: "Unknown card type",
    INVALID_EXPIRATION_DATE: "Invalid Expiration Date",
    CVV_MANDATORY: "CVV Mandatory",
    CONTRACT_NOT_FOUND: "Contract not found",
    INVALID_CARD_NUMBER: "Invalid card number",
    PAYMENT_TOKEN_NOT_FOUND: "Payment token not found",
    INVALID_PAYMENT_TOKEN: "Invalid payment token Invalid token (cancelled, ...)",
    SUBSCRIPTION_ID_NOT_FOUND: "SubscriptionID was not found",
    INVALID_SUBSCRIPTION: "Invalid Subscription",
    PAYMENT_TOKEN_ALREADY_EXISTS: "Payment token already exists",
    PAYMENT_TOKEN_CREATION_DECLINED: "Payment token creation declined",
    PAYMENT_TOKEN_PURGED: "Payment token purged",
    AMOUNT_NOT_AUTHORIZED: "Amount not authorized",
    CARD_RANGE_NOT_FOUND: "Card range not found",
    NOT_ENOUGH_CREDIT: "Not enough credit",
    NO_CREDIT: "No credit",
    BRAND_NOT_FOUND: "Brand not found",
    MERCHANT_NOT_ENROLLED: "Merchant not enrolled",
    INVALID_ACS_SIGNATURE: "Invalid ACS Signature",
    TECHNICAL_ERROR_3DS: "Technical error 3DS",
    WRONG_PARAMETER_3DS: "Wrong Parameter 3DS",
    DISABLED_3DS: "3DS Disabled",
    PAN_NOT_FOUND: "PAN not found",
    ONEY_WS_ERROR: "OneyWsError",
    BAD_REQUEST_ID: "Bad request Id",
    UNDEFINED_ERROR: "Undefined Error",
}
