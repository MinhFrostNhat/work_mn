import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips= sns.load_dataset('tips')
fight=sns.load_dataset('flights')
iris=sns.load_dataset('iris')
#sns.distplot(tips['total_bill'],kde=False,bins=20)

#sns.jointplot(x='total_bill',y='tip',data=tips)
#sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')

"""sns.pairplot(tips)
sns.pairplot(tips,hue='sex',palette='cool')"""

"sns.rugplot(tips['total_bill'])"


"""sns.barplot(x='sex',y='total_bill',data=tips)
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
"""

#sns.countplot(x='sex',data=tips)

#sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')


#sns.violinplot(x='day',y='total_bill',data=tips)

#heatmap
"""ft=fight.pivot_table(index='month',columns='year',values='passengers')
#sns.heatmap(ft,cmap='cool',linecolor='black',linewidths=1)

sns.clustermap(ft,cmap='cool',standard_scale=1)
"""

"""
# regression plots

#sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',scatter_kws={'s':10})
#sns.lmplot(x='total_bill',y='tip',data=tips)

#sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')

sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex')

plt.tight_layout()
"""

# Grids
#sns.pairplot(iris)

"""girdd=sns.PairGrid(iris)
#girdd.map(plt.scatter)
girdd.map_diag(sns.distplot)
girdd.map_upper(plt.scatter)
girdd.map_lower(sns.kdeplot)"""

"""gridd=sns.FacetGrid(data=tips,col='time',row='smoker')
gridd.map(sns.distplot,'total_bill')
plt.show()"""

# style and color
"""sns.set_style('dark')
sns.countplot(x='sex',data=tips)
sns.despine(bottom=True)
plt.show()"""


"""sns.set_context('notebook')
plt.figure(figsize=([12,5]))
sns.countplot(x='sex',data=tips,palette='hot')
plt.show()"""


"""sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')
plt.show()"""



































































