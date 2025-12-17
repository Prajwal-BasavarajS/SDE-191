import array as arr 

arr1 = arr.array('i',[1,2,3,4])

arr1.append(5)

print(arr1)


arr1.pop(2)

print(arr1)

del arr1[2]
print(arr1)


arr1.remove(1)

print(arr1)



arr1.append(8) 

print(arr1)


arr1[2] = 9

print(arr1)


if 2 in arr1:
    print("true")