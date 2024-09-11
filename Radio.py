class Radio:
    def __init__(self, brand, model, year, frequency_range):
        self.brand = brand
        self.model = model
        self.year = year
        self.frequency_range = frequency_range
        self.is_on = False
        self.current_station = None

    def turn_on(self):
        self.is_on = True
        print("Radio turned on.")
        return "Radio turned on."

    def turn_off(self):
        self.is_on = False
        print("Radio turned off.")
        return "Radio turned off."

    def tune_in(self, station):
        if self.is_on:
            self.current_station = station
            print(f"Tuned in to {station}.")
            return f"Tuned in to {station}."
        else:
            print("Radio is off. Please turn it on first.")
            return "Radio is off. Please turn it on first."


# Create an instance of the Radio class
my_radio = Radio("premier", "FM-MW-SW", 2024, "FM 81-109 MHz")

# Use the methods of the Radio class
print("Radio Status:")
print(my_radio.turn_on())
print(my_radio.tune_in("98.4 FM"))
print(my_radio.tune_in("91.3 FM"))
print(my_radio.turn_off())
print(my_radio.tune_in("93.3 FM"))