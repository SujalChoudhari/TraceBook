import time
import traceback


def format_stack_trace(exception):
    """
    Formats the stack trace of an exception into a readable string.

    Args:
        exception (Exception): The exception to format.

    Returns:
        str: The formatted stack trace.
    """
    return "".join(
        traceback.format_exception(
            etype=type(exception), value=exception, tb=exception.__traceback__
        )
    )


def current_timestamp():
    """
    Returns the current timestamp in a readable format.

    Returns:
        str: The current timestamp.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def time_execution(func):
    """
    Measures the execution time of a function.

    Args:
        func (callable): The function to measure.

    Returns:
        tuple: A tuple containing the result of the function and the execution time in seconds.
    """
    start_time = time.time()
    result = func()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time
