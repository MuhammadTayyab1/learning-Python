import tkinter

def login():
    txtfld=tkinter.Entry(text="ok", bd=5)
    txtfld.place(x=180, y=270)



app = tkinter.Tk()
app.title("Login")
app.minsize(500, 500)
helloLabel = tkinter.Label(app, text="Login your account").pack()

label1=tkinter.Label(text="User name")
label1.place(x=80,y=170)

txtfld=tkinter.Entry(text="Name", bd=5)
txtfld.place(x=180, y=170)

label2=tkinter.Label(text="Password", textvariable="nm")
label2.place(x=80,y=230)

txtfld1=tkinter.Entry(text="Password", textvariable="pa", bd=5)
txtfld1.place(x=180, y=230)

b1=tkinter.Button(text="login",width=12,bg="brown",fg="white",command="login")
b1.place(x=150,y=380)

app.mainloop()
