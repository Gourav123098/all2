from plyer import notification
import requests
from bs4 import BeautifulSoup

def notyfy(title,massage):
    notification.notify(
        title=title,
        message=massage,
        app_icon = "./co.ico",
        timeout= 10
    )

def getdata(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    notyfy("me","This is good")    

    # myhtmldata = getdata("https://www.mohfw.gov.in/")
    # # print(myhtmldata)
    # soup = BeautifulSoup(myhtmldata,'html.parser')
    # for table in soup.find_all('table'):
    #     print(table)