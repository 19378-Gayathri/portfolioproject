import requests
import os
import smtplib
from email.message import EmailMessage

API_KEY = os.environ["WEATHER_API_KEY"]

CITY = "Kollam"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"]

weather = data["weather"][0]["main"]

print("Temperature:", temperature)
print("Weather:", weather)

alert = False

if temperature > 35:
    alert = True

if weather.lower() in ["rain", "drizzle", "thunderstorm"]:
    alert = True

if alert:

    sender = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_PASSWORD"]

    msg = EmailMessage()

    msg["Subject"] = "Weather Alert"

    msg["From"] = sender

    msg["To"] = sender

    msg.set_content(
        f"""
Weather Alert!

City: {CITY}

Temperature: {temperature}°C

Condition: {weather}
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print("Alert sent!")

else:
    print("No alert needed")