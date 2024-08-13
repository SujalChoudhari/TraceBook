from tracebook.logger import Logger, LogLevel
from tracebook.utils import time_execution

# Initialize logger
logger = Logger(log_level=LogLevel.DEBUG, output="console")


def add(a, b):
    logger.log_function_call("add", a, b)
    try:
        result = a + b
        logger.log_result("add", result)
        return result
    except Exception as e:
        logger.log_exception("add", e)


def multiply(a, b):
    logger.log_function_call("multiply", a, b)
    try:
        # Simulating a time-consuming operation
        result, exec_time = time_execution(lambda: a * b)
        logger.log_result("multiply", result)
        logger.log_execution_time("multiply", exec_time)
        return result
    except Exception as e:
        logger.log_exception("multiply", e)


# Function calls
add(5, 3)
multiply(4, 7)

# Example with an error
add("five", 3)
