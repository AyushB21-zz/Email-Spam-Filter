def Pass():
        pass

    def Sendmail():
        global count
        global c
        msg = MIMEMultipart()
        msg['From'] = 'abcxyz123@gmail.com'
        msg['To'] = Toe.get()  # send to multiple users
        msg['Subject'] = Subjecte.get()

        body = texte.get("1.0", "end-1c")
        msg.attach(MIMEText(body, 'plain'))
        if count > 0:
            filename = root.filename
            attachment = open(filename, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename=" + filename)
            msg.attach(part)
