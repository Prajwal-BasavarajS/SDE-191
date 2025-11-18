n = 5
space = 2*(n-1)
for i in range (1,n+1):
    # number
    for j in range(1,i+1):
        print(j,end="")
    #space 
    for j in range(0,space):
        print(" ",end="")
    # number 
    for j in range(i,0,-1):
        print(j,end ="")
    print()
    space-=2


def pattern_13(n):
    space = 2*(n-1)
    for i in range (1,n+1):
        for j in range (1,i+1):
            print(j,end="")
        for j in range(0,space):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end ="")
        space -= 2
        print()



pattern_13(5)