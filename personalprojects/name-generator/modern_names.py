from bs4 import BeautifulSoup
import requests
import json

def urlScraper(url):
    response = requests.get(url, timeout=3)
    content = BeautifulSoup(response.content, "html.parser")

    #print(content)
    table = content.find('table',class_="t-stripe")
    body = table.find('tbody')
   # print(table)
    girlsname = set()
    boysname = set()
    for name in body.find_all('tr'):
        tds = name.find_all('td')
        if 'Source' in tds[1].text:
            break
        boysname.add(tds[1].text)
        girlsname.add(tds[3].text)

    print("Girls names here")
    print(girlsname)
    print("Boys names here")

    print(boysname)

    return boysname, girlsname


def main():
    boringBoy1, boringGirl1 = urlScraper('https://www.ssa.gov/oact/babynames/decades/century.html')
    boringBoy2, boringGirl2 = urlScraper('https://www.ssa.gov/oact/babynames/decades/names2000s.html')

    boringBoy = boringBoy1.union(boringBoy2)
    boringGirl = boringGirl1.union(boringGirl2)

    newBoy, newGirl = urlScraper('https://www.ssa.gov/oact/babynames/decades/names2010s.html')
    print(newBoy)
    print(newGirl)

    print("both boring and new boys names:")
    print(newBoy.intersection(boringBoy))
    print("both boring and new girls names:")
    print(newGirl.intersection(boringGirl))



if __name__ == "__main__":
    main()