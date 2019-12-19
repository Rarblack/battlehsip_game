class NotEmptyError(Exception):
    """Raised when point is not empty"""
    pass


class PointOutOfBoardError(Exception):
    """Raised when point exits already on board"""
    pass


class NegativeNumberError(Exception):
    """Raised when negative number is inputted"""
    pass


class NotInDictError(Exception):
    """Raised when input is not in the dictionary"""
    pass


class LessThanTenError(Exception):
    """Raised when input is less than 10"""
    pass


class MoreThanNinetyNineError(Exception):
    """Raised when input is more than 99"""
    pass

