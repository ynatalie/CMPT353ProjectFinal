import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn

def main():

    places = ["Arbutus Ridge","Downtown","Dunbar-Southlands","Fairview","Grandview-Woodland",
              "Hastings-Sunrise","Kensington-Cedar Cottage","Kerrisdale","Killarney",
              "Kitsilano","Marpole","Mount Pleasant","Oakridge","Renfrew-Collingwood",
              "Riley Park","Shaughnessy","South Cambie","Strathcona","Sunset","Victoria-Fraserview",
              "West End","West Point Grey"]

    data = pd.read_csv("alldatafile/crimedata2022.csv")
    crimeCount = data.groupby(["NEIGHBOURHOOD","YEAR","MONTH"]).count().reset_index()
    crimeCount = crimeCount[["NEIGHBOURHOOD","YEAR","MONTH","TYPE"]]
    crimeCount["crimeCount"] = crimeCount["TYPE"]
    crimeCount = crimeCount[["NEIGHBOURHOOD","MONTH","crimeCount"]]
    crimeCount ['NEIGHBOURHOOD'] = crimeCount['NEIGHBOURHOOD'].str.replace("Central Business District", "Downtown")

    pop = pd.read_csv("alldatafile/population2022data.csv")
    pop = pop[["Neighbourhood","Prediction"]]
    pop.columns = ["NEIGHBOURHOOD","Population"]

    mergedata = crimeCount.merge(pop,on = "NEIGHBOURHOOD",how = "left")
    mergedata["crimerates"] = mergedata["crimeCount"]/mergedata["Population"]
    mergedata = mergedata[["NEIGHBOURHOOD","MONTH","crimerates"]]
    mergedata = mergedata[mergedata["crimerates"].notna()]
    mergedata.to_csv("alldatafile/crimeRateData.csv")
    new = mergedata.pivot("NEIGHBOURHOOD","MONTH","crimerates")
    fig = seaborn.heatmap(new, xticklabels=True, yticklabels=True)
    plt.show()

if __name__ == '__main__':
    main()