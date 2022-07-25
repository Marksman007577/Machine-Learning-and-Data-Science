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
