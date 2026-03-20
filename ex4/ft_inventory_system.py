import sys


def test_inventory_system(arguments: list[str]) -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in arguments[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key, value = parts
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")

    if not inventory:
        print("No items provided. Usage: python3 ft_inventory_system.py"
              " <item>:<qty> ...")
        return

    total: int = sum(inventory.values())
    count: int = len(inventory.keys())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {count} items: {total}")
    for key, qty in inventory.items():
        percent = round((qty / total) * 100, 1)
        print(f"Item {key} represents {percent}%")

    most_abundant: str = list(inventory.keys())[0]
    least_abundant: str = list(inventory.keys())[0]
    for item in inventory:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant}"
          f" with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant}"
          f" with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    test_inventory_system(sys.argv)
