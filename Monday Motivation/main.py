import smtplib
import datetime
import random

my_email = "harini.9926@gmail.com"
password = "9926@rodrigo"
sender = "harini.2019754@iit.ac.lk"
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

