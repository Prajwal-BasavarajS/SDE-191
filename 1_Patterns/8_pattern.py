n = 5 

for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range (0,n*2-(i*2)-1):
        print("1",end="")
    for j in range(0,i):
        print(" ",end="")
    print()
