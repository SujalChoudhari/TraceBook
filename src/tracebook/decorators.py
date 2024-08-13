# tracebook/decorators.py
from functools import wraps
from tracebook.utils import get_memory_usage, get_cpu_usage
from tracebook.logger import Logger  # Assuming the Logger class is in logger.py


def trace(
    logger: Logger,
    log_inputs: bool = True,
    log_outputs: bool = True,
    log_exceptions: bool = True,
    log_resources: bool = False,
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if log_inputs:
                logger.log_function_call(func.__name__, *args, **kwargs)
            try:
                result = func(*args, **kwargs)
                if log_outputs:
                    logger.log_function_exit(func.__name__, str(result))
                return result
            except Exception as e:
                if log_exceptions:
                    logger.log_exception(func.__name__, e)
                raise
            finally:
                if log_resources:
                    cpu_usage = get_cpu_usage()
                    memory_usage = get_memory_usage()
                    logger.log_details(
                        f"CPU Usage: {cpu_usage}, Memory Usage: {memory_usage}"
                    )
        return wrapper

    return decorator


def trace_inputs(logger: Logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log_function_call(func.__name__, *args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def trace_outputs(logger: Logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.log_function_exit(func.__name__, str(result))
            return result

        return wrapper

    return decorator


def trace_exceptions(logger: Logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.log_exception(func.__name__, e)
                raise

        return wrapper

    return decorator


def trace_resources(logger: Logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import time

            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            logger._save_message(
                f"Execution Time: {end_time - start_time} seconds, CPU Usage: {cpu_usage}, Memory Usage: {memory_usage}"
            )
            return result

        return wrapper

    return decorator
