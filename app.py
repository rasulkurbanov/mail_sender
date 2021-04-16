import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "It is a test message from email_sender"
msg['From'] = "Rasuljon Kurbanov"
msg['To'] = "rasuljohn139@gmail.com"

msg.set_content("Hey this is a text from python app")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("rasuliy550@gmail.com", "MushtariyBonu0509")
    smtp.send_message(msg)
    print("all is ok")

