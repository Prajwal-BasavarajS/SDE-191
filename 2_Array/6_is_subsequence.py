def iSubsequence(word1,word2):
    s = len(word1)
    t = len(word2)

    if word1 == "":
        return True
    
    if s > t :
        return False
    
    j = 0

    for i in range(t):
        if word2[i] == word1[j]:
            if j == s-1 :
                return True
            j += 1

    return False

test_cases = [
    # Basic cases
    ("abc", "abcde", True),
    ("ace", "abcde", True),
    ("aec", "abcde", False),

    # Exact match
    ("abc", "abc", True),

    # word1 longer than word2
    ("abcd", "abc", False),

    # Empty strings
    ("", "abc", True),
    ("", "", True),
    ("abc", "", False),

    # Single character
    ("a", "a", True),
    ("a", "b", False),

    # Repeated characters
    ("aaa", "aaaaa", True),
    ("aaaa", "aaa", False),

    # Case sensitivity
    ("abc", "akbdacs",True),

    # Non-contiguous subsequence
    ("abc", "a1b2c3", True),

    # Special characters
    ("a$c", "a$b$c", True),
    ("aaa","aaaa",True),

    ("abc","akbdacs",True),
    
    ("aaffd","abbacewffad",True)

]

# for w1, w2, expected in test_cases:
#     result = iSubsequence(w1, w2)
#     print(f"isSubsequence({w1!r}, {w2!r}) = {result} | Expected: {expected}")


for w1,w2, expected in test_cases:
    result = iSubsequence(w1,w2) 
    print(f"isSubsequence ({w1!r} , {w2!r}) = {result} | Expected result = {expected}")

