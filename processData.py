import asyncio
from pyquery import PyQuery as pq
import config


async def processData(data,session):
    '''
    data is from the http response in main module.
    '''
    d = pq(data)
    title=d('div.picinfo span.title').text()
    url=d('div.picinfo span.links a').eq(1).text()
    wechat = d('ul.aboutus span').eq(0).text()
    phone = d('ul.aboutus span').eq(1).text()
    email = d('ul.aboutus span').eq(2).text()
    address = d('ul.aboutus span').eq(3).text()

    d = d('div.main')

    basicInfo = d('div.block-inc-info').text()
    investField=[]
    for tag in d('div.pad div.darkblue b').items():
        investField.append(tag.text())

    investTurn=[]
    for tag in d('div.pad div.yellow b').items():
        investTurn.append(tag.text())

    investors=[]
    for tag in d('ul.list-prodcase li b').items():
        investors.append(tag.text())

    print(title)
    # print(basicInfo)
    # print(investTurn)
    # print(investors)
    result={
        'title': title,
        'url': url,
        'phone': phone,
        'email': email,
        'address': address,
        'descript': basicInfo,
        'investField': investField,
        'investTurn': investTurn,
        'investor': investors
    }

    return result

      
    