import requests
from bs4 import BeautifulSoup
from pytrends.request import TrendReq
import pandas as pd

news_site_url = 'https://www.hindustantimes.com' #/search?q
headers  ={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}



pytrend = TrendReq()
print('running hindustan times scraper')
def get_top_keywords(country_name):
    trending = pytrend.trending_searches(pn=country_name)
    return list(trending[0])



trending_keywords = get_top_keywords('india')


data = []
for kw in trending_keywords:
    print(kw)
    url = news_site_url + '/search?q=' +kw
    response = requests.get(url,headers=headers)
    print(response)
    soup = BeautifulSoup(response.content,'lxml')
    try:
        result = soup.find_all('div',class_='cartHolder page-view-candidate listView')[:3]
        
    except:
        pass
    for each in result:
      #  print(each)
        a_tag = each.find('a',href=True)
        title = each.find('h2')
        title = title.text
        link = a_tag['href']
        img_url = each.find('img')['src']
        data.append({'title':title,'source':'Times Of India','link':news_site_url+'/'+link,'img':img_url})



df = pd.DataFrame(data)

def get_toi_data(as_df=False):
    if as_df:
        return df
    return data
#print(get_data(as_df=True))

