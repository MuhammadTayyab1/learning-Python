# string array
cars = ["Ford", "Volvo", "BMW"]

for x in range(3):
    print(cars[x])



# Or 
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)



# Adding, removing in arrays
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")

for y in cars:
    print(y)

print("============================")

cars.remove("Ford")
for y in cars:
    print(y)

