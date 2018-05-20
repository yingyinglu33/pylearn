import pandas as pd
"""
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
"""

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 500)

#1. load the data from infections.csv
data = pd.read_csv("~/PycharmProjects/pylearn/inspections.csv")
#print(data.head())

#2. identify the employees who have given the top 3 and bottom 3 mean scores across all the named programs.

#subset = data[['employee_id', 'score']]
#print(subset.head())
top_mean_score = data.groupby(['employee_id'])['score'].mean().nlargest(3)
print(top_mean_score)
bottom_mean_score = data.groupby(['employee_id'])['score'].mean().nsmallest(3)
print(bottom_mean_score)

#3. Which cities have the highest and lowest mean scores? Which facility has the most locations?
top_city_score = data.groupby(['facility_city'])['score'].mean().nlargest(1)
print(top_city_score)

bottom_city_score = data.groupby(['facility_city'])['score'].mean().nsmallest(1)
print(bottom_city_score)

top_facility = data.groupby(['facility_name'])['facility_id'].count().nlargest(1)
print(top_facility)

"""
4.  which city's annual score is improving the most? And which city is deteriorating the most? 
For missing values, use the average of know values for that city. 
Show the trends in a line graph, by quarter for the lowest and highest cities.
"""