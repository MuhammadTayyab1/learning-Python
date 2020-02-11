# take input of processes from user
pro = int(input('Enter your number of processes: '))

# take input of resouces from user
res = int(input('Enter Your number of resources: '))

# initilize varibale for claimmatrix and array allocation
array = []
claimmatrix = []

for i in range(pro):
    temp = []
    claim = []

    # Input from user of Allocation matrix
    for j in range(res):
        temp.append(int(input('Enter data allocation matrix : ')))
    array.append(temp)
    
    # Input from user of claim matrix
    for j in range(res):
        claim.append(int(input('Enter data claim matrix : ')))
    claimmatrix.append(claim)

needmatrix = []
for i in range(pro):
    temp = []
    for j in range(res):
        temp.append(claimmatrix[i][j]-array[i][j])
    needmatrix.append(temp)

# Print according sequence
print(claimmatrix)
print(needmatrix)
print(array)


resources = []
for i in range(res):
    resources.append(int(input(f'Enter total resource for {i+1}:')))
print(resources)

r_vector = []
for i in range(res):
    temp = 0
    for j in range(pro):
        temp += array[j][i]
    r_vector.append(resources[i]-temp)
print(r_vector)

# Checking condition with available

my_array = ['False' for i in range(pro)]
while True:
    if 'False' in my_array:
        for i in range(pro):
            if my_array[i] == 'False':
                if r_vector >= needmatrix[i]:
                    print(f'Process {i+1}')
                    for j in range(res):
                        r_vector[j] += array[i][j]
                    print(f'Available matrix: {r_vector}')
                    my_array[i] = 'True'
        continue
    else:
        break