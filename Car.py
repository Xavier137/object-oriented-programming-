class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def get_description(self):
        return f"{self.year} {self.color} {self.make} {self.model} with {self.mileage} miles."

    def drive(self, miles):
        self.mileage += miles
        return f"You drove {miles} miles. The new mileage is {self.mileage} miles."

# Create a Car instance
car = Car("Ford", "BMW", 2022, "Grey", 30000)

# Print the car description
print(car.get_description())

# Drive the car and print the updated description
print(car.drive(100))
print(car.get_description())