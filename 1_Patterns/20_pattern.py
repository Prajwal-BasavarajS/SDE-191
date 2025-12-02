def fun_up(n):
    space = n*2
    for i in range(1,n+2):
        for j in range(0,i):
            print("*",end = " ")
        for j in range(0,space):
            print(" ",end =' ')
        for j in range(0,i):
            print("*",end=" ")
        space -=2 
        print()
def fun_down(n):
    e = n+2
    space = 0
    for i in range(1,e):
        for j in range(0,e-i):
            print("*",end=" ")
        for j in range(0,space):
            print(" ",end=" ")
        for j in range(0,e-i):
            print("*",end = " ")
        space+=2
        print()



fun_up(5)
fun_down(5)