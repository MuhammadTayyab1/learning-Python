num=input("Enter a number = ")

arr=[]
sum=0
flag=False

for i in range(len(num)):
    arr.append(int(num[i]))
    sum += arr[i]


for j in range(len(arr)):
    if sum % arr[i]==0:
        flag=True
    else:
        flag=False


print(flag)