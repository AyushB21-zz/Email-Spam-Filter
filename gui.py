root = Tk()
    root.title('New Message')
    To = Label(root, text="To:")
    Subject = Label(root, text="Subject:")
    text = Label(root, text="Message:")
    To.grid(row=1, column=0, sticky=W)
    Subject.grid(row=2, column=0, sticky=W)
    text.grid(row=3, column=0, sticky=NW)

    Toe = Entry(root, width=67)
    Subjecte = Entry(root, width=67)
    texte = Text(root, width=50, height=5)
    Toe.grid(row=1, column=1, sticky=W)
    Subjecte.grid(row=2, column=1, sticky=W)
    texte.grid(row=3, column=1, sticky=W)

    attach = Button(root, text="Attach", relief=GROOVE, command=attach)
    attach.grid(row=6, column=1, sticky=W)
    send = Button(root, text="Send", relief=GROOVE, command=Sendmail)
    send.grid(row=6, column=0, sticky=W)
    file = Label(root, text='')
    file.grid(row=7, column=0, sticky=W)
    root.geometry('500x170')
    root.mainloop()
