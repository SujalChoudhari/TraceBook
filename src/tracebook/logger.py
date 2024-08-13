import logging
from typing import Literal

from tracebook.config import Config, LogLevel
from tracebook.remote_handler import log_push_file_to_remote_server
from tracebook.utils import current_timestamp


class Logger:
    def __init__(self, config: Config):
        self.config = config

        with open(self.config.file_path, "a") as file:
            file.write(f"=== Starting TraceBook at {current_timestamp()} ===\n")
        if self.config.remote_config.use:
            log_push_file_to_remote_server(self.config)

    def _save_message(self, message: str):
        if self.config.output == "console" or self.config.output == "both":
            if self.config.log_level == LogLevel.DEBUG:
                logging.debug(message)
            elif self.config.log_level == LogLevel.INFO:
                logging.info(message)
            elif self.config.log_level == LogLevel.WARNING:
                logging.warning(message)
            elif self.config.log_level == LogLevel.ERROR:
                logging.error(message)
            elif self.config.log_level == LogLevel.CRITICAL:
                logging.critical(message)

        if self.config.output == "file" or self.config.output == "both":
            with open(self.config.file_path, "a") as file:
                file.write(message + "\n")
            if self.config.remote_config.use:
                log_push_file_to_remote_server(self.config)

    def log_function_enter(self, function_name: str, parameters: str):
        message = self._generate_message(
            ">", f"Entering function {function_name} with parameters: {parameters}"
        )
        self._save_message(message)

    def log_function_exit(self, function_name: str, result: str):
        message = self._generate_message(
            "<", f"Exiting function {function_name} with result: {result}"
        )
        self._save_message(message)

    def log_function_call(self, function_name: str, *args, **kwargs):
        parameters = f"Arguments: {args}, Keyword Arguments: {kwargs}"
        self.log_function_enter(function_name, parameters)

    def log_exception(self, function_name: str, exception: Exception):
        message = self._generate_message(
            "|", f"Exception in function {function_name}: {str(exception)}"
        )
        self._save_message(message)

    def log_details(self, message: str):
        message = self._generate_message("*", f"Details: {message}")
        self._save_message(message)

    def _generate_message(self, operation_symbol: Literal[">", "<", "|"], message):
        return f"[{current_timestamp()}] {operation_symbol} {message}"
