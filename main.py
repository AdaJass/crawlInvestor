import aiohttp
import asyncio
import config
import processData as pd
import sys

async def fetchData(pages, callback = pd.processData):
    #set request url and parameters here or you can pass from outside. 
    
    #use s.** request a webside will keep-alive the connection automaticaly,
    #so you can set multi request here without close the connection 
    #while in the same domain.
    #i.e. 
    #await s.get('***/page1')
    #await s.get('***/page2')
    ######################################################################## 
    cookies = {}

    conn = aiohttp.TCPConnector(limit=config.REQ_AMOUNTS)    
    s = aiohttp.ClientSession(headers = config.HEADERS, cookies=cookies, connector=conn)   

    url = 'https://www.itjuzi.com/investfirm/'
    while  pages<6484:        
        async with s.get(url+str(pages+1)) as r:
            data =  await r.text(encoding='utf-8')
            investor = await callback(data, s)
        pages=pages+17

if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    #total invest departments has 6484
    #coroutine in tasks will run 
    tasks = [fetchData(i, pd.processData) for i in range(17)]    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close() 
