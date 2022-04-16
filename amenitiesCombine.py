import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

def main():
    food = pd.read_csv("alldatafile/foodClean.csv")
    food = food[["name", "neighbourhood"]]
    food = food.groupby(["neighbourhood"])["name"].count().reset_index(name="foodAmenCounts")


    trans = pd.read_csv("alldatafile/transClean.csv")
    trans = trans[["name", "neighbourhood"]]
    trans = trans.groupby(["neighbourhood"])["name"].count().reset_index(name="transAmenCounts")


    ent = pd.read_csv("alldatafile/entClean.csv")
    ent = ent[["name", "neighbourhood"]]
    ent = ent.groupby(["neighbourhood"])["name"].count().reset_index(name="entAmenCounts")


    night = pd.read_csv("alldatafile/nightClean.csv")
    night = night[["name", "neighbourhood"]]
    night = night.groupby(["neighbourhood"])["name"].count().reset_index(name="nightAmenCounts")


    arts = pd.read_csv("alldatafile/artsClean.csv")
    arts = arts[["name", "neighbourhood"]]
    arts = arts[arts["name"].notna()]
    arts = arts.groupby(["neighbourhood"])["name"].count().reset_index(name="artsAmenCounts")


    reli = pd.read_csv("alldatafile/reliClean.csv")
    reli = reli[["name", "neighbourhood"]]
    reli = reli[reli["name"].notna()]
    reli = reli.groupby(["neighbourhood"])["name"].count().reset_index(name="reliAmenCounts")


    amen_data = food.merge(trans, on=["neighbourhood"], how="left")
    amen_data = amen_data.merge(ent, on=["neighbourhood"], how="left")
    amen_data = amen_data.merge(night, on = ["neighbourhood"],how = "left")
    amen_data = amen_data.merge(arts,on = ['neighbourhood'],how = "left")
    amen_data = amen_data.merge(reli, on=['neighbourhood'], how="left")
    amen_data = amen_data.fillna(0)
    amen_data.to_csv("alldatafile/amendataClean.csv")


if __name__ == '__main__':
    main()