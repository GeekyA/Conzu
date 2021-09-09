from bs4 import BeautifulSoup
import requests
from pytrends.request import TrendReq
import pandas as pd
import random


pytrend = TrendReq()

def get_top_keywords(country_name):
    trending = pytrend.trending_searches(pn=country_name)
    return list(trending[0])


print('running ndtv')
news_site_url = 'https://www.ndtv.com'

todays_keywords = get_top_keywords('india')



html_content = []

for kw in todays_keywords:
    print(kw)
    url = news_site_url + '/search?searchtext=' + kw
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.content,'lxml')
    try:
        results = soup.find('ul',class_='src_lst-ul').find_all('li')[:3]
        html_content.append(results)
    except:
        print(f"Exception here: {kw}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
        pass
    
    
data = []
for result in html_content:
    for article in result:
        img_url = article.find('span',{'class':'img-gratio'}).find('img',{'class':'img_brd marr10'})['src']
        a_tag = article.find('div',{'class':'src_itm-ttl'}).find('a',title=True,href=True)
        data.append({'title':a_tag['title'],'source':'NDTV','link':a_tag['href'],'img':img_url})

df = pd.DataFrame(data)
print(df)

def get_ndtv_data(as_df=False):
    if as_df:
        return df
    return data

#print(get_data(as_df=True))
