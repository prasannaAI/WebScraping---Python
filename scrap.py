from bs4 import BeautifulSoup
import requests
import pandas as pd

url ='https://www.worldometers.info/coronavirus/#countries'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

rows= soup.find('table', {'id':"main_table_countries_today"},).find('tbody').find_all('tr')



countries_list = []

for row in rows:
    dic = {}
    dic['Country_Name'] = row.find_all('td')[1].text
    dic['Country_Total_Cases'] = row.find_all('td')[2].text
    dic['Country_Total_Deaths'] = row.find_all('td')[4].text.replace(" ", "")
    dic['Country_Total_Recovered'] = row.find_all('td')[6].text


    countries_list.append(dic)
    

countries_list = countries_list[8:18]

df = pd.DataFrame(countries_list)
df.to_csv('Task.csv', index=False)









