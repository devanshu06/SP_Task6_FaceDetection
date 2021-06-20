import smtplib
def sendemail(sender_mail, reciever_mail,message, sender_password):
    print("Sending mail...")
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        print(s.login(sender_mail, sender_password))
        s.sendmail(sender_mail, reciever_mail, message)
        s.quit()
        print("Successfully sent email")    
    except Exception as e:
        print("Error: unable to send email : {}".format(e)) 
