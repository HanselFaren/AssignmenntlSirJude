f = int(input("Enter a temperature in Fahrenheit: "))
print(f"\nThe temperature in Fahrenheit is: {f}")
def convert_temp():
    c = (5 / 9) * (f - 32)
    def convert_to_celcius():
        print(f"The temperature in Celcius is: {c}")
    convert_to_celcius()
    def convert_to_kelvin():
        k = c + 273.15
        print(f"The temperature in Kelvin is: {k}")
    convert_to_kelvin()

convert_temp()