#!/usr/bin/python

import smtplib
import re 
import gspread
import string
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint
from oauth2client.service_account import ServiceAccountCredentials

#Randomly select a quote 
def choose_quote(wks):
    randomQuote = (randint(0,145))
    quote_entry = wks.cell(randomQuote, 1)
    return quote_entry.value 

#email the quote
def email(quote):
    me = "luanna.tasks@gmail.com"
    you = "luannaochoa@gmail.com"
    attachment = 'qod.png'

    msg = MIMEMultipart('related')
    msg['Subject'] = "Quote of The Day"
    msg['From'] = me
    msg['To'] = you

    message = """
    <html>
    <header>
        <center><img src="cid:%s"><br></center>
    </header>
    <body>
        <br>
        <br>
        <br>
        <center><b>%s</b><br></center>
    </body>
    </html>
    """ % (attachment, quote)

    msgText = MIMEText(message, 'html')  
    msg.attach(msgText)   

    fp = open(attachment, 'rb')                                                  
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<{}>'.format(attachment))
    msg.attach(img)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("luanna.tasks@gmail.com", "luannatasks!")
    server.sendmail(me, you, msg.as_string())
    server.quit()


def main():
    "main function"
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('access.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("Quotes").sheet1
    email(choose_quote(wks))

if __name__ == "__main__":
    main()

