import numpy as np
import pandas as pd

np.random.seed(101)
my_data = np.random.randint(0, 100, (4, 3))
#print(my_data)

my_row = ["CA", "NY", "AZ", "TX"]
my_column = ["JAN", "FEB", "MAR"]

df = pd.DataFrame(data=my_data, index=my_row, columns=my_column)
print(df)