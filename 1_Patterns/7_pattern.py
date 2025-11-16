n = 5 

for i in range(0,n):
    # space
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i*2+1):
        print("1",end="")
    for j in range(0,n-i-1):
        print(" ",end = "")
    print()




n = 5

for i in range(1, n + 1):            # i = 1 to 5
    # spaces
    for j in range(0, n - i):
        print("*", end="")

    # 1s
    for j in range(0, 2*i - 1):
        print("1", end="")

    # spaces
    for j in range(0, n - i):
        print(" ", end="")

    print()
