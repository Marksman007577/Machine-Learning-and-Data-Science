# creating a dataframe using numpy or manual inputed values
import numpy as np
import pandas as pd

np.random.seed(101)
my_data = np.random.randint(0, 101, (4, 3))

my_row = ['CA', 'NY', 'AZ', 'TX']
my_column = ['JAN', 'FEB', 'MAR']

df = pd.DataFrame(data=my_data, index=my_row, columns=my_column)
print(df)

df.info()
