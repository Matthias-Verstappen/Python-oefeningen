#oefening 1

def celsius_to_farenheit(degrees_celsius):
    return (degrees_celsius * (9/5) + 32)


degrees_celsius1 = float(input("Degrees Celsius: "))
degrees_farenheit = celsius_to_farenheit(degrees_celsius1)


print(f"{degrees_celsius1} degrees Celsius = {degrees_farenheit} degrees Farenheit.")