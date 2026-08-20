paragraph = input("Enter a paragraph: ")
para_words = paragraph.split()
length_freq = {}
for word in para_words:
    length_freq[len(word)] = length_freq.get(len(word), 0) + 1
print(length_freq)
