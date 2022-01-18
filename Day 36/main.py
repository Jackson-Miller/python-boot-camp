import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT = os.environ.get("TWILIO_ACCOUNT")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def get_stock_price_daily_difference():
    api_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": AV_API_KEY
    }

    response = requests.get(AV_ENDPOINT, api_params)
    stock_data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in stock_data.items()]
    yesterdays_closing_price = float(data_list[0]["4. close"])
    day_priors_closing_price = float(data_list[1]["4. close"])
    price_difference = abs(yesterdays_closing_price - day_priors_closing_price )
    difference_percentage = price_difference / yesterdays_closing_price * 100
    return difference_percentage


def get_news_results():
    api_params = {
        "qInTitle":COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_ENDPOINT, api_params)
    news_articles = response.json()["articles"][:3]
    headlines = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_articles]
    for article in headlines:
        send_sms(article)


def send_sms(message):
    client = Client(TWILIO_ACCOUNT, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_='<phone number>',
        to='<phone number>'
    )


stock_change_percent = get_stock_price_daily_difference()

if stock_change_percent > 5:
    get_news_results()
