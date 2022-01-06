# oefening 7

initial_limit = int(input("Enter an initial limit: "))
final_limit = int(input("Enter a final limit: "))

if final_limit < initial_limit:
    print("The initial limit must be smaller than the final limit!")
elif initial_limit == final_limit:
    print("Sum of the numbers from", initial_limit, "to", final_limit, "\n", initial_limit)
else:
    sum_numbers = initial_limit
    for i in range(initial_limit + 1, final_limit + 1):
        sum_numbers += i
        print(f"+ {i} --> {sum_numbers}")

