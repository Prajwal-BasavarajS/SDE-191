n=10
for i in range (0,n):
    if i==0 or i == n-1 :
        for j in range(0,n):
            print("*",end=" ")
    else:
        for j in range(0,1):
            print("*", end=" ")
        for s in range(0,n-2):
            print(" ",end=" ")
        for j in range(0,1):
            print("*",end=" ")
    print()
print("new")
n = 10
for i in range(0,n):
    for j in range(0,n):
        if (i ==0 or i == n-1 or j == 0 or j == n-1):
            print("*", end=" ")
        else :
            print(" ",end=" ")
    print()
