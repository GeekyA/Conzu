from ndtv_scraper import get_ndtv_data # ndtv scraper
from toi_scraper import get_toi_data # toi scraper
import pandas as pd
import numpy as np
import os
import random 




data1 = get_ndtv_data()
data2 = get_toi_data()
full_data = data1 + data2 

data = pd.DataFrame(data1)
data = data.dropna()
filtered_data = data.iloc[0::3]


full_data = pd.DataFrame(full_data)
full_data = full_data.dropna()

filtered_data = full_data.iloc[0::3]
linux_path = '/home/ansh/'
windows_path = 'C:/news_1/'

os.system('cd ..')
full_data.to_csv(linux_path+'news_aggregator/articles.csv')
filtered_data.to_csv(linux_path+'news_aggregator/filtered.csv')

