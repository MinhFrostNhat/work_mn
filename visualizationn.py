import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




df1=pd.read_csv('df1.csv',index_col=0)
df2=pd.read_csv('df2.csv')
df3=pd.read_csv('df3.csv')


#part 1
#df1['A'].hist(bins=30)

#df2.plot.area(alpha=0.4)

#df2.plot.bar(stacked=True)

#df1.plot.scatter(x='A',y='B',color='black')

#df2.plot.box()

#df1.plot.hexbin(x='A',y='B',cmap='cool',gridsize=20)

#df1['A'].plot.kde()

#df1.plot.density()

#df1['A'].plot.line(x=df1.index,y='B')
#plt.show()

# part 2

#print(df3.head())

#df3.plot.scatter(x='a',y='b',color='red')

#df3['a'].plot.hist()

#df3['a'].plot.hist(bins=30)

#df3[['a','b']].plot.box()

#df3['c'].plot.kde()

df3.head(30).plot.area(alpha=0.5)





plt.show()













