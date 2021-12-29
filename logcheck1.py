def CheckLogin():
    global ro
    with open(creds) as f:
        data = csv.reader(f)
        for line in data:
            try:
                uname = line[0]
                pword = line[1]
                if nameEL.get() == uname and pwordEL.get() == pword:
                    rootA.destroy()
                    r = Tk()
                    r.title(':D')
                    r.geometry('150x50')
                    rlbl = Label(r, text='\n[+] Logged In', fg='blue', bg='silver')
                    rlbl.pack()
                    r.mainloop()
                    send()
            except IndexError:
                pass
