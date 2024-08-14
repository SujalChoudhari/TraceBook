from tracebook import Logger
from tracebook.config import Config, LogLevel, WebUIConfig


logger = Logger(
    config=Config(
        log_level=LogLevel.INFO,
        output="both",
        file_path="test.log",
        web_config=WebUIConfig(
            title="MyTraceBook Dashboard ",
            foreground_color="#003456",
            background_color="#F0F0FF",
            show_star_on_github=False,
            indent_logs=False,
            is_active=True,
            port=2234,
            refresh_interval=2000,
            max_data_points=200,
        ),
    ),
)


@logger.trace(log_resources=True)
def fact(x):
    if x == 0:
        logger.critical("A print statemment above warning")
        logger.warning("A print statemment above error")
        logger.error("A print statemment above info")
        logger.info("A print statemment above 0/0")
        return 0 / 0
    else:
        return x * fact(x - 1)


@logger.trace(log_resources=True)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@logger.trace(log_resources=True)
def complex_operation(x):
    fact_result = fact(x)
    fib_result = fibonacci(x)
    return fact_result + fib_result


if __name__ == "__main__":
    while True:
        x = int(input("Enter a number: "))
        result = complex_operation(x)

        print(f"Result of complex operation with {x}: {result}")
