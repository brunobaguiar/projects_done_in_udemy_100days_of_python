##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib

# import os
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

MY_EMAIL = "your@gmail.com"
PASSWORD = "your password"
today_birthday_name = ""
today_birthday_email = ""


# 4. Send the letter generated in step 3 to that person's email address.
def send_birth_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Encrypted message to secure our connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=today_birthday_email,
            msg=f"Subject: Happy Birthday!\n\n{data_file}")


# 1. Update the birthdays.csv
data_file_birth = pandas.read_csv("birthdays.csv")
birthday_dict = data_file_birth.to_dict('records')

# Today attributes
now = dt.datetime.now()
today = now.date()
month = now.month
day = now.day
year = now.year

# 2. Check if today matches a birthday in the birthdays.csv

# Check birthday dict for matches
for names in birthday_dict:
    if names["month"] == month and names["day"] == day:
        today_birthday_name = names['name']
        today_birthday_email = names['email']
        # 3. If step 2 is true, pick a random letter from letter
        # templates and replace the [NAME] with the person's actual
        # name from birthdays.csv
        # random_directory = random.choice(os.listdir("/letter_templates"))
        with open(
                f'letter_templates/'
                f'letter_{random.randint(1, 3)}.txt', mode="r") as file:
            # read file
            data_file = file.read()
            # find and replace word
            data_file = data_file.replace('[NAME]', today_birthday_name)
        print(f"It is {names['name']} birthday")
        send_birth_email()
    else:
        pass
