#oefening 8.1

current_hour = int(input('Enter the current hour: '))
wait_time = int(input('How long do you want to wait: '))

if current_hour + wait_time > 24:
    alarm = (current_hour + wait_time) % 24
else:
    alarm = current_hour + wait_time
print(f'The alarm will sound at {alarm}h.')
