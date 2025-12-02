
def fun_up(n):
    space = 0
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end = " ")
        for s in range (0, space):
            print(" ",end =" ")
        for j in range(0,n-i):
            print("*",end=" ")
        space = space + 2
        print()

def fun_down(n):
    space = (n-1) * 2 
    for i in range(1,n+1):
        for j in range(0,i):
            print("*",end=" ")
        for s in range(0,space):
            print(" ",end =" ")
        for j in range(0,i):
            print("*",end=" ")
        space = space - 2
        print()

fun_up(5)
fun_down(5)





