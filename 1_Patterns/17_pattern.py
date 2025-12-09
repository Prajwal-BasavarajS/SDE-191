n = 5
for i in range(n):
    
    # spaces
    for s in range(n - i - 1):
        print(" ", end=" ")

    # increasing letters
    for j in range(i + 1):
        print(chr(65 + j), end=" ")

    # decreasing letters
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end=" ")
    
    print()


a = 5

for i in range(0,a):
    for j in range(0,n-i-1):
        print(" ",end=" ")

    for j in range(i+1):
        print(chr(65+j),end=" ")
    
    for j in range(i-1,-1,-1):
        print(chr(65+j),end = " ")
    
    print()



















# n=5

# for i in range(0,5):
#     for j in range (0,n):
#         print("*",end=" " )
#     n=n-1   
#     print()

# a=65
# n=5
# for i in range (0,5):
#     for j in range (0,n):
#         print(chr(a+j),end="")
#     n=n-1
#     print()

# print("je")

# a = 65

# for i in range(0,5):
#     for j in range(0,i+1):
#         print(chr(a+i),end="")
#     print()
