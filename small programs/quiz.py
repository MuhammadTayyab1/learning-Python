user=str(input("Enter = "))
# input    3413289830 a-bcdefghij
arr1=[]
arr2=[]
op=""
ind=0

hold= user.split(" ")
number=hold[0]
alpha=hold[1]

for i in range(len(number)):
    arr1.append(number[i])

for j in range(len(alpha)):
    if alpha[j]=="-":
        op="-"
        ind=j
    elif alpha[j]=="+":
        op="+"
        ind=j
    else:
        arr2.append(alpha[j])
        

s1=""
s2=""
res=""

for k in range(len(arr1)):
    if k<=ind:
        s1+=arr1[k]
    elif k>ind:
        s2+=arr1[k]
if op=="+":
    res=int(s1)+int(s2)
elif op=="-":
    res=int(s1)-int(s2)

print(res)
        
   


    
    