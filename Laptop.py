class Laptop:
    def __init__(self, brand, model, year, processor, ram, storage):
        self.brand = brand
        self.model = model
        self.year = year
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def get_specs(self):
        specs = f"{self.year} {self.brand} {self.model} with {self.processor} processor, {self.ram} RAM, and {self.storage} storage."
        print(specs)
        return specs

    def upgrade_ram(self, additional_ram):
        self.ram += additional_ram
        print(f"RAM upgraded to {self.ram}.")
        return f"RAM upgraded to {self.ram}."


# Create an instance of the Laptop class
my_laptop = Laptop("HP", "16-k0370TX", 2022, "Intel Core i7", 16, "2TB SSD")

# Use the methods of the Laptop class
print("Laptop Specs:")
print(my_laptop.get_specs())
print("Upgrading RAM...")
print(my_laptop.upgrade_ram(8))
print("Updated Laptop Specs:")
print(my_laptop.get_specs())