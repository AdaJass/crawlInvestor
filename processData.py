import asyncio
from pyquery import PyQuery as pq
import config

async def processData(data,session):
    '''
    data is from the http response in main module.
    '''
    d = pd(data)
    title=d('div.picinfo span.title').text()
    url=d('div.picinfo span.links a').eq(1).text()
    wechat = d('ul.aboutus span').eq(0).text()
    phone = d('ul.aboutus span').eq(1).text()
    email = d('ul.aboutus span').eq(2).text()
    address = d('ul.aboutus span').eq(3).text()

    d = d('div.main')

    basicInfo = d('div.block-inc-info').text()
    investField=[]
    for tag in d('div.pad div.darkblue b'):
        investField.append(tag.text())

    investTurn=[]
    for tag in d('div.pad div.yellow b'):
        investTurn.append(tag.text())

    investors=[]
    for tag in d('ul.list-prodcase li b'):
        investors.append(tag.text())
        
            

