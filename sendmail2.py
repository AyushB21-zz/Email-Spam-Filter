else:
            pass
        text = msg.as_string()
        mail = smtplib.SMTP('smtp.gmail.com', 25)
        mail.connect('smtp.gmail.com', 25)
        mail.starttls()
        mail.login("abcxyz123@gmail.com", "abc123")  # this is in format username , password

        try:
            mail.sendmail("abcxyz123@gmail.com", msg['To'], text)
            c += 1
            print('email sent')
        except:
            print('error sending email')

        mail.quit()
        root.destroy()
        if c >= 1:

            r = Tk()
            r.title(':D')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[+] Email sent', fg='blue', bg='silver')
            rlbl.pack()
            r.mainloop()

        else:
            r = Tk()
            r.title(':D')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[!] Error Sending Email', fg='blue', bg='silver')
            rlbl.pack()
            r.mainloop()
