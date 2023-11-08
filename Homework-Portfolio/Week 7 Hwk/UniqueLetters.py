word = input("Enter a word: ")
unique = [""]

for character in word:
    if character not in unique:
        unique.append(character)

print(unique)