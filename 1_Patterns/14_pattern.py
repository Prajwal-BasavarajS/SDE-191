
# for i in range (5,0,-1):
#         print("*"*i)
def pattern_14(n):
    
   
    for i in range(1,n+1):
        for j in range(0,i):
            print(chr(65+j),end="")
    
        print()


    
   

pattern_14(5)
