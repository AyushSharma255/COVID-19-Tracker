'''
This is inteneded for the US statistics, if you want a specific one,
hop onto 'url', and find the information link desired.
'''


import requests
from bs4 import BeautifulSoup as bsoup

url = "https://www.worldometers.info/coronavirus/country/us/"
counterId = "maincounter-wrap"

def requestInformation():
    urlRequest = requests.get(url)  # Request
    urlSoup = bsoup(urlRequest.text, "lxml")

    mainCounters = urlSoup.find_all("div", {"id": counterId})

    numbers = []
    '''
    'numbers' Index

    0 - Cases
    1 - Deaths
    2- Recoveries
    '''

    for counter in mainCounters:
        spanNumber = counter.find(
            "span")  # Only one span tag is in all of these #maincounter-wrap tags, in the span tag is the data we need
        numbers.append(spanNumber.contents[0])  # contents[0] refers to the text in the tag

    return numbers

