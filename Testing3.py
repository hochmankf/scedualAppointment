from re import S
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from datetime import datetime, timedelta
from datetime import date
from datetime import datetime
from datetime import datetime, timezone
import os
import smtplib


class DemoGetText():
    def demo_gettext(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://serguide.maccabi4u.co.il/heb/doctors/doctorssearchresults/?City=5000&Gender=2&PageNumber=1&RequestId=6e184a98-1969-5069-83f0-affd9ba8a1d0&Source=SearchPage&TreatPubTypeList=453780005&TreatType=453780005")
        time.sleep(12)
        text = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[2]').text
        print(text)
        time.sleep(2)

        closestDate = text[7:]
        print(closestDate)
        dateformat = datetime.strptime(closestDate, "%d/%m/%y")
        print(dateformat, "formated")

        today = datetime.now()
        print("today is ", today)

        delta = dateformat - today
        print("next appintment is within ", delta.days, "days")

        deltaInt = delta.days
        msg = "Next appintment is within", deltaInt, "days"

        max_days = 30

        if deltaInt < max_days:
            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()
            server.login('mikatestprog@gmail.com', 'Yomo111!!!')

            server.sendmail('mikatestprog@gmail.com',
                            'mikatestprog@gmail.com', msg)

            print('Mail sent')

        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('mikatestprog@gmail.com', 'Yomo111!!!')

            server.sendmail('mikatestprog@gmail.com',
                            'mikatestprog@gmail.com', 'No colonoscopy for you!')
            print('Mail sent')


findbyxpath = DemoGetText()
findbyxpath.demo_gettext()
