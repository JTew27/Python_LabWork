word1 = input("Enter a word: ")
word2 = input("Enter another word: ")



def appear(word1,word2):
    unique = [" "]
    for character in word1:
        if character not in unique:
            unique.append(character)

    for character in word2:
        if character not in unique:
            unique.append(character)
    print ("The following letters appear:",unique)

def appearBoth(word1, word2):
    set1 = set(word1)
    set2 = set(word2)

    both = set1.intersection(set2)

    if len(both) > 0:
        print ("The following letters appear in both words:", both)


def appearOnce(word1,word2):
    set1 = set(word1)
    set2 = set(word2)

    appearsOnce = set1.symmetric_difference(set2)

    if len(appearsOnce) > 1:
        print ("These letters appear once",appearsOnce)


appear(word1,word2)
appearBoth(word1,word2,)
appearOnce(word1,word2)