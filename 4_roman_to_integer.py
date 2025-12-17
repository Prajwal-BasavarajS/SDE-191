def rom_to_int(word):
    n = len(word)

    d = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    summ = 0
    i = 0

    while i < n:
        # Subtractive case
        if i < n - 1 and d[word[i]] < d[word[i + 1]]:
            summ += d[word[i + 1]] - d[word[i]]
            i += 2
        else:
            summ += d[word[i]]
            i += 1

    return summ


word = 'MCMLIV'
print(rom_to_int(word))
