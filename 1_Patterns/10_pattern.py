n = 5
for i in range(0,n*2):
    star = i
    if (i>n): 
        star = 2*n-i
    for j in range(0,star):
        print("*",end = " ")
    
    print()