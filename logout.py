
def logout():
    ro.destroy()
    r = Tk()
    r.title(':D')
    r.geometry('150x100')
    rlbl = Label(r, text='\n[+] Logged Out Successfully.', fg='blue')
    rlbl.pack()
    r.mainloop()
    login()
