name=input("enter your name")
value=int(input("hello "+name+"\nEnter your anount"))

a=int(0)

if value>=100000:
    a= value * 0.20
    print("Your tax payable is = ",a)
    
elif value>=70000 and value<=90000:
    a= value * 0.15
    print("Your tax payable is = ",a)

elif value<70000 and value>=40000:
    a= value * 0.08
    print("Your tax payable is = ",a)
    
else:
    a= value * 0.02
    print("Your tax payable is = ",a)
   