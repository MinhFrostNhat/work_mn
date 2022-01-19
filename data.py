import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
a=pd.read_csv("Human_Resources.csv")



a.scartter(x = 'OverTime', y = 'MonthlyIncome')

plt.show()


"""print(a.head(5))
print(a.info())
print(a['Age'].median())"""

"""print(a[a['MonthlyIncome']==a['MonthlyIncome'].max()])
print(a.iloc[a['MonthlyIncome'].idxmax()])
print(a.iloc[a['MonthlyIncome'].idxmin()])"""

"""print(a['JobLevel'].value_counts())"""

"""a['JobLevel']=a['Department'].apply(len)
print(a[['JobLevel','Department']])"""

#print(a[a['JobLevel']==1]['Department'].value_counts())
"""plt.figure(figsize=[60,20])
tc=a.corr()
sns.heatmap(tc,annot=True)
plt.tight_layout()
plt.show()"""

"""sns.countplot(x='Gender',data=a)
plt.show()"""

"""sns.barplot(x='Gender',y='MonthlyIncome',data=a)
plt.show()"""