import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv('F:\python work\data2.csv')
print(df)


# Generat a report
profile = profileReport(df)
profile.to_file(output_file="data2.html")