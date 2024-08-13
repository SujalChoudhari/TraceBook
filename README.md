# Trace Book

**Trace Book** is a Python package designed for comprehensive code bookkeeping. It provides tools to log function calls, parameters, return values, and execution times. Additionally, it supports decorators for easy integration, automatic error tracking, and remote log transmission, all with customizable log levels and output configurations.

## Features

- **Function Logging**: Track function calls, parameters, return values, and execution times.
- **Automatic Error Tracking**: Log exceptions and stack traces automatically.
- **Decorators**: Simplify logging with decorators that track function parameters and results.
- **Remote Log Transmission**: Securely send logs to a remote server.
- **Customizable Log Levels**: Control log verbosity with DEBUG, INFO, WARNING, and ERROR levels.
- **Configurable Output**: Choose between logging to files or transmitting logs to a remote server.

## Installation

You can install **Trace Book** using `pip`:

```bash
pip install tracebook
```

Or by cloning the repository and installing it manually:

```bash
git clone https://github.com/yourusername/tracebook.git
cd tracebook
pip install .
```

## Usage

### Basic Logging

To log function calls, parameters, return values, and execution times, you can use the logging functionality:

```python
from tracebook.logger import Logger

logger = Logger()

def my_function(param1, param2):
    result = param1 + param2
    logger.log_function_call('my_function', param1, param2, result)
    return result

my_function(1, 2)
```

### Using Decorators

To simplify logging, you can use the provided decorators:

```python
from tracebook.decorators import log_function

@log_function
def my_function(param1, param2):
    return param1 + param2

my_function(1, 2)
```

### Remote Log Transmission

To send logs to a remote server:

```python
from tracebook.remote_handler import RemoteLogger

remote_logger = RemoteLogger(server_url="https://yourserver.com/log", api_key="yourapikey")

def my_function(param1, param2):
    result = param1 + param2
    remote_logger.log_function_call('my_function', param1, param2, result)
    return result

my_function(1, 2)
```

### Configuring Log Levels

Control the verbosity of logs by setting the log level:

```python
from tracebook.logger import Logger
from tracebook.config import LogLevel

logger = Logger(log_level=LogLevel.DEBUG)

def my_function(param1, param2):
    result = param1 + param2
    logger.log_function_call('my_function', param1, param2, result)
    return result

my_function(1, 2)
```

### Configuring Output

You can choose whether to log to a file or send logs to a remote server by configuring the output:

```python
from tracebook.logger import Logger

logger = Logger(output="file", file_path="logs.txt")

def my_function(param1, param2):
    result = param1 + param2
    logger.log_function_call('my_function', param1, param2, result)
    return result

my_function(1, 2)
```

## Documentation

For more detailed documentation, including advanced usage, configuration options, and examples, please refer to the `docs/` directory or visit the online documentation at [https://yourdocslink.com](https://yourdocslink.com).

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
