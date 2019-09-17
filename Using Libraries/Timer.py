import time
import os

count=0

def check(aa,j,a,b,c,d,e,f,g,h,i):
    if aa=="0":
        print(j)
    elif aa=="1":
        print(a)
    elif aa=="2":
        print(b)
    elif aa=="3":
        print(c)
    elif aa=="4":
        print(d)
    elif aa=="5":
        print(e)
    elif aa=="6":
        print(f)
    elif aa=="7":
        print(g)
    elif aa=="8":
        print(h)
    elif aa=="9":
        print(i)
    

a ="     |\n"
a+="     |\n"
a+="     |\n"
a+="     |\n"
a+="     |\n"

b =" ____\n"
b+="     |\n"
b+=" ____|\n"
b+="|    \n"
b+="|____\n"

c =" ____\n"
c+="     |\n"
c+=" ____|\n"
c+="     |\n"
c+=" ____|\n"


d ="|    |\n"
d+="|    |\n"
d+="|____|\n"
d+="     |\n"
d+="     |\n"

e =" ____\n"
e+="|     \n"
e+="|____\n"
e+="     |\n"
e+="_____|\n"

f =" ____\n"
f+="|     \n"
f+="|____\n"
f+="|    |\n"
f+="|____|\n"

g ="_____\n"
g+="     |\n"
g+="     |\n"
g+="     |\n"
g+="     |\n"

h =" ____\n"
h+="|    |\n"
h+="|____|\n"
h+="|    |\n"
h+="|____|\n"

i =" ____\n"
i+="|    |\n"
i+="|____|\n"
i+="     |\n"
i+="     |\n"


j =" ____\n"
j+="|    |\n"
j+="|    |\n"
j+="|    |\n"
j+="|____|\n"


min= int(input("Enter total time in minutes =  "))
seconds=min*60

for k in range(seconds):
    
    # 1 second timer
    time.sleep(1)
    os.system('cls')

    count+=1

    #Counvert into string in order to break in list
    aa=str(count)

    # If 1 digit number
    if count<10:
        check(aa,j,a,b,c,d,e,f,g,h,i)
    else:
        # else two or more digits
        arr=[]
        for i in range(len(aa)):
            arr.append(aa[i])
        
        hold=len(arr)
        if hold==2:
            var1=arr[0]
            var2=arr[1]
            check(var1,j,a,b,c,d,e,f,g,h,i)
            check(var2,j,a,b,c,d,e,f,g,h,i)
        elif hold==3:
            var1=arr[0]
            var2=arr[1]
            var3=arr[2]

            check(var1,j,a,b,c,d,e,f,g,h,i)
            check(var2,j,a,b,c,d,e,f,g,h,i)
            check(var3,j,a,b,c,d,e,f,g,h,i)
        elif hold==4:
            var1=arr[0]
            var2=arr[1]
            var3=arr[2]
            var4=arr[3]

            check(var1,j,a,b,c,d,e,f,g,h,i)
            check(var2,j,a,b,c,d,e,f,g,h,i)
            check(var3,j,a,b,c,d,e,f,g,h,i)
            check(var4,j,a,b,c,d,e,f,g,h,i)

        elif hold==5:
            var1=arr[0]
            var2=arr[1]
            var3=arr[2]
            var4=arr[3]
            var5=arr[4]

            check(var1,j,a,b,c,d,e,f,g,h,i)
            check(var2,j,a,b,c,d,e,f,g,h,i)
            check(var3,j,a,b,c,d,e,f,g,h,i)
            check(var4,j,a,b,c,d,e,f,g,h,i)
            check(var5,j,a,b,c,d,e,f,g,h,i)


input()