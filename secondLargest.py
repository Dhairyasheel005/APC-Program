numbers = [15, 40, 80, 25, 60]

largest = second = -999999

for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)