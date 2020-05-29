file_contents = open("sample.txt", "r")

word_frequency= {}

for line in file_contents:
    for each in line.split():
        if each.lower() in word_frequency:
            word_frequency[each.lower()]+=1
        else:
            word_frequency[each.lower()] = 1
print(word_frequency)


