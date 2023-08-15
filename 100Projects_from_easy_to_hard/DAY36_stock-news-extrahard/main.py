import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "ALPHA_API_KEY"
NEWS_API_KEY = "NEWS_API_KEY"
twlio_number = "+twlio_number"
auth_token = "auth_token"
account_sid = "account_sid"

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":ALPHA_API_KEY
}
news_parameters = {
    "q":COMPANY_NAME,
    "from":"2023-07-15",
    "sortBy":"publishedAt",
    "apiKey":NEWS_API_KEY
}
up_down = None
response = requests.get(url = "https://www.alphavantage.co/query", params=stock_parameters)
daily_data = response.json()["Time Series (Daily)"]
stock_data = []
for i in daily_data:
    stock_data.append(float(daily_data[i]["4. close"]))
    if len(stock_data)>=2:break

percentage = ((stock_data[0]-stock_data[1])/stock_data[0])*100
if percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
if abs(percentage) >= 1:
    news_request = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_article = news_request.json()['articles']
    first_3_news = news_article[:3]
    mesg_for_user = [f"TSLA: {up_down}{int(percentage)}%\nHeadline: {i['title']}\nBrief: {i['description']}" for i in first_3_news]
    client = Client(account_sid, auth_token)
    for mesg_str in mesg_for_user:
        print(mesg_str)
        message = client.messages \
                    .create(
                        body=mesg_str,
                        from_= twlio_number,
                        to='your number'
                    )
