
# Tuple 
tuple =(1,2,3,'x','y','z')

for i in range(len(tuple)):
    print(tuple[i])



# Joining 2 tuple
tuple1=(1,2,3,4)
tuple2=("q","w","e","r")

tuple3= tuple1+tuple2
print(tuple3)



# Range of index
cars = ("Ford", "Volvo", "BMW","Datsun","Cadillac","Nissan","Audi")
print(cars[2:5])



# Search in tuple
a = ("Ford", "Volvo", "BMW")

if "BMW" in a:
    print("Yes BMW is in a")
else:
    print("Not found")