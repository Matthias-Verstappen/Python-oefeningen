#oefening 7.1


low = int(input('Enter initial limit: '))
high = int(input('Enter upper limit: '))
sum = low


if low > high:
    print('The initial limit must be smaller than the upper limit.')
elif low == high:
    print(low)
else:
    print(f'sum of numbers from {low} till {high}')
    while low != high:
        low += 1
        sum += low
        print(f'+ {low} --> {sum}')