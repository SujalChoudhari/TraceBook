import unittest
from unittest.mock import MagicMock, patch
from tracebook.decorators import (
    trace,
    trace_inputs,
    trace_outputs,
    trace_exceptions,
    trace_resources,
)


class TestDecorators(unittest.TestCase):

    def test_trace_inputs(self):
        logger = MagicMock()

        @trace_inputs(logger)
        def test_func(x, y):
            return x + y

        result = test_func(3, 4)

        # Check that logger methods were called
        logger.log_function_call.assert_called_with("test_func", 3, 4)

        # Check the function result
        self.assertEqual(result, 7)

    def test_trace_outputs(self):
        logger = MagicMock()

        @trace_outputs(logger)
        def test_func(x, y):
            return x + y

        result = test_func(3, 4)

        # Check that logger methods were called
        logger.log_function_exit.assert_called_with("test_func", "7")

        # Check the function result
        self.assertEqual(result, 7)


