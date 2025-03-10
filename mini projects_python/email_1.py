#the below program is just to send email without using email.message library

# import smtplib

# s = smtplib.SMTP(host="smtp.gmail.com", port=587)
# s.starttls()
# s.login("imranibrahim795@gmail.com", "alnh xgyg yajt tbnl")
# s["su"]
# message = "Hi this is to test sending email from python program"
# s.sendmail("imranibrahim795@gmail.com", "mohamedimrant004@gmail.com", message)
# s.quit()


import smtplib
from email.message import EmailMessage
with open("ibrahim.txt", "rb") as file:
    # mails = [ "mohamedimrantajudeen@gmail.com", "kavinesh252006@gmail.com"]
    family = ["mohamedimrantajudeen@gmail.com, kavinesh252006@gmail.com, mohamedimrant004@gmail.com, aghaashvengatesan104@gmail.com"]
    email = EmailMessage()
    email["to"] = family
    email["from"] = "Mohamed Imran"
    email["subject"] = "testing automated email sending using python program"
    email.set_content("Congrats you have succesfully recieved this automated mail")
    with smtplib.SMTP(host= "smtp.gmail.com" , port= 587) as smtp:
        smtp.starttls()
        smtp.login("imranibrahim795@gmail.com", "alnh xgyg yajt tbnl")
        smtp.send_message(email)
        smtp.quit()
        print("Email sent!")
