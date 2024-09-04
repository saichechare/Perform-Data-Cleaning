import pandas as pd
data = pd.read_csv("Employees.csv")

# find the duplicated value
print(data.duplicated())

#find the missing value
print(data.isnull())

# there is no missing value and not a null value