from array import array

arr = array('i', [10, 20, 30, 40, 50])

print("Original array:", arr)

print("First element:", arr[0])

arr[1] = 100
print("After update:", arr)

arr.append(60)
print("After append:", arr)

arr.extend([70, 80])
print("After extend:", arr)

arr.insert(2, 25)
print("After insert:", arr)

arr.remove(30)
print("After remove:", arr)

arr.pop()
print("After pop:", arr)

print("Index of 40:", arr.index(40))
print("Count of 20:", arr.count(20))
print("Length:", len(arr))

arr.reverse()
print("After reverse:", arr)

print("Type code:", arr.typecode)

print("Array elements:")
for x in arr:
    print(x)

print("As list:", arr.tolist())