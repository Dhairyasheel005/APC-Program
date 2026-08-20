input_string2 = "swiss"
char_count2 = {}
first_repeating = None
for ch in input_string2:
    if ch in char_count2:
        first_repeating = ch
        break
    char_count2[ch] = 1
print(first_repeating)
