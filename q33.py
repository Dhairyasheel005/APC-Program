input_string = "swiss"
char_count = {}
for ch in input_string:
    char_count[ch] = char_count.get(ch, 0) + 1
first_unique = None
for ch in input_string:
    if char_count[ch] == 1:
        first_unique = ch
        break
print(first_unique)
