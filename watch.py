#!/usr/bin/python3.5
from lxml import html
import requests

page=requests.get('https://en.wikipedia.org/wiki/Xbox_One_system_software')

doc = html.fromstring(page.text)

rows = doc.xpath('//table[@class="infobox vevent"]/tr/*/text()')
current_release = rows[12]

file = open('previous_release.txt', 'w+')
previous_release = file.readline()
if (previous_release != current_release) :
        print("new release!")
