

var= open(r'C:\Users\Tayyab\Desktop\file.txt','r')
a=var.readlines()
print(a)
arr=[]
for i in a:
    arr.append([int(j) for j in i.split(' ')   ] )

print(arr)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print("")
