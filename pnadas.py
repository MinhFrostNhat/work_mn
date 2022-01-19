import numpy as np
import pandas as pd

labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}

print(pd.Series(data=my_data,index=labels))
#print(pd.Series(my_data,labels))
#print(pd.Series(d))
#print(pd.Series(labels))

ser1=pd.Series([1,2,4,5],['chien','chip','trau','berry'])
ser2=pd.Series([7,8,9,10],['laura','den','trung','berry'])
"""
print(ser1)
print(ser1['berry'])
print(ser1[3])
print(ser1+ser2)
"""


# DATAFRAMES
from numpy.random import randn

np.random.seed(101)
df=pd.DataFrame(randn(5,3),['A','b','c','D','E'],[1,2,3])
#print(df)
#print(df[1])
#print(df[[1,2]])
"""df['E']=df[1]+df[3]
print(df)

df.drop('E',axis=1,inplace=True)
print(df)"""

# ROWS

"""print(df.loc['A'])
print(df.iloc[1])"""

#print(df.loc['A',2])

# compare
"""boolldf=df>0
print(df[boolldf])
print(df[df>0])"""

"""print(df[2]>0)
print(df[df[2]>0])
print(df[df[2]<0])"""

"""ass=df[(df[1]>1) & (df[2]>0)]
print(ass)"""

#print(df.reset_index())

"""newind='CA NY WY OR CO'.split()
df['states']=newind
print(df)
print(df.set_index('states'))"""
"""
outside=['FNC','FNC','FNC','G2','G2','G2']
inside=[1,2,3,3,2,1]
hier_index=list(zip(outside,inside))
print(hier_index)

hier_index=pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

dff=pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(dff)

print(dff.loc['FNC'])
print(dff.loc['FNC'].loc[1])

dff.index.names=['TEAM','GROUP']
print(dff)"""


# MISSING DATA

"""d={'A':[1,2,np.nan],'B':[4,np.nan,np.nan],'C':[1,2,3]}
dio=pd.DataFrame(d)
print(dio)

print(dio.dropna())
print(dio.dropna(axis=1))
print(dio.dropna(thresh=2))"""

"""dio1=dio.fillna(value="alo")
print(dio1)

dio1=dio['A'].fillna(value=dio['C'].median())
print(dio1)"""

# GROUP BY
"""
data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Peson':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],'Sales':[200,100,350,125,246,300]}
dio=pd.DataFrame(data)
print(dio)

bycom=dio.groupby('Company')
print(bycom.sum())
print(bycom.mean())
print(bycom.median())
print(bycom.max())
print(bycom.sum().loc['GOOG'])

print(bycom.describe())
"""












