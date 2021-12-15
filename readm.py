def readm():
    import imapclient
    import pyzmail
    mail = imapclient.IMAPClient("imap.gmail.com", ssl=True)
    mail.login("abcxyz123@gmail.com", "abc123")
    mail.select_folder('INBOX', readonly=True)
    uid_A = mail.search(["SEEN"])
    for i in uid_A:  # loop for displaying the seen mails
        id = i
        email_data = mail.fetch([id], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(email_data[id][b"BODY[]"])
        # body_text = message.text_part.get_payload().decode(message.text_part.charset)
        mail_date = message.get_decoded_header('date')
        mail_subject = message.get_subject()
        mail_from = message.get_addresses('from')
        print("from:", mail_from, "\n" "Date:", mail_date, "\n" "Subject:", mail_subject, '\n')
    mail.logout()
