def megrestrings(word1,word2):
    a = len(word1) 
    b = len(word2)

    i = 0               # moving elements through strings
    j = 0

    s = []
    
    word = 1

    while i < a and  j < b :
        if word == 1 :
            s.append(word1[i])
            i += 1
            word = 2
        else : 
            s.append(word2[j])
            j += 1
            word = 1

    while i < a :
        s.append(word1[i])
        i += 1

    while j < b :
        s.append(word2[j])
        j += 1
    

    return "".join(s)


word1 = "abc"
word2 = "pqrst"
print(word1)
print(word2)
print("merged = ",end = " ")
print(megrestrings(word1,word2))



from itertools import zip_longest

def merge_strings_pythonic(word1, word2):
    # zip_longest fills missing values with empty string
    return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))

# Test
word1 = "abc"
word2 = "pqrst"

print("word1:", word1)
print("word2:", word2)
print("merged =", merge_strings_pythonic(word1, word2))
