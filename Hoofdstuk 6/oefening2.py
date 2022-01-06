#oefening2

def euro_to_dollar(euros, exchange_rate):
    return euros * exchange_rate

dollar_rate = float(input("Current dollar rate (€ -> $): "))
euro_amount = float(input("Your amount in euro: "))
converted_euros = euro_to_dollar(euro_amount, dollar_rate)

print(f'€ {euro_amount} = $ {converted_euros}')