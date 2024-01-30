import numpy as np
import pandas as pd

dict = {
    'Age': 23,
    'Education': 'Masters',
    'Salary': 25000
    }
print(dict)

data = np.array([list(dict.values())])
headers = list(dict.keys())
print(data)
print(headers)

df = pd.DataFrame(data, columns=headers)
print(df)