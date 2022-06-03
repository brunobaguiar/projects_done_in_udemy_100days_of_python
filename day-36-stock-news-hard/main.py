import requests
from datetime import datetime
from pandas.tseries.offsets import BDay
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "9FFZ4NOEJ12LZCPL"
NEWS_API_KEY = "0c2563c016ff4e42aa3caf42a7416655"

account_sid = 'ACa10d9456df04aa1cf8a254dabc06f48d'
auth_token = '3c81b534c1b685b95ae0aac1019f9e08'

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get the stock data of TSLA
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "9FFZ4NOEJ12LZCPL",
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

# Using list comprehension to turn dict in list
data_list = [value for (key, value) in stock_data.items()]

# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.

# Getting close stock value of yesterday
yesterday_data = data_list[0]
yesterday_close_value = float(yesterday_data["4. close"])
print(yesterday_close_value)

# Getting close stock value of the day before yesterday
the_day_before_yesterday_data = data_list[1]
the_day_before_yesterday_close_value = float(the_day_before_yesterday_data["4. close"])
print(the_day_before_yesterday_close_value)

close_value_delta = abs(yesterday_close_value - the_day_before_yesterday_close_value)
delta_percentage = close_value_delta / yesterday_close_value * 100
print(close_value_delta, delta_percentage)
if yesterday_close_value < the_day_before_yesterday_close_value:
    delta = f"🔺{round(delta_percentage)}%"
else:
    delta = f"🔻{round(delta_percentage)}%"


# HINT 2: Work out the value of 5% of yesterday's closing stock price.
def is_volatility_high():
    if delta_percentage > 10:
        return True
    else:
        return False


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator

# Get the last news data of TSLA
news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}

response = requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
articles = response.json()["articles"]
three_articles = articles[:3]
print(three_articles)

formatted_articles = [f"TSLA: {delta}\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
print(formatted_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.

if is_volatility_high():
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+1599999999',
            to='+5511999999999'
        )
        print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
