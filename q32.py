num_list = [2, 7, 11, 15, 4]
target = 9
seen_numbers = {}
result_pair = None
for num in num_list:
    complement = target - num
    if complement in seen_numbers:
        result_pair = (complement, num)
        break
    seen_numbers[num] = True
print(result_pair)
