num=int(input("Enter value = "))

a=0
b=1

fbs_array=[]
prime_array=[]

# Add input number at begnning 
fbs_array.append(num)
fbs_array.append(a)
fbs_array.append(b)

# Generate Sequence 
for i in range(num-1):
    sum=a+b
    a=b
    b=sum
    if sum<=num:
        fbs_array.append(sum)


print("fbs_array =  ",fbs_array)

# Search prime numbers from fbs_array and copy into prime_array
for j in range(len(fbs_array)):
    flag=False
    for k in range(2,fbs_array[j]):
        if fbs_array[j] % k==0:
            flag= True
            break
        else:
            continue

    if flag==False:
        if fbs_array[j]==0 or fbs_array[j]==1:
            pass
        else:
            prime_array.append(fbs_array[j])


# Delete prime values from fbs_array
for q in range(len(prime_array)):
        hold=prime_array[q]

        for w in range(len(fbs_array)):
            if hold==fbs_array[w]:

                for e in range(w,len(fbs_array)-1,1):
                    fbs_array[e]=fbs_array[e+1]

                
print("prime_array = ",prime_array)

# Remove garbage value
le=int(len(fbs_array)-len(prime_array))
fbs_array=fbs_array[:le]
print("\nfbs_array after removing prime numbers")
print("fbs_array =  ",fbs_array)



        
      
