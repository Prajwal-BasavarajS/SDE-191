n = 5  # number of lines

for i in range(n):
    start = 96 + (n - i)   # ASCII: 97 → 'a'
    for j in range(start, 102):   # 101 → 'e'
        print(chr(j), end=" ")
    print()
