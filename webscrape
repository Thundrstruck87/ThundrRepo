# This webscraping program will scrape the website below to scan for ammo being in stock or out of stock. If in stock
# it will send an email notification to two email addresse

import smtplib
from bs4 import BeautifulSoup
import requests
import time

def get_page_html(url):
    page = requests.get(url)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("span", {"class": "product-line-stock-msg-out-text"})
    if len(out_of_stock_divs) < 1:
        print("item is available")
        return True
    else:
        return False



def check_inventory():
    url = "https://www.[redacted].com/hornady-5-56-nato-55-gr-fmj-m193-frontierr"
    page_html = get_page_html(url)
    while True:
        if check_item_in_stock(page_html) == True:
            send_mail()
        else:
            print("Item is out of stock")
            break


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email123@email.com', 'password')
    subject = "Ammo Is In!"
    body = 'Hey, ammo is in! Check the link! https://[redacted].com/hornady-5-56-nato-55-gr-fmj-m193-frontierr'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('email123@email.com','email123@email.com',msg)
    print('Email has been sent')

    server.quit()

while False:
    check_inventory()

while True:
    print("Item is out of stock, checking again...")
    time.sleep(10800) # This will run every 3 hours

# Program will run every 3 hours WHILE condition is true, meaning that the item is out of stock
# Once item is in stock, program should send notification via email and terminate
