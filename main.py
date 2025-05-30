# coding for a brighter future 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
#the fun doesnt end
df=pd.read_csv('USA_Housing.csv')
print("\n first 10 not five of the data set you are wrong")
print(df.head(10))
print("\n info about the data set as knowledge is power")
print(df.info())
print("\n the summary statistics of the data set")
print(df.describe())
print("\n column of the data set")
print(df.columns)
df_numeric=df.drop(columns=['Address'])
print("\n generating pair plot")
sns.pairplot(df_numeric)
plt.suptitle('Pair Plot of USA Housing', y=1.02)
plt.show()


      
