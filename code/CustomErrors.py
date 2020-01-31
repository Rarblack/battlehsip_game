class NotEmptyError(Exception):
    """Raised when point is not empty"""
    pass


class NotInRangeError(Exception):
    """Raised when input is not within given range"""
    pass


class PointOutOfBoardError(Exception):
    """Raised when point exits already on board"""
    pass


class NotInDictError(Exception):
    """Raised when input is not in the dictionary"""
    pass


class NotAllowedNumberError(Exception):
    """Raised when input is within [10-100) boundary"""
    pass

