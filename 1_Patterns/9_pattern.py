

def pat_7(n):
    for i in range(0,n):
        # space
        for j in range(0,n-i-1):
            print(" ",end="")
        # star
        for j in range(0,i*2+1):
            print("1",end="")
        # space
        for j in range(0,n-i-1):
            print(" ",end = "")
        print()

def pat_8(n):
    for i in range(0,n):
        for j in range(0,i):
            print(" ",end="")
        for j in range (0,n*2-(i*2)-1):
            print("1",end="")
        for j in range(0,i):
            print(" ",end="")
        print()

pat_7(5)
(pat_8(5))
