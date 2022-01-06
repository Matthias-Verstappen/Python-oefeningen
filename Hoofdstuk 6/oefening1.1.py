# oefening 1.1

celsius = float(input('Degrees Celsius: '))


def celsius_to_farenheit(celsius):
    return celsius * (9 / 5) + 32

print(f'{celsius} degrees Celsius = {celsius_to_farenheit(celsius)} degrees Farenheit')