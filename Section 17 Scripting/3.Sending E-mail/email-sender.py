import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Omar Hesham"
email["to"] = "omarshehabwork@gmail.com"
email["subject"] = "you have won a million dollars!"
email.set_content("I am a python Master")
app_password_google = "vxxq uijn drnl fdel"
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # starts server
    smtp.starttls()  # encryption mechanism
    smtp.login("omarshehabwork@gmail.com", app_password_google)
    smtp.send_message(email)
    print("e-mail sent")
