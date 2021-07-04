class ProviderException(Exception):
    pass

class ProviderRequestException(ProviderException):
    pass

class ConvertException(Exception):
    pass

class CurrencyConvertException(ConvertException):
    pass

class UnitConvertException(ConvertException):
    pass
