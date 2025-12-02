n = 5 
for i in range (0,n+1):
    for s in range(0,n-i):
        print(" ",end = " ")
    for j in range(0,i):
        print("*" ,end =" ")
    print()

n=5
print("new")
for i in range(0,n+1):
    for s in range(0,i):
        print(" ",end =" ")
    for j in range(0,n-i):
        print("*",end= " ")
  
    print()



# n = 5
# space = 0
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("*",end = " ")
#     for s in range (0, space):
#         print(" ",end =" ")
#     for j in range(0,n-i):
#         print("*",end=" ")
    
#     space = space + 2
#     print()