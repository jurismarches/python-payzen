class SignatureError(Exception):
    """
    Payzen signature check error
    """
    def __init__(self, message, response):
        super().__init__(message)

        self.response = response


class PayzenError(Exception):
    """
    Payzen Error
    """
    def __init__(self, message, error_code, extended_error_code, response):
        super().__init__(message)

        self.error_code = error_code
        self.extended_error_code = extended_error_code
        self.response = response
