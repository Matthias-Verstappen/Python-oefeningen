#oefening 2.1

current_dollar_rate = float(input('Current dollar rate (€ -> $): '))
euro = float(input('Your amount in Euro: '))

def euro_to_dollar(euro, exchange_rate):
    return euro * exchange_rate

print(f'€ {euro} = $ {euro_to_dollar(euro, current_dollar_rate)}')