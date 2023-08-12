##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random,smtplib
data = pd.read_csv("birthdays.csv")
dic_data = data.to_dict(orient="records")
now = dt.datetime.now()
my_email = "anemail@gmail.com"
password="a password"


def add_csv():
    x = input("Enter name,email,year,month,day seperated by comma\n").split(",")
    dic = {'name': x[0], 'email': x[1], 'year': x[2], 'month': x[3], 'day': x[4]}
    dic_data.append(dic)
    data = pd.DataFrame(dic_data)
    data.to_csv("birthdays.csv", index=False)
    

while True:
    check = input("Do you want to add more records to the csv?(Y/N)\n").upper()
    if check == 'Y':
        add_csv()
    else:break


for i in dic_data:
    if i["month"] == now.month:
        if i["day"] == now.day:
            
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
                templet = file.read()
            templet = templet.replace("[NAME]", i["name"])
# Sending mail
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=i["email"], msg=f"Subject:Happy Birthday{i['name']}\n\n{templet}")

