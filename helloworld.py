import requests
import json
import pandas as pd
import os

response = requests.get('https://corona.lmao.ninja/v2/countries?yesterday&sort').json()                                 #API FOR COUNTRIES
result = requests.get("https://api.rootnet.in/covid19-in/stats/latest").json()                                          #API FOR STATES


                                                # CODE FOR DATAFRAME AND INFROMATION OF COUNTRIES


cases = []
country = []
todayCases = []
deaths = []
todayDeaths = []
recovered = []
todayRecovered = []
active = []
critical = []
tests = []
population = []


for i in response[0:]:
    country.append(i['country'])
    cases.append(i['cases'])
    todayCases.append(i['todayCases'])
    deaths.append(i['deaths'])
    todayDeaths.append(i['todayDeaths'])
    recovered.append(i['recovered'])
    todayRecovered.append(i['todayRecovered'])
    active.append(i['active'])
    critical.append(i['critical'])
    tests.append(i['tests'])
    population.append(i['population'])


d = {"Country":country, "Total Cases" :cases,
     "Today's Case":todayCases,
     "Deaths" :deaths,
     "Today's Deaths" :todayDeaths,
     "Recovered" :recovered,
     "Today's Recovered" :todayRecovered,
     "Active" :active, "Critical" :critical,
     "Tests" :tests,
     "Population" :population}

df = pd.DataFrame(d)
print(df)
print(sum(cases))

path = "C:\\Users\\nisha\\.ipython"
os.chdir(path)                                                                            #CSV FILE FOR COUNTRIES DATA
df.to_csv("Coronavirus PowerBI Raw", sep='\t')


                                                     # CODE FOR DATAFRAME AND INFROMATION OF STATES


Data = result["data"]
Region = Data["regional"]

state = []
Foreign = []
Discharged = []
Deaths = []
totalconfirmed = []

for i in Region[0:]:
     state.append(i["loc"])
     Foreign.append(i["confirmedCasesForeign"])
     Discharged.append(i["discharged"])
     Deaths.append(i["deaths"])
     totalconfirmed.append(i["totalConfirmed"])


dic = {"State":state,
       "Total Cases":totalconfirmed,
       "Recovered":Discharged,
       "Total deaths":Deaths,
       "Foreign Cases":Foreign }

ff = pd.DataFrame(dic)
print(ff)
#print(sum( totalconfirmed))

path = "C:\\Users\\nisha\\.ipython"
os.chdir(path)                                                                          #CSV FILE FOR STATES DATA
ff.to_csv("Coronavirus PowerBI Raw New", sep='\t')


                                                                          #CODE FOR  GRAPHS DATAs



Get=requests.get("https://api.covid19india.org/data.json").json()
graph=Get["cases_time_series"]

Date = []
Dailycon = []
Dailyrec = []
Dailydea = []
Totcon = []
Totrec = []
Totdeac = []

for i in graph[0:]:
    Date.append(i["date"])
    Dailycon.append(i["dailyconfirmed"])
    Dailyrec.append((i["dailyrecovered"]))
    Totcon.append(i["totalconfirmed"])
    Totrec.append(i["totalrecovered"])
    Dailydea.append(i["dailydeceased"])
    Totdeac.append(i["totaldeceased"])

di={"Date" :Date ,
    "Daily confirmed" :Dailycon ,
    "Daily Recovered" :Dailyrec ,
    "Total Confirmed" :Totcon ,
    "Total Recovered" :Totrec ,
    "Daily Deaths" :Dailydea ,
    "Total Deaths" :Totdeac}

ef=pd.DataFrame(di)
print (ef)

path = "C:\\Users\\nisha\\.ipython"
os.chdir(path)                                                                            #CSV FILE FOR Graphs DATA
ef.to_csv("Coronavirus PowerBI Raw Graphs", sep='\t')


