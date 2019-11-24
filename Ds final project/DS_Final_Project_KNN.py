import os
import numpy as np
from PIL import Image



# function of array program
# Function to read data from database
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





# function of img program

# Function use to find score of every character
def KNNScore(arr,arr2):
    score = 0
    for y in range(0,250):
        for x in range(0,250):
            if(arr[x][y]==arr2[x][y]):
                score+=1
    return score


# Using bbox alogorithm to crop the user's image
def bbxcrop(arr,img):
    x1=-250
    x2=-1
    y1=-250
    y2=-1

    for y in range(0,250):
        for x in range(0,250):
            ny = arr[x,y]
            r = ny[0]

            if(r<100):
                
                if(x1==-1):
                    x1=x
                else:
                    x2=x

                if(y1==-1):
                    y1=y
                else:
                    y2=y
    
    img = img.crop((x1, y1, x2, y2))
    img = img.resize((250,250))
    img.save("update3.jpg")
    return img
            



# Break picture into pixel and convert into binary
def image_pixel(image):
    im = Image.open(image)
    
    pix = im.load()
    im=bbxcrop(pix,im)
    pix = im.load()

    arr =np.array([None for i in range(62500)])
    arr.shape=(250,250)
    for y in range(0,im.height-1):
        for x in range(0,im.width-1):
            ny = pix[x,y]
            img_rgb_pix = ((ny[0]+ny[1]+ny[2])/3)

            if (img_rgb_pix) < 100:
                arr[x,y]=0

            elif (img_rgb_pix) > 100:
                arr[x,y]=1
    
    return arr






userinputchoise=""

print("                         ************Welcome to Charater detection************** ")
print("                            Implimentation of K nearest Neighbors Algorithm \n\n\n")
print("                                     Press 1 for detection from array")
print("                                     Press 2 for detection from image\n\n")
print("          This project is important for kids who can easily able to learn character from here\n\n\n")
print("          \t  " , chr(169) , " Copyright all rights reserved CMT Softwares Solution\n\n")



try:
    userinputchoise=int(input("Enter your option = "))
except:
    print("Enter numerice value please")

os.system('cls')

if userinputchoise==1:


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



    # open data from files
    charcount=65
    for inter in range(26):
        myvalhold=str(chr(charcount))
        a=readfile(myvalhold)
        arrymaster[inter]=a
        charcount+=1





    # Analyzing data

    score = [0 for i in range(26)]
    max = -1000000

    for i in range(len(arrymaster)):
        temp=arrymaster[i]

        for j in range(5):
            for k in range(5):
            
                if temp[j][k]==search[j][k]:
                    score[i]+=1


    # Clear screen
    os.system('cls')
    



    store_of_i = 0
    print("\n SYMBOLS GIVEN AS INPUT ARE : \n")

    for i in range(5):
        for j in range(5):
            print(search[i][j], end="")
        print("")
    print("\n")




    # Define score and weight of each charater as compare to user define

    for i in range(len(score)):
        if score[i] > max:
            max= score[i]
            store_of_i=i
            
            



    #Checking and analyzing result of charaters  

    charres=65

    for res in range(26):
        if store_of_i==res:
            print("Your give symbol is =  ",str(chr(charres)))
        else:
            charres+=1


            
    valval1=input(" ")




#________________________________________________________________________________________________________
# Image detection program. Image detection program. Image detection program. Image detection program
#________________________________________________________________________________________________________


elif userinputchoise==2:




    # Test array store user define picture given through path link
    test = np.array([None for i in range(62500)])
    test.shape = (250,250)



    # Using char from 65 to 91 in to open jpg files from database using ASCII Table
    myaplha = 65


    # Initilization of arrays/lists
    n = [None for i in range(26)]
    charaterhold = [None for i in range(26)]
    aplha = [None for i in range(26)]


    # Store A to Z in alpha array/list
    for i in range(len(aplha)):
        aplha[i] = chr(myaplha)
        myaplha+=1





    print("              ************* WELCOME NEW USER ************\n\n\n")
    print("             Please enter the path link of your character\n")
    print("      Our system will detect that specific character using KNN algorithm\n")
    print("         And predict the result using artificial intelligance\n")
    print("                        Hope you will enjoy....... \n")
    print("             It will help in your childern learning process\n\n\n")
    print("                     +2 age allow not for infants")
    print("            Press any key to continue, Except power button :P ")
    input("")

    # Clear screen
    os.system('cls')




    # User input path of jpg/img
    usergivepath=""

    try: 
        usergivepath=input("Enter complete path of image = ")
    except:
        print("Enter correct path of image file")


    image = 'test.jpg'
    testn = image_pixel(usergivepath)



    # Open files from database
    for j in range(len(charaterhold)):
        dh = str(aplha[j])
        datahold = (dh+".jpg")
        charaterhold[j]=image_pixel(datahold)




    # Method calling to save score for each character
    for j in range(26):
        n[j] = (KNNScore(testn,charaterhold[j]))



    # min2 and inx variable for analizing result
    min2 =-1
    inx =-1





    for i in range(0,len(n)):

        if(min2<n[i]):
            inx = i
            min2 = n[i]



    # Print Character after detection
    print("\n\n_______________________________________")
    print("Your given character is ",(chr)(65+inx))
    print("_______________________________________\n\n")


else:
    print("Wrong selection")

input("")


# Copyright all rights reserved CMT Softwares Solution 2019- 3019
# cmt-ss.live
# Muhammad Tayyab
# Muhammad Adnan
# Najam shehzad
# Fazeel abbass