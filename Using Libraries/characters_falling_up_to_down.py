import random
import time
import os


se=int(input("Enter seconds =   "))

for i in range(se):
    b=[]

    for j in range(20):
        c=random.randint(65,89)
        b.append(chr(c))


    for m in range(4):
        hold= random.randint(0,5)

        if hold==0:
            print(b[0],"                  ",b[1],"            ",b[2],"                        ",b[3],"              ",b[4],"\n\n\n\n\n")
        elif hold==1:
            print("       ",b[5],"                 ",b[6],"               ",b[7],"                     ",b[8],"             ",b[9],"\n\n\n\n\n")
        elif hold==2:
            print("  ",b[10],"       ",b[11],"                  ",b[12],"                ",b[13],"                            ",b[14],"\n\n\n\n\n")
        else:
            print(b[15],"                       ",b[6],"                  ",b[17],"                   ",b[18],"                        ",b[19],"\n\n\n\n\n")
    
    time.sleep(1)
    del b
    os.system('cls')


    


