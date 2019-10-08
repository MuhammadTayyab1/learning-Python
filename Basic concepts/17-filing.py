
# r read
# w write
# a+ append

fs= open(r'C:\Users\Tayyab\Desktop\newfile.txt','w')
fs.write("This is my data")
fs.close()


fs1= open(r'C:\Users\Tayyab\Desktop\newfile.txt','r')
hold=fs1.read()
print(hold)
