import sys


def test_inventory_system(arguments: list[str]) -> None:
    print("=== Inventory System Analysis ===")
    unique_items = len(arguments) - 1
    inventory: dict[str, int] = {}
    if unique_items == 0:
        print("Empty inventory")
        return
    else:
        for arg in arguments[1:]:
            key, value = arg.split(":")
            inventory[key] = int(value)
    total_items = sum(inventory.values())
    unique_types = len(inventory.keys())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")
    print()
    print("=== Current Inventory ===")
    for key, value in inventory.items():
        percent = (value / total_items) * 100
        if value > 1:
            print(f"{key}: {value} units ({percent:.1f}%)")
        else:
            print(f"{key}: {value} unit ({percent:.1f}%)")
    most_abundant: str | None = None
    least_abundant: str | None = None
    for item in inventory:
        qty = inventory.get(item)
        if most_abundant is None or qty > inventory.get(most_abundant):
            most_abundant = item
        if least_abundant is None or qty < inventory.get(least_abundant):
            least_abundant = item
    print()
    print("=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} ({inventory.get(most_abundant)}"
          "units)")
    print(f"Least abundant: {least_abundant} ({inventory.get(least_abundant)}"
          "units)")
    print()
    print("=== Item Categories ===")
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}
    restock: list[str] = []
    restock_str = ""
    for key, value in inventory.items():
        if value >= 5:
            moderate[key] = value
        elif value <= 1:
            restock.append(key)
            scarce[key] = value
        else:
            scarce[key] = value
    for i, item in enumerate(restock):
        if i != 0:
            restock_str += ", "
        restock_str += item

    keys_str = ""
    for i, key in enumerate(inventory.keys()):
        if i != 0:
            keys_str += ", "
        keys_str += key
    values_str = ""
    for i, value in enumerate(inventory.values()):
        if i != 0:
            values_str += ", "
        values_str += str(value)
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print()
    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock_str}")
    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {values_str}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    test_inventory_system(sys.argv)
