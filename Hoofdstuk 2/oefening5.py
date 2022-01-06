#oefening 5
number = int(input("Enter a number: "))
final_digit = int(input("Final digit you want to test with: "))
last_digit_number = number % 10
if number < 0:
    print("Negative numbers will not be tested.")
elif final_digit == last_digit_number:
    print(number, "ends with", final_digit)
else:
    print(number, "does not end with", final_digit)