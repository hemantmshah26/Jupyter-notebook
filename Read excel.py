import pandas as pd
data = pd.read_csv("Test.xlsx", low_memory=False)
print("Total rows: {0}".format(len(data)))
print(list(data))
