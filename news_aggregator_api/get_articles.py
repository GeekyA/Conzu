import pandas as pd
import random
import numpy as np




def articles_from_csv(filtered=False):
    linux_path = '/home/ansh/'
    windows_path = 'C:/news_1/'
    #d = pd.read_csv('C:/news_1/news_aggregator/articles.csv')
    if filtered:
        #d = pd.read_csv(linux_path+'news_aggregator/filtered.csv')
        d = pd.read_csv('C:/news_1/news_aggregator-main/filtered.csv')
    else:
        #d = pd.read_csv(linux_path+'news_aggregator/articles.csv')
        d = pd.read_csv('C:/news_1/news_aggregator-main/articles.csv')
    d = d.to_dict('records')
    return d
    


