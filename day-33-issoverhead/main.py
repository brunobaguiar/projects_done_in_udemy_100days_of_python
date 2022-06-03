import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -15.622660  # Your latitude
MY_LONG = -46.548859  # Your longitude
my_email = "your@gmail.com"
password = "yourpassword"


def is_iss_up():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5):
        if (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
            return True
        else:
            return False
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour
    return hour_now >= sunset

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(10)
    if is_iss_up() and is_night():
        print("Look up! ISS on the sky!")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Encrypted message to secure our connection
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: Look up!\n\nISS on the sky!")
    else:
        print("Nothing on the sky")
