marks = [70,85,90,45,60,78,88,95,67,72,80,55,40,98,91,65,77,83,58,69]

print("Highest:", max(marks))
print("Lowest:", min(marks))

avg = sum(marks)/len(marks)
print("Average:", avg)

above = 0
below = 0

for i in marks:
    if i > avg:
        above += 1
    elif i < avg:
        below += 1

print("Above average:", above)
print("Below average:", below)