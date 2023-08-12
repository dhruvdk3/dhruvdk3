import requests,datetime, smtplib, time
my_long,my_lat = 78.8718, 21.7679
my_email, passcode = "myemail@gmail.com","my passcode"

def is_iss_overhead():
    ISS = requests.get(url="http://api.open-notify.org/iss-now.json")
    ISS.raise_for_status()
    issro_long, issro_lat = float(ISS.json()["iss_position"]["longitude"]),float(ISS.json()["iss_position"]["latitude"])
    if my_lat-5<= issro_lat <= my_lat+5 and my_long-5 <= issro_long <= my_long+5:
        return True

def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0")
    response.raise_for_status()
    sunrise = int((str(response.json()['results']['sunrise']).split('T'))[1].split(":")[0])
    sunset = int((str(response.json()['results']['sunset']).split('T'))[1].split(":")[0])

    tillnow = datetime.datetime.now()
    current_hour = tillnow.hour
    if current_hour >= sunset and current_hour <= sunrise:
        return True

while True:
    time.sleep(60)
    print(3)
    if is_iss_overhead() and is_night():
        send = smtplib.SMTP("smtp.gmail.com", port=587)
        send.starttls()
        send.login(user=my_email, password=passcode)
        send.sendmail(msg="Subject:Look above\n\nIssro is currently above you. look into the sky.")