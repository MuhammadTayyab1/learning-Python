LA=[2,5,7,8,9]

k=3
n=5

j=k

print("Given")
print(LA)

while j<n:
    LA[j-1]=LA[j]
    j=j+1
    n=n-1

print("Output")
print(LA)


