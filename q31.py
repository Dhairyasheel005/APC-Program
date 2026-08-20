word_list = ["cat", "dog", "lion", "goat", "ant", "tiger"]
length_groups = {}
for word in word_list:
    length_groups.setdefault(len(word), []).append(word)
print(length_groups)
