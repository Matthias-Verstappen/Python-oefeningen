#oefening 11
weight = float(input("What is your weight? "))
length = float(input("What is your length in centimeters? "))
bmi = (weight / (length * length)) * 10000

if bmi < 18:
    print("underweight")
elif 18 <= bmi < 25:
    print("normal weight")
elif 25 <= bmi < 27:
    print("slightly overweight")
elif 27 <= bmi < 30:
    print('moderate overweight')
elif 30 <= bmi < 40:
    print('obese')
else:
    print("sickly obese")