import smtplib
import datetime
import random
from secret import EMAIL, PASSWORD, SENDER_EMAIL

my_email = EMAIL
password = PASSWORD
sender = SENDER_EMAIL
now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open(file="quotes.txt", mode="r") as file:
        text = random.choice(file.readlines())
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # For secure purposes
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=sender,
                            msg=f"Subject:Monday Motivation\n\n{text}")

