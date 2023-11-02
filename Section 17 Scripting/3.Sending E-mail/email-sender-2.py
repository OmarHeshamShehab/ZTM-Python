import smtplib
from email.message import EmailMessage
from pathlib import (
    Path,  # we could also used os.path as it allows us to access HTML file as Path mainly has read_text
)
from string import Template

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Omar Hesham"
email["to"] = "omarshehabwork@gmail.com"
email["subject"] = "you have won a million dollars!"
email.set_content(html.substitute({"name": "TinTin"}), "html")
app_password_google = "vxxq uijn drnl fdel"

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # starts server
    smtp.starttls()  # encryption mechanism
    smtp.login("omarshehabwork@gmail.com", app_password_google)
    smtp.send_message(email)
    print("e-mail sent")
