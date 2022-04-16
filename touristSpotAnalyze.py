import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from scipy import stats

def main():
    #chi thetha analysis to find out if the neighbourhood and different amenities are related
    amendata = pd.read_csv("alldatafile/amendataClean.csv")
    amendata = amendata[["entAmenCounts","nightAmenCounts","artsAmenCounts","reliAmenCounts"]]
    entdata = amendata["entAmenCounts"].to_numpy()
    nightdata = amendata["nightAmenCounts"].to_numpy()
    artsdata = amendata["artsAmenCounts"].to_numpy()
    relidata = amendata["reliAmenCounts"].to_numpy()

    contingency = [[entdata],[nightdata],[artsdata],[relidata]]
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    print("This is an analysis of ChiSquare")
    print("The p-value of this analysis is: ", p)
    print("This analysis is done to see if being in different Neighbourhood affects different type of amenities available")
    print("From this analysis, it is known that p value is very small which means it confirms that differnt Neighbourhood affects types of amenities that is available there")
    print("Therefore the conclusion from this analysis is to choose which neighbourhood you wanna stay in because different neighbourhood have different type of tourist attractions!")

if __name__ == '__main__':
        main()