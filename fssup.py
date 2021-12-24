def FSSignup():
    with open(creds, 'a') as f:  # creates the documents using the variables we made at the top

        f.write(nameE.get())  # nameE is the variable we were storing the input to
        f.write(',')
        f.write(pwordE.get())  # same as nameE
        f.write('\n')
        f.close()  # closes the file
    roots.destroy()  # this will destroy the signup window
    login()  # this will move us on to the login defination
