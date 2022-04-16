import crimeHeatmap
import touristSpotAnalyze
import requests
import json
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

name = input("What is your name? ^_^ : ")
print("\n")
print("Hello " + name + " welcome to our Vancouver Neighbourhood tour planning helper")
print("\n")
print("I will be providing you with data to help you plan with your tour around Vancouver Neighbourhood!")
print("\n")
print("First I will provide you with a weather forecasting. This data is cited from a website.")
print("\n")
print("Here you go, below shown are today weather with prediction so you can plan your tour accordingly!")
print("\n")

input("Press enter")
#we are using a guide that we got from website on how to scrap from wttr.in
#we don't take any credit for this, just to make the program fun and better
city = 'vancouver'
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)
print(res.text)
print("\n")

#showing crime rates
input("Press enter")
print("\n")
print("Now that we know the weather, let's start planning!")
print("\n")
print("I believe safety is important when visiting an area, here I provide you with a crime rate heat map per month in 2022")
print("\n")
input("Press enter")
crimeHeatmap.main()
input("Press enter")

print("Next here is a list of neighbourhood with the most trees if you do enjoy nature")
print("\n")
print(pd.read_csv("alldatafile/tree.csv"))
print("\n")
input("Press enter")
print("\n")
print("Here are a full list of different amenity total in every neighbourhood type I prepared for you:")
print("\n")
print(pd.read_csv("alldatafile/amendataClean.csv"))
print("\n")
input("Press enter")

print("Lastly an interesting statistics facts: ")
print("\n")
touristSpotAnalyze.main()
print("\n")

print("Thank you! I hope this helps for you to decide which Vancouver Neighbourhood you wanna go and have a safe trip!")










