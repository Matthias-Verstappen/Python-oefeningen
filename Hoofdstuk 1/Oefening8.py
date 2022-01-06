#oefening8
time = float(input("Enter the current hour: "))
wait_time = int(input("Enter how long you want to wait: "))
end_hour = time + wait_time
alarm_time = end_hour % 24
print('The alarm will sound at '+ str(alarm_time)+'h')