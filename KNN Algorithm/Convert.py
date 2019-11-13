import os

def readfile(da):

    num=["" for i in range(25)]
    data=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
    index=0
    with open(r"./"+da+".txt") as f:
        for item in f:
            for i in item:
                num[index]=i
                index+=1
    count=0
    for i in range(5):
        for j in range(5):
            data[i][j]=num[count]
            count+=1
    return data



print("\t\t\t     Welcome new user\n")
print("                   Please read instructions carefully \n\n")
print("        " , chr(26) , " you can only use panel 0 to 14 to draw your alphabet")
print("                           _____________________________")
print("                          " + "|  0  |  1  |  2  |  3  |  4  |")
print("                          |-----|-----|-----|-----|-----|")
print("                          " + "|  5  |  6  |  7  |  8  |  9  |")
print("                          |-----|-----|-----|-----|-----|")
print("                          " + "|  10 |  11 | 12  |  13 |  14 |")
print("                          |-----|-----|-----|-----|-----|")
print("                          " + "|  15 | 16  | 17  |  18 |  19 |")
print("                          |-----|-----|-----|-----|-----|")
print("                          " + "|  20 | 21  | 23  |  24 |  25 |\n")
print("        " , chr(26) , " you only can type star ( * ) or space (  ) to fill these panel")
print("              for example for draw A fill panel like this \n")
print("                           _____________________________")
print("                          " + "|  *  |     |     |     |  *  |")
print("                          |-----|-----|-----|-----|-----|")
print("                          " + "|  *  |  *  |     |     |  *  |")
print("                          |-----|-----|-----|-----|-----|")
print("                          " + "|  *  |     |  *  |     |  *  |")
print("                          |-----|-----|-----|-----|-----|")
print("                          " + "|  *  |     |     |  *  |  *  |")
print("                          |-----|-----|-----|-----|-----|")
print("                          " + "|  *  |     |     |     |  *  |\n")
print("       must confirm before process detection that all panel have")
print("                * and space at the place of 0 to 14")
print("                        Hope you will enjoy\n")
print("\t  " , chr(169) , " Copyright all rights reserved CMT Softwares Solution\n\n")
print("                press enter to continue.....................\n\n")
input("")
os.system('cls')

# input = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
arrymaster = ["","","","","","","","","","","","","","","","","","","","","","","","","",""]

search = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]

mycount = 0
for i in range(5):
    for j in range(5):
        if mycount < 10:
            search[i][j] = "0" + str(mycount)
        else:
            search[i][j] = "" + str(mycount)
        mycount+=1



print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[0][0], search[0][1], search[0][2], search[0][3], search[0][4]))
print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[1][0], search[1][1], search[1][2], search[1][3], search[1][4]))
print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[2][0], search[2][1], search[2][2], search[2][3], search[2][4]))
print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[3][0], search[3][1], search[3][2], search[3][3], search[3][4]))
print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[4][0], search[4][1], search[4][2], search[4][3], search[4][4]))



block = 0
for i in range(5):
    for j in range(5):
        print("ENTER ONLY SPACE OR STAR FOR BLOCK = " , block)
        mydata=input("Enter ")
        search[i][j]=mydata
        os.system('cls')
        #Console.Clear()
        print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[0][0], search[0][1], search[0][2], search[0][3], search[0][4]))
        print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[1][0], search[1][1], search[1][2], search[1][3], search[1][4]))
        print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[2][0], search[2][1], search[2][2], search[2][3], search[2][4]))
        print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[3][0], search[3][1], search[3][2], search[3][3], search[3][4]))
        print("      {0}      {1}      {2}      {3}      {4}\n\n".format(search[4][0], search[4][1], search[4][2], search[4][3], search[4][4]))


        if ((search[i][j] == " *" or search[i][j] == "  ")):
            print("error in above block " , block , "\nrewrite the symbol for block =" , block)
            #print(block)
            search[i][j]=input(" ")
            
        # else:
        #      print("error in above block " , block , "\nrewrite the symbol for block =" , block)

        block+=1
                
    print(" ")
valval=input(" ")

# For A
a = readfile("a")
arrymaster[0] = a


# for b
b = readfile("b")
arrymaster[1] = b


# for c
c = readfile("a")
arrymaster[2] = c


# For D
d = readfile("d")
arrymaster[3] = d


# For E
e = readfile("e")
arrymaster[4] = e


# For F
f = readfile("f")
arrymaster[5] = f


# For G
g = readfile("g")
arrymaster[6] = f


# For H
h = readfile("h")
arrymaster[7] = h


# For I
iv = readfile("i")
arrymaster[8] = iv


# For j
jj = readfile("j")
arrymaster[9] = jj


# For k
k = readfile("k")
arrymaster[10] = k


# For l
l = readfile("l")
arrymaster[11] = l



# For m
m = readfile("m")
arrymaster[12] = m


# For n
n = readfile("n")
arrymaster[13] = n


# For o
o = readfile("o")
arrymaster[14] = o


# For p
p = readfile("p")
arrymaster[15] = p


# For q
q = readfile("q")
arrymaster[16] = q


# For r
r = readfile("r")
arrymaster[17] = r


# For s
s = readfile("s")
arrymaster[18] = s


# For t
t = readfile("t")
arrymaster[19] = t


# For u
u = readfile("u")
arrymaster[20] = u


# For v
v = readfile("v")
arrymaster[21] = v


# For w
w = readfile("w")
arrymaster[22] = w


# For x
x = readfile("x")
arrymaster[23] = x


# For y
y = readfile("y")
arrymaster[24] = y


# For z
z = readfile("z")
arrymaster[25] = z



score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
max = -1000000

for i in range(len(arrymaster)):
    temp=arrymaster[i]

    for j in range(5):
        for k in range(5):
            
            if temp[j][k]==search[j][k]:
                score[i]+=1

os.system('cls')
    
store_of_i = 0
print("\n SYMBOLS GIVEN AS INPUT ARE : \n")

for i in range(5):
    for j in range(5):
        print(search[i][j], end="")
    print("")
print("\n")


for i in range(len(score)):
    if score[i] > max:
        max= score[i]
        store_of_i=i
            
            

#Checking   

if (store_of_i == 0):
    print("CHARATER IS A")
            
elif (store_of_i == 1):
    print("CHARATER IS B")
    
elif (store_of_i == 2):
    print("CHARATER IS C")

elif store_of_i == 3:
    print("CHARATER IS D")
            
elif store_of_i == 4:
    print("CHARATER IS E")
            
elif store_of_i == 5:
    print("CHARATER IS F")
            
elif store_of_i == 6:
    print("CHARATER IS G")
            
elif store_of_i == 7:
    print("CHARATER IS H")
            
elif store_of_i == 8:
    print("CHARATER IS I")
            
elif store_of_i == 9:
    print("CHARATER IS J")
            
elif store_of_i == 10:
    print("CHARATER IS K")
            
elif store_of_i == 11:
    print("CHARATER IS L")
            
elif store_of_i == 12:
    print("CHARATER IS M")
            
elif store_of_i == 13:
    print("CHARATER IS N")
            
elif store_of_i == 14:
    print("CHARATER IS O")
            
elif store_of_i == 15:
    print("CHARATER IS P")
            
elif store_of_i == 16:
    print("CHARATER IS Q")
            
elif store_of_i == 17:
    print("CHARATER IS R")
            
elif store_of_i == 18:
    print("CHARATER IS S")
            
elif store_of_i == 19:
    print("CHARATER IS T")
            
elif store_of_i == 20:
    print("CHARATER IS U")
            
elif store_of_i == 21:
    print("CHARATER IS V")
            
elif store_of_i == 22:
    print("CHARATER IS W")
            
elif store_of_i == 23:
    print("CHARATER IS X")
            
elif store_of_i == 24:
    print("CHARATER IS Y")
            
elif store_of_i == 25:
    print("CHARATER IS Z")
            
valval1=input(" ")



     
