#!/usr/bin/env python
# coding: utf-8

# In[467]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm
from sklearn import preprocessing
from bioinfokit.analys import stat
import statsmodels.api as sm

def main():

    tree = pd.read_csv("alldatafile/street-trees.csv", sep =";")

    tree = tree[["TREE_ID","NEIGHBOURHOOD_NAME"]]
    tree = tree.groupby(["NEIGHBOURHOOD_NAME"])['TREE_ID'].count().reset_index(name = "Number of Trees")
    tree = tree.sort_values("Number of Trees",ascending=False)
    tree.to_csv("alldatafile/tree.csv")
    # tree

    #cleaning up to use area
    #the areas I am using are an estimate from 2016 data because there is no update on
    #them yet, however I believe, area is not changing a lot through years therefore
    #I believe it is still acceptable to use an old area just for an estimation

    area = pd.ExcelFile("alldatafile/Vancouver_Neighbourhood_Population_1971-2016.xlsx")

    #extracting the population data from 2nd sheet to a df
    area = pd.read_excel(area, sheet_name = '1971-2016 Population')
    area = area.rename(columns={"Unnamed: 0" : "Neighbourhood"})
    area = area[0:22]


    #Subsetting areas
    area1 = area.iloc[:, 22].dropna()
    area1 = area1.apply(int)


    #extracting predicted population data for 2022.
    pop =  pd.read_csv("alldatafile/population2022data.csv")
    pop = pop.iloc[:, [1,2]]
    # pop



    #Subsetting negihborhood
    area = area.iloc[:,0].dropna()
    area = pd.DataFrame({"Neighbourhood" : area})
    # area
    area["Area(ha)"] = area1
    area['Neighbourhood'] = area['Neighbourhood'].str.upper()


    #sorting both datasets according to the neighbourhood areas
    tree = tree.sort_values("NEIGHBOURHOOD_NAME")
    # print(tree)

    area = area.sort_values("Neighbourhood")
    # print(area)



    # Fully processed data for analysis
    area["treeCountsPerArea"] = tree["Number of Trees"]
    area["Population"] = pop["Prediction"]

    area.head()


    # Normalizing the data before doing the analysis
    area1 = area[["Area(ha)","treeCountsPerArea","Population"]]

    d = preprocessing.normalize(area1)

    scaled_area = pd.DataFrame(d, columns= area1.columns)
    scaled_area['Neighbourhood'] = area["Neighbourhood"]


    # ANOVA Test

    #melting the dataset to for anova test
    df_melt = pd.melt(scaled_area, id_vars=['Neighbourhood'],
    value_vars=["Area(ha)", "treeCountsPerArea", "Population"])

    df_melt.columns = ['Neighbourhood', 'treatments', 'value']

    df_melt.head()



    fvalue, pvalue = stats.f_oneway(area['Area(ha)'], area['treeCountsPerArea'], area['Population'])
    # print(fvalue, pvalue)

    # The p-value obtained through ANOVA analysis is significant ( p < 0.005), hence, it is
    # concluable that there are statistically significant differences means among treatments

    from bioinfokit.analys import stat
    res = stat()
    res.anova_stat(df=df_melt, res_var='value', anova_model='value ~ C(treatments)')
    res.anova_summary


    # In[483]:


    # Post-Hoc comparison analysis (since ANOVA's pvalue < 0.05)
    from bioinfokit.analys import stat




    # perform multiple pairwise comparison (Tukey's HSD)
    res = stat()
    res.tukey_hsd(df=df_melt, res_var='value', xfac_var='treatments',
             anova_model='value ~ C(treatments)')
    res.tukey_summary



    # Above result from Tukey's HSD suggests that except Area(ha)-treeCountsPerArea, all other pairwise
    # treatments rejects null hypothesis (p <0.05), inddicating all the statistical significant difference



    # Q-Q plot
    import statsmodels.api as sm
    # res.anova_std_residuals are standardized residuals obtained from ANOVA (check above)

    sm.qqplot(res.anova_std_residuals, line='45')
    plt.xlabel("Theorical Quantiles")
    plt.ylabel('Standardized Residuals')
    # plt.show()
    plt.savefig('alldatafile/QQtree.png')


    #Histogram
    plt.hist(res.anova_model_out.resid, bins='auto', histtype ='bar', ec='k')
    plt.xlabel("Residuals")
    plt.ylabel('Frequency')
    # plt.show()
    plt.savefig('alldatafile/histtree.png')


    # #Shapiro-Wilk test - testing ANOVA Assumptions of normall distribution of residuals
    # from statsmodels.formula.api import ols

    # model = ols('value ~ C(treatments)', data = df_melt).fit()
    # w,pvalue = stats.shapiro(model.resid)
    # print(w, pvalue)


    # #not normally distributed

if __name__ == '__main__':
    main()

