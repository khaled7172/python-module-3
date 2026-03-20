import sys


def argument_info(arguments: list[str]) -> None:
    length = len(arguments)
    print(f"Program name: {arguments[0]}")
    if length == 1:
        print("No arguments provided!")
    if length > 1:
        print(f"Arguments received: {length - 1}")
    for arg in range(1, len(arguments)):
        print(f"Argument {arg}: {arguments[arg]}")
    print(f"Total arguments: {len(arguments)}")


def test_command_line() -> None:
    print("=== Command Quest ===")
    argument_info(sys.argv)


if __name__ == "__main__":
    test_command_line()
