print("Temperature Conversion Program")
print("Enter temperature and its unit (C/F/K)")

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F/K): ").upper()

if unit == 'C':
    f = (temp * 9/5) + 32
    k = temp + 273.15
    print(f"Celsius: {temp}")
    print(f"Fahrenheit: {f}")
    print(f"Kelvin: {k}")

elif unit == 'F':
    c = (temp - 32) * 5/9
    k = c + 273.15
    print(f"Fahrenheit: {temp}")
    print(f"Celsius: {c}")
    print(f"Kelvin: {k}")

elif unit == 'K':
    c = temp - 273.15
    f = (c * 9/5) + 32
    print(f"Kelvin: {temp}")
    print(f"Celsius: {c}")
    print(f"Fahrenheit: {f}")

else:
    print("Invalid unit")