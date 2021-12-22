def seanre():
    with open(sar, 'w+') as f:  # creates the documents using the variables we made at the top

        f.write(mail_date.get())  # nameE is the variable we were storing the input to
        f.write(',')
        f.write(mail_subject.get())  # same as nameE
        f.write('\n')
        f.write(mail_from.get())  # same as nameE
        f.write('\n')
        f.close()  # closes the file
    roots.destroy()  # this will destroy the signup window
    login()
