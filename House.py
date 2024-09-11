class House:
    def __init__(self, address, num_bedrooms, num_bathrooms, square_footage):
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.square_footage = square_footage

    def get_details(self):
        return f"House at {self.address} with {self.num_bedrooms} bedrooms, {self.num_bathrooms} bathrooms, and {self.square_footage} square feet."

    def add_bedroom(self):
        self.num_bedrooms += 1
        return f"Added a bedroom. The new total is {self.num_bedrooms} bedrooms."

# Create a House instance
house = House("123 Main St", 3, 2, 1500)

# Print the house details
print(house.get_details())

# Add a bedroom and print the updated details
print(house.add_bedroom())
print(house.get_details())