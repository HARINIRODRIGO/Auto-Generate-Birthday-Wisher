import random
import smtplib
import pandas
import datetime

EMAIL_ADDRESS = "harini.9926@gmail.com"
PASSWORD = "9926@rodrigo"
message = ""
num = random.randint(1, 3)

data = pandas.read_csv("birthdays.csv")
date = datetime.datetime.now()
today = str(date.month) + ":" + str(date.day)

x = [[items.get("name"), items.get("email"), {"month": items.get("month"), "day": items.get("day")}]
     for row, items in data.iterrows()]

for i in x:
    b_day = str(i[2].get("month")) + ":" + str(i[2].get("day"))

    if today == b_day:
        with open(f"letter templates\\letter_{num}.txt") as letter:
            data = letter.readlines()
            data[0] = data[0].replace("[NAME]", i[0])

        for d in data:
            if d != "/n":
                message += d

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()  # For secure purposes
            connection.login(EMAIL_ADDRESS, PASSWORD)
            connection.sendmail(EMAIL_ADDRESS,
                                i[1],
                                f"Subject:Happy Birthday\n\n{message}")
