# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 09:52:45 2021

@author: yanga
"""


import pandas as pd
import numpy as np

income = pd.read_csv(r"C:\git_repo\python_scratches\income.csv")

income.columns[0:2]

income

income.dtypes

income["State"].dtypes

income.shape

["XXX" + x for x in list(income.Index.unique())]

income.State.nunique()



income.shape

pd.crosstab(income.Index, income.State)

income.Index.value_counts()


income.iloc



x = pd.DataFrame({"var1" : np.arange(1,20,2), "var2": np.arange(1,20,2)}, index=[9,8,7,6,10, 1, 2, 3, 4, 5])
x


x.loc[:3,]
x.iloc[:3,-1]



data = pd.DataFrame({"A" : ["John","Mary","Julia","Kenny","Henry"], "B" : ["Libra","Capricorn","Aries","Scorpio","Aquarius"]})
data 
list(data.columns)



xxx = data.rename(columns={"A":"cus_name"})
data
xxx


income.head()
income.set_index("Index", inplace = True)
income
income.reset_index()

income.drop("Index", axis = 1)
income.drop(range(4))
income

income.sort_values(["Index", "Y2002"])

income["diff1"] = income.eval("Y2008" - "Y2009")

income.head()

income.describe(include = ["object"])





data = pd.DataFrame({"Items" : ["TV","Washing Machine","Mobile","TV","TV","Washing Machine"], "Price" : [10000,50000,20000,10000,10000,40000]})
data


list(data.Items.duplicated())

data[data.Items.duplicated() == False]


iris = pd.read_csv(r"C:\git_repo\python_scratches\iris.csv")

iris["setosa"] = iris.Species == "setosa"
iris.head()

iris["setosa"][iris.setosa == True] = 1
iris["setosa"][iris.setosa == False] = 0

iris.rank()

iris['Rank2'] = iris['Sepal.Length'].groupby(iris["Species"]).rank(ascending=1)
iris.head()
iris.Rank2


iris['Petal.Width'].cumsum()



students = pd.DataFrame({'Names': ['John','Mary','Henry','Augustdus','Kednny'],
                         'Zodiac Signs': ['Aquarius','Libra','Gemini','Pisces','Virgo']})
students2 = pd.DataFrame({'Names': ['John','Mary','Henry','Augustus','Kenny'],
                          'Marks' : [50,81,98,25,35]})

result = pd.merge(students, students2, on='Names', how = "right")  #it only takes intersections



