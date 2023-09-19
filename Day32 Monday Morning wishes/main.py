from smtplib import SMTP
from datetime import datetime
from random import choice
MY_EMAIL = "juisch20220011145@gmail.com"
MY_PASSWORD = "ncqhirekxceafrbr"

connection = SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASSWORD)

now = datetime.now()
day_of_week = now.weekday()
Monday = 0

if day_of_week == Monday:
    with open("quotes.txt", "r") as quote_file:
        quotes = quote_file.readlines()
        random_quote = choice(quotes)

    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject : Monday Motivation {random_quote}"
    )





