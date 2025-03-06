fahreinhet= float(input("Enter temperature in Fahrenheit: "))
fahrenheit_to_celsius = lambda fahrenheit: (fahrenheit - 32) * 0.5556
celsius = fahrenheit_to_celsius(fahreinhet)
celsius = round(celsius)

print("Temperature in Celsius: " , celsius)
