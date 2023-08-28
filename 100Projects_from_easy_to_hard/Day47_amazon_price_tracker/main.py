from bs4 import BeautifulSoup
import requests, lxml, smtplib

my_email = "mail"
password = "password"
header = {
    "Accept-Language":"lang",
    "User-Agent":"user agent"
}
response = requests.get(url="https://www.amazon.in/Dr-Trust-Electronic-Rechargeable-Composition/dp/B08VKBZ9VJ/ref=sr_1_6?crid=2ESZLKM6V2ZRR&keywords=realme+weight+machine&qid=1693216980&sprefix=realme+weight%2Caps%2C202&sr=8-6", headers=header)
response_data = response.text

soup = BeautifulSoup(response_data, 'lxml')
x = soup.find(name="span", class_="a-offscreen")
price = float(x.getText().replace('₹', '').replace(',', ''))
title = str(soup.find(name="span", id = "productTitle").string.strip())
if price < 1200:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Price Alert\n\n{title} id now at {price}")

