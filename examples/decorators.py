from tracebook.decorators import (
    log_execution_time,
    log_function,
    log_function_call,
    log_result,
)


@log_function()  # Logs call, result, and execution time
def add(a, b):
    return a + b


@log_function_call()  # Logs only the function call
def multiply(a, b):
    return a * b


@log_result()  # Logs only the result
def subtract(a, b):
    return a - b


@log_execution_time()  # Logs only the execution time
def divide(a, b):
    return a / b


# Function calls
add(5, 3)
multiply(4, 7)
subtract(10, 4)
divide(8, 2)
