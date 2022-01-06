#oefening 9

names = []
distances = []
name = ""
distance = 0
count = 0

print("Enter your name and distance to school.")
print("Type stop when you want to close the entry.")

while name != "stop":
    name = input("Enter your name: ")
    distance = float(input("Distance to school: "))
    if name != "stop" and distance != "stop":
        names.append(name)
        distances.append(distance)
        count += 1



print("Overview")

i = 0
while i < len(names) - 1:
    print(names[i], distances[i], end="     ")

