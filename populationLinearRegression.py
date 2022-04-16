import pandas  as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

def main():
    #Reading data
    data = pd.read_csv("alldatafile/vanpopdata.csv")

    data = data.loc[24:33]
    places = ["Arbutus Ridge","Downtown","Dunbar-Southlands","Fairview","Grandview-Woodland",
              "Hastings-Sunrise","Kensington-Cedar Cottage","Kerrisdale","Killarney",
              "Kitsilano","Marpole","Mount Pleasant","Oakridge","Renfrew-Collingwood",
              "Riley Park","Shaughnessy","South Cambie","Strathcona","Sunset","Victoria-Fraserview",
              "West End","West Point Grey"]
    data = data.astype(int)
    data.columns = ["Neighbourhood","Arbutus Ridge","Downtown","Dunbar-Southlands","Fairview","Grandview-Woodland",
              "Hastings-Sunrise","Kensington-Cedar Cottage","Kerrisdale","Killarney",
              "Kitsilano","Marpole","Mount Pleasant","Oakridge","Renfrew-Collingwood",
              "Riley Park","Shaughnessy","South Cambie","Strathcona","Sunset","Victoria-Fraserview",
              "West End","West Point Grey"]
    data = data.astype(int)
    data

    X = data.iloc[:,0].values.reshape(-1,1)
    y = data.iloc[:,1].values.reshape(-1,1)
    model = LinearRegression()
    model.fit(X,y)

    X_fit = [[2022]]
    y_fit = model.predict(X_fit)

    pop2022 = []
    for i in range(22):
        X = data.iloc[:,0].values.reshape(-1,1)
        y = data.iloc[:,i+1].values.reshape(-1,1)
        model = LinearRegression()
        model.fit(X,y)
        X_fit = [[2022]]
        y_fit = model.predict(X_fit)
        pop2022.append(y_fit)

    new = []
    for i in range(len(pop2022)):
        new.append(pop2022[i][0][0])


    pop2022 = pd.DataFrame({"Neighbourhood":places,"Prediction":new})
    pop2022.to_csv("alldatafile/population2022data.csv")

if __name__ == '__main__':
    main()
