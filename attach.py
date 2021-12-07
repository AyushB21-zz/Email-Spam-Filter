def mail():
    def attach():
        global count
        count += 1
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        file = Label(root, text=root.filename)
        file.grid(row=7, column=0, sticky=W)

