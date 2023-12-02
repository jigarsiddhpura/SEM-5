class InventoryItem:
    def __init__(self, item_id, description, price):
        self.item_id = item_id
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.item_id}: {self.description}, Price: ${self.price:.2f}"


class Electronics(InventoryItem):
    def __init__(self, item_id, description, price, brand, power_consumption):
        super().__init__(item_id, description, price)
        self.brand = brand
        self.power_consumption = power_consumption

    def __str__(self):
        return super().__str__() + f", Brand: {self.brand}, Power Consumption: {self.power_consumption}W"


class Clothing(InventoryItem):
    def __init__(self, item_id, description, price, size, color):
        super().__init__(item_id, description, price)
        self.size = size
        self.color = color

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Color: {self.color}"


class Furniture(InventoryItem):
    def __init__(self, item_id, description, price, material, dimensions):
        super().__init__(item_id, description, price)
        self.material = material
        self.dimensions = dimensions

    def __str__(self):
        return super().__str__() + f", Material: {self.material}, Dimensions: {self.dimensions}"


class StoreInventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item_id):
        for item in self.inventory:
            if item.item_id == item_id:
                self.inventory.remove(item)
                return True
        return False

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory Items:")
            for item in self.inventory:
                print(item)


# Usage example:
store_inventory = StoreInventory()

# Add items to the inventory
tv = Electronics("E001", "Smart TV", 799.99, "Sony", 120)
shirt = Clothing("C001", "Men's Shirt", 29.99, "M", "Blue")
table = Furniture("F001", "Coffee Table", 149.99, "Wood", "40x20x18 inches")

store_inventory.add_item(tv)
store_inventory.add_item(shirt)
store_inventory.add_item(table)

# Display the inventory
store_inventory.display_inventory()

# Remove an item
item_id_to_remove = "C001"
if store_inventory.remove_item(item_id_to_remove):
    print(f"Item {item_id_to_remove} removed.")
else:
    print(f"Item {item_id_to_remove} not found.")

# Display the updated inventory
store_inventory.display_inventory()
