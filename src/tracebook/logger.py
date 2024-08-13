# logger.py
import logging
from functools import wraps
from typing import Literal
from tracebook.config import Config, LogLevel
from tracebook.remote_handler import log_push_file_to_remote_server
from tracebook.utils import current_timestamp, get_memory_usage, get_cpu_usage


class LoggerCore:
    def __init__(self, config: Config):
        self.config = config
        with open(self.config.file_path, "a") as file:
            file.write(f"=== Starting TraceBook at {current_timestamp()} ===\n")
        if self.config.remote_config.use:
            log_push_file_to_remote_server(self.config)

        if self.config.show_web:
            from tracebook.dashboard import RealTimeDashboard
            self.dashboard = RealTimeDashboard(
                self.config.file_path, self.config.web_port
            )
            self.dashboard.run()
        else:
            self.dashboard = None

    def _save_message(self, message: str, level: LogLevel = LogLevel.INFO):
        level_str = level.name
        full_message = f"[{level_str}] {message}"

        if self.config.output == "console" or self.config.output == "both":
            self._log_to_console(full_message, level)

        if self.config.output == "file" or self.config.output == "both":
            with open(self.config.file_path, "a") as file:
                file.write(full_message + "\n")
            if self.config.remote_config.use:
                log_push_file_to_remote_server(self.config)

    def _log_to_console(self, message: str, level: LogLevel):
        log_method = {
            LogLevel.DEBUG: logging.debug,
            LogLevel.INFO: logging.info,
            LogLevel.WARNING: logging.warning,
            LogLevel.ERROR: logging.error,
            LogLevel.CRITICAL: logging.critical,
        }.get(level, logging.info)
        log_method(message)

    def log_function_enter(self, function_name: str, parameters: str):
        message = self._generate_message(">", f"{function_name} {parameters}")
        self._save_message(message, LogLevel.INFO)

    def log_function_exit(self, function_name: str, result: str):
        message = self._generate_message("<", f"{function_name} {result}")
        self._save_message(message, LogLevel.INFO)

    def log_function_call(self, function_name: str, *args, **kwargs):
        parameters = f"{args} {kwargs}"
        self.log_function_enter(function_name, parameters)

    def log_exception(self, function_name: str, exception: Exception):
        message = self._generate_message("|", f"{function_name} {str(exception)}")
        self._save_message(message, LogLevel.ERROR)

    def log_details(self, message: str, level: LogLevel = LogLevel.INFO):
        message = self._generate_message("*", message)
        self._save_message(message, level)

    def _generate_message(self, operation_symbol: Literal[">", "<", "|", "*"], message):
        return f"{current_timestamp()} {operation_symbol} {message}"
