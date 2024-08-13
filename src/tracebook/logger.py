# src/traebook/logger.py

import logging
import sys

from tracebook.utils import format_stack_trace

from .config import LogLevel


class Logger:
    def __init__(self, log_level=LogLevel.INFO, output="console", file_path=None):
        """
        Initialize the Logger.

        Args:
            log_level (LogLevel): The minimum level of logs to capture.
            output (str): Where to send the logs ('console' or 'file').
            file_path (str): The path to the log file (required if output is 'file').
        """
        self.log_level = log_level
        self.output = output

        if output == "file" and file_path is None:
            raise ValueError("file_path must be specified when output is 'file'")

        self.logger = logging.getLogger("TraceBookLogger")
        self.logger.setLevel(log_level)

        if output == "console":
            handler = logging.StreamHandler(sys.stdout)
        elif output == "file":
            handler = logging.FileHandler(file_path)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_function_call(self, func_name, *args, **kwargs):
        """
        Log the call to a function, including parameters.

        Args:
            func_name (str): The name of the function being logged.
            *args: Positional arguments passed to the function.
            **kwargs: Keyword arguments passed to the function.
        """
        if self.log_level <= LogLevel.INFO:
            self.logger.info(
                f"Function '{func_name}' called with args: {args} and kwargs: {kwargs}"
            )

    def log_result(self, func_name, result):
        """
        Log the result of a function.

        Args:
            func_name (str): The name of the function.
            result: The result returned by the function.
        """
        if self.log_level <= LogLevel.INFO:
            self.logger.info(f"Function '{func_name}' returned: {result}")

    def log_execution_time(self, func_name, execution_time):
        """
        Log the execution time of a function.

        Args:
            func_name (str): The name of the function.
            execution_time (float): The time taken to execute the function.
        """
        if self.log_level <= LogLevel.INFO:
            self.logger.info(
                f"Function '{func_name}' executed in {execution_time:.6f} seconds"
            )

    def log_exception(self, func_name, exception):
        """
        Log an exception that occurred during a function call.

        Args:
            func_name (str): The name of the function.
            exception (Exception): The exception raised.
        """
        if self.log_level <= LogLevel.ERROR:
            self.logger.error(
                f"Exception in function '{func_name}': {format_stack_trace(exception)}"
            )
