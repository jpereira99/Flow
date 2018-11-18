import os
import time
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
from datetime import datetime
from selenium import webdriver

global itinDepart1
global itinArrive1
global itinPrice1
global itinTimeElapsed1

global itinDepart2
global itinArrive2
global itinPrice2
global itinTimeElapsed2

global itinDepart3
global itinArrive3
global itinPrice3
global itinTimeElapsed3

global allitems

def scrape(startPoint, endPoint, departOrNot, date, time, AMOrNot):
    driver = webdriver.Chrome("/Users/jayden/Documents/Projects/Flow/chromedriver")
    driver.set_page_load_timeout(30)
    driver.get("https://www.njtransit.com/hp/hp_servlet.srv?hdnPageAction=HomePageTo")
    driver.implicitly_wait(20)

    class NJTransit():
        starting = []
        dest = []

    driver.find_element_by_id("starting_street_address").send_keys(startPoint)
    driver.find_element_by_id("dest_street_address").send_keys(endPoint)

    if departOrNot == False:
        driver.find_element_by_id("arrive").click()

    driver.find_element_by_id("datepicker").clear()
    driver.find_element_by_id("datepicker").send_keys(date)

    driver.find_element_by_id("Time").clear()
    driver.find_element_by_id("Time").send_keys(time)

    driver.find_element_by_id("Suffix").click()
    if AMOrNot == False:
        driver.find_element_by_id("Suffix").send_keys("PM")
    else:
        driver.find_element_by_id("Suffix").send_keys("AM")

    driver.find_element_by_id("submitbtn").click()

    html_source=driver.page_source
    driver.quit()
    soup=BeautifulSoup(html_source, 'html.parser')

    itinerary = soup.findAll('font')
    numtotal = len(itinerary)

    i = 0
    state1 = 0
    timechange = "12:00"
    FMT = '%I:%M %p'

    while i < numtotal:
        if itinerary[i].get_text() == 'Transfer Fee':
            if state1 == 0:
                itinMark1 = i
                state1 += 1
            elif state1 == 1:
                itinMark2 = i
                state1 += 1
            elif state1 == 2:
                itinMark3 = i
                state1 += 1
        i += 1





    itinDepart1 = itinerary[0].get_text()
    itinArrive1 = itinerary[itinMark1 - 7].get_text()
    itinDepart1 = itinDepart1[8:].strip()
    itinArrive1 = itinArrive1[8:].strip()
    itinPrice1 = Decimal(sub(r'[^\d.]','',itinerary[itinMark1 + 1].get_text().strip())) + Decimal(sub(r'[^\d.]','',itinerary[itinMark1 - 2].get_text().strip())) + Decimal(sub(r'[^\d.]','',itinerary[itinMark1 - 5].get_text().strip()))
    itinTimeEnd1 = itinArrive1[-8:].strip()
    itinTimeStart1 = itinDepart1[-8:].strip()
    itinTimeElapsed1 = datetime.strptime(itinTimeEnd1, FMT) - datetime.strptime(itinTimeStart1, FMT)

    itinDepart2 = itinerary[itinMark1 + 3].get_text()
    itinArrive2 = itinerary[itinMark2 - 7].get_text()
    itinDepart2 = itinDepart2[8:].strip()
    itinArrive2 = itinArrive2[8:].strip()
    itinPrice2 = Decimal(sub(r'[^\d.]','',itinerary[itinMark2 + 1].get_text().strip())) + Decimal(sub(r'[^\d.]','',itinerary[itinMark2 - 2].get_text().strip())) + Decimal(sub(r'[^\d.]','',itinerary[itinMark2 - 5].get_text().strip()))
    itinTimeEnd2 = itinArrive2[-8:].strip()
    itinTimeStart2 = itinDepart2[-8:].strip()
    itinTimeElapsed2 = datetime.strptime(itinTimeEnd2, FMT) - datetime.strptime(itinTimeStart2, FMT)

    itinDepart3 = itinerary[itinMark2 + 3].get_text()
    itinArrive3 = itinerary[itinMark3 - 7].get_text()
    itinDepart3 = itinDepart3[8:].strip()
    itinArrive3 = itinArrive3[8:].strip()
    itinPrice3 = Decimal(sub(r'[^\d.]','',itinerary[itinMark3 + 1].get_text().strip())) + Decimal(sub(r'[^\d.]','',itinerary[itinMark3 - 2].get_text().strip())) + Decimal(sub(r'[^\d.]','',itinerary[itinMark3 - 5].get_text().strip()))
    itinTimeEnd3 = itinArrive3[-8:].strip()
    itinTimeStart3 = itinDepart3[-8:].strip()
    itinTimeElapsed3 = datetime.strptime(itinTimeEnd3, FMT) - datetime.strptime(itinTimeStart3, FMT)

    allitems = {
        "Depart1": itinDepart1,
        "Arrive1": itinArrive1,
        "Price1": itinPrice1,
        "TimeElapsed1": itinTimeElapsed1,

        "Depart2": itinDepart2,
        "Arrive2": itinArrive2,
        "Price2": itinPrice2,
        "TimeElapsed2": itinTimeElapsed2,

        "Depart3": itinDepart3,
        "Arrive3": itinArrive3,
        "Price3": itinPrice3,
        "TimeElapsed3": itinTimeElapsed3
    }
    return allitems