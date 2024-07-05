"""
This module contains classes for several custom exception types

Custom Exception Types:
------------------------
    AppBaseException:
        base exception for the application
    NotFoundException:
        an exception to be used if a product is not found within the database
    DalException:
        an exception for an error in the data access layer
    BusinessLogicException:
        an exception for an error in business logic (to be honest I'm having trouble remembering how this is different
        from a DalException)

"""


class AppBaseException(Exception):
    pass


class NotFoundException(AppBaseException):
    pass


class DalException(AppBaseException):
    pass


class BusinessLogicException(AppBaseException):
    pass