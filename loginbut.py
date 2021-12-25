def login():
    global nameEL
    global pwordEL
    global rootA
    rootA = Tk()
    rootA.geometry('500x500')
    rootA.title('Login')
    # intruction=Label(rootA,text='Please Login')
    intruction = Label(rootA, text='Email Client', fg='black', font=('Algerian', 30))
    intruction.grid(sticky=E)

    nameL = Label(rootA, text='Username: ', font=("Courier", 20))
    pwordL = Label(rootA, text='Password: ', font=("Courier", 20))
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    loginB = Button(rootA, text='Login', fg='black', height=2, width=30, font='bold', bg='silver', relief=GROOVE,
                    command=CheckLogin)
    loginB.grid(columnspan=2, sticky=W)
    loginB = Button(rootA, text='Signup', fg='blue', height=2, width=30, font='bold', bg='silver', relief=GROOVE,
                    command=Signup)
    loginB.grid(columnspan=2, sticky=W)

    rmuser = Button(rootA, text='Delete User', font='bold', bg='silver', fg='red', relief=GROOVE, command=DelUser)
    rmuser.grid(column=2, sticky=W)
    rootA.mainloop()
