import numpy as np
import pandas as pd
# pandas series from a list
my_index = ["USA", "Canada", "Mexico"]
my_data = [1776, 1867, 1821]

my_ser = pd.Series(data=my_data, index=my_index)

print(my_ser)

#pandas series from a dictionary
ages = {"Sam": 5, "Frank": 10, "Spike": 7}
my_serr = pd.Series(ages)
print(my_serr)

#Adding two series in pandas
Q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
Q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}

sales_Q1 = pd.Series(Q1)
sales_Q2 = pd.Series(Q2)

total_sale = sales_Q1.add(sales_Q2, fill_value=0)
print(total_sale)
