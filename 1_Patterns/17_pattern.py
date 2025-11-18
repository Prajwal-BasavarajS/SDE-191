n = 4
for i in range(n):
    
    # spaces
    for s in range(n - i - 1):
        print(" ", end="")

    # increasing letters
    for j in range(i + 1):
        print(chr(65 + j), end="")

    # decreasing letters
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    
    print()
