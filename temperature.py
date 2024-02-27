class Temperature:
    '''This is a Temperature class.'''

    def __init__(self, temperature=0.0, unit="celsius"):
        self.temperature = temperature
        self.unit = unit

    def convert_fahrenheit_to_celsius(self):
        if self.unit == "fahrenheit":
            self.temperature = (self.temperature - 32) * 5/9
            self.unit = "celsius"
        else:
            print("The temperature is already in Celsius.")

    def convert_celsius_to_fahrenheit(self):
        if self.unit == "celsius":
            self.temperature = self.temperature * 9/5 + 32
            self.unit = "fahrenheit"
        else:
            print("The temperature is already in Fahrenheit.")

# Example usage:
temperature_obj = Temperature(100.0, "fahrenheit")
print(f"Initial temperature: {temperature_obj.temperature} {temperature_obj.unit}")

temperature_obj.convert_fahrenheit_to_celsius()
print(f"Temperature after conversion: {temperature_obj.temperature} {temperature_obj.unit}")

temperature_obj.convert_celsius_to_fahrenheit()
print(f"Temperature after conversion: {temperature_obj.temperature} {temperature_obj.unit}")