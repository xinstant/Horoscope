#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:42:42 2021

@author: Maks Fraszka

Using webscraping, this function returns a paragraph detailing your current 
horoscope based on your input of the zodiac sign.

"""

import requests
import bs4

zodiacs = {'Aries':1,'Taurus':2,'Gemini':3,'Cancer':4,'Leo':5,
           'Virgo':6,'Libra':7,'Scorpio':8,'Sagittarius':9,
           'Capricorn':10,'Aquarius':11,'Pisces':12}

def zodiac():
    x = input('Type in your zodiac sign: ')
    url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={}'
    res = requests.get(url.format(zodiacs[x]))
    soup = bs4.BeautifulSoup(res.text,'lxml')
    text = soup.select('p')
    horoscope = text[0]
    return horoscope
