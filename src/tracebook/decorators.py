# src/bookkeeping/decorators.py

from functools import wraps

from .config import LogLevel
from .logger import Logger
from .utils import time_execution

# Create a default logger instance
default_logger = Logger(log_level=LogLevel.INFO, output="console")


def log_function(logger=default_logger):
    """
    Decorator to log function calls, arguments, results, and execution time.

    Args:
        logger (Logger): An instance of the Logger class.

    Returns:
        callable: The decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log function call
            logger.log_function_call(func.__name__, *args, **kwargs)
            try:
                # Measure execution time and get result
                result, exec_time = time_execution(lambda: func(*args, **kwargs))
                # Log result and execution time
                logger.log_result(func.__name__, result)
                logger.log_execution_time(func.__name__, exec_time)
                return result
            except Exception as e:
                # Log exception
                logger.log_exception(func.__name__, e)
                raise  # Re-raise the exception after logging

        return wrapper

    return decorator


def log_function_call(logger=default_logger):
    """
    Decorator to log function calls and arguments.

    Args:
        logger (Logger): An instance of the Logger class.

    Returns:
        callable: The decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log function call
            logger.log_function_call(func.__name__, *args, **kwargs)
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Log exception
                logger.log_exception(func.__name__, e)
                raise  # Re-raise the exception after logging

        return wrapper

    return decorator


def log_result(logger=default_logger):
    """
    Decorator to log function results.

    Args:
        logger (Logger): An instance of the Logger class.

    Returns:
        callable: The decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                # Log result
                logger.log_result(func.__name__, result)
                return result
            except Exception as e:
                # Log exception
                logger.log_exception(func.__name__, e)
                raise  # Re-raise the exception after logging

        return wrapper

    return decorator


def log_execution_time(logger=default_logger):
    """
    Decorator to log the execution time of a function.

    Args:
        logger (Logger): An instance of the Logger class.

    Returns:
        callable: The decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Measure execution time and get result
            result, exec_time = time_execution(lambda: func(*args, **kwargs))
            # Log execution time
            logger.log_execution_time(func.__name__, exec_time)
            return result

        return wrapper

    return decorator
