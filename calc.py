class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        print(f"{num1} + {num2} = {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        print(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        print(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            print("Error: Division by zero is not allowed")
            return "Error: Division by zero is not allowed"
        result = num1 / num2
        self.history.append(f"{num1} / {num2} = {result}")
        print(f"{num1} / {num2} = {result}")
        return result

    def get_history(self):
        print("Calculation History:")
        print("\n".join(self.history))


# Create an instance of the Calculator class
my_calculator = Calculator()

# Use the methods of the Calculator class
print("Results:")
my_calculator.add(5, 3)
my_calculator.subtract(10, 4)
my_calculator.multiply(7, 2)
my_calculator.divide(12, 3)

# Display the calculation history
my_calculator.get_history()