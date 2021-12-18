def Signup():  # this is for signing up
    global pwordE  # global variables
    global nameE
    global roots
    rootA.destroy()
    roots = Tk()  # this creates the window just a blank one
    roots.title("Signup")  # these renames the title of said window to signup
    intruction = Label(roots,
                       text='Please Enter new Credidentials\n')  # this puts a label so just a piece of text saying 'please enter ...'
    intruction.grid(row=0, column=0, sticky=E)  # this just puts it in the window on row 0 and column 0

    nameL = Label(roots, text='New Username: ')  # this just does the same as above, instead with the text new username
    pwordL = Label(roots, text='New Password: ')
    nameL.grid(row=1, column=0, sticky=W)  # same thing as the intruction var just on different rows
    pwordL.grid(row=2, column=0, sticky=W)

    nameE = Entry(roots)  # this now puts on text box waiting for input
    pwordE = Entry(roots,
                   show='*')  # same as above ,yet show ='*' what this does is just replace the text with the '*' like a password box :D
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)

    signupButton = Button(roots, text='Signup', relief=GROOVE,
                          command=FSSignup)  # this create the button with the text 'signup', when you click the command FSSignup will run
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()  # this just make the window keep open, we will destro it soon
