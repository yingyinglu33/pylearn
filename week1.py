"""
    demonstrate the use of Python for "spreadsheeting"
    needs:
    pip install pandas
    pip install matplotib
    or Jupyter

"""

import pylab as mp
import pandas as pd

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 500)

data = pd.read_csv("emps.csv")
print(data.head())

subset = data[["Employee #", "Salary", "Income"]]
print(subset.head())

sorted = subset.sort_values(by=["Salary"])
print(sorted.head())

# uncomment following in Jupyter
#mp.plot(sorted)