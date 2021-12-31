def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()


if os.path.isfile(creds):
    login()
else:
    Signup()
