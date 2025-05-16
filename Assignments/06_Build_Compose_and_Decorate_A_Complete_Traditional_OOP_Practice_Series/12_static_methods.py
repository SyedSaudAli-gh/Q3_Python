class TemperatureConverter:
   
    @staticmethod
    def celsius_to_fahrenheit(c):
        f = (c * 9/5) + 32
        print("\n\tTemperature Converter\n")
        print(f"\tCelsius To Fahrenheit {f}")
        
TemperatureConverter.celsius_to_fahrenheit(34)