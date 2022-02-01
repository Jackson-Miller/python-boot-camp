import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
EMAIL_SERVER = os.getenv("EMAIL_SERVER")
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
item_uri= "https://smile.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS"
goal_price = 199.99
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


response = requests.get(item_uri, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price_string = soup.find(class_="a-offscreen").getText()
price = float(price_string.replace("$", ""))
item_name = soup.find(id="productTitle").getText().strip()

if price <= goal_price:
    with smtplib.SMTP_SSL(EMAIL_SERVER, port=465) as connection:
        connection.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_USERNAME,
            to_addrs=EMAIL_USERNAME,
            msg=f"From: {EMAIL_USERNAME}\r\nTo: {EMAIL_USERNAME}\r\nSubject:Amazon Price Alert!\r\nThe item {item_name} is ${price} and is lower than your goal of ${goal_price}.\r\n\r\n{item_uri}"
        )
