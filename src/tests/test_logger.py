import unittest
from unittest.mock import mock_open, patch

from tracebook.config import Config, LogLevel, RemoteConfig
from tracebook.logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.config = Config(
            output="both",
            log_level=LogLevel.DEBUG,  # noqa: F821
            file_path="test.log",
            remote_config=RemoteConfig(None, None, True),
        )
        self.logger = Logger(self.config)

    @patch("tracebook.logger.log_push_file_to_remote_server")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_message_console_and_file(self, mock_open, mock_remote):
        self.logger._save_message("Test message")
        mock_open.assert_called_once_with("test.log", "a")
        handle = mock_open()
        handle.write.assert_called_once_with("Test message\n")
        mock_remote.assert_called_once_with(self.config)

    @patch("tracebook.logger.logging.debug")
    def test_log_function_enter(self, mock_debug):
        with patch("tracebook.logger.current_timestamp", return_value="timestamp"):
            self.logger.log_function_enter("test_func", "param1, param2")
            message = "[timestamp] > Entering function test_func with parameters: param1, param2"
            mock_debug.assert_called_once_with(message)

    @patch("tracebook.logger.logging.debug")
    def test_log_function_exit(self, mock_debug):
        with patch("tracebook.logger.current_timestamp", return_value="timestamp"):
            self.logger.log_function_exit("test_func", "result1")
            message = "[timestamp] < Exiting function test_func with result: result1"
            mock_debug.assert_called_once_with(message)

    @patch("tracebook.logger.logging.debug")
    def test_log_function_call(self, mock_debug):
        with patch("tracebook.logger.current_timestamp", return_value="timestamp"):
            self.logger.log_function_call("test_func", "arg1", kwarg1="value1")
            parameters = "Arguments: ('arg1',), Keyword Arguments: {'kwarg1': 'value1'}"
            message = f"[timestamp] > Entering function test_func with parameters: {parameters}"
            mock_debug.assert_called_once_with(message)

    @patch("tracebook.logger.logging.debug")
    def test_log_exception(self, mock_debug):
        with patch("tracebook.logger.current_timestamp", return_value="timestamp"):
            self.logger.log_exception("test_func", Exception("Test exception"))
            message = "[timestamp] | Exception in function test_func: Test exception"
            mock_debug.assert_called_once_with(message)

    @patch("tracebook.logger.current_timestamp", return_value="timestamp")
    def test_generate_message(self, mock_timestamp):
        result = self.logger._generate_message(">", "Test message")
        self.assertEqual(result, "[timestamp] > Test message")


if __name__ == "__main__":
    unittest.main()
