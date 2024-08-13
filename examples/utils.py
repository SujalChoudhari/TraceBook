import time
from tracebook.utils import format_stack_trace, current_timestamp, time_execution

try:
    # Some code that might raise an exception
    result = 1 / 0
except Exception as e:
    print(f"Error occurred at {current_timestamp()}: {format_stack_trace(e)}")

# Example of timing a function
def my_function():
    # Some time-consuming operation
    time.sleep(2)
    return "done"

result, exec_time = time_execution(my_function)
print(f"Function executed in {exec_time} seconds")
