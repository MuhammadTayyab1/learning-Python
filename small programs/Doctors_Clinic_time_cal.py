cs=int(input("Enter : "))

for i in range(cs):
    data=input("Enter number of patient and time seperated by space").split()
    total= (10 - int(data[1]))*(int(data[0])-1)
    print(total)
