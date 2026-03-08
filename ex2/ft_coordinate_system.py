import sys
import math


def parsing_formula(arguments: list[str]) -> None:
    origin: tuple[int, int, int] = (0, 0, 0)
    default_position: tuple[int, int, int] = (10, 20, 5)
    distance = math.sqrt((default_position[0] -
                          origin[0]) ** 2 +
                         (default_position[1] -
                          origin[1]) ** 2 +
                         (default_position[2] -
                          origin[2]) ** 2)
    if len(arguments) == 1:
        print(f"Position created: {default_position}")
        print(f"Distance between {origin} and {default_position}:"
              f"{distance:.2f}")
    else:
        print(f"Parsing coordinates: {arguments[1]}")
        split_string = arguments[1].split(",")
        temp_list: list[int] = []
        for i in split_string:
            try:
                num = int(i)
                temp_list.append(num)
            except ValueError as e:
                print(f"Error parsing coordinates: {e}")
                print(f"Error details - Type: ValueError, Args: ({e},)")
                print()
                return

        new_tuple = tuple(temp_list)
        distance = math.sqrt((new_tuple[0] -
                              origin[0]) ** 2 +
                             (new_tuple[1] -
                              origin[1]) ** 2 +
                             (new_tuple[2] -
                              origin[2]) ** 2)
        print(f"Parsed position: {new_tuple}")
        print(f"Distance between {origin} and {new_tuple}: {distance}")
        print()
        print("Unpacking demonstration:")
        print(f"Player at x={new_tuple[0]}, y={new_tuple[1]},"
              f"z={new_tuple[2]}")
        print(f"Coordinates: X={new_tuple[0]}, Y={new_tuple[1]},"
              f"Z={new_tuple[2]}")


def test_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()
    parsing_formula(sys.argv)


if __name__ == "__main__":
    test_coordinate_system()
