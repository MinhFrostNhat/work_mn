import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic=sns.load_dataset('titanic')


#sns.jointplot(x='fare',y='age',data=titanic)

#sns.distplot(titanic['fare'],kde=False,color='red')

#sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')

#sns.swarmplot(x='class',y='age',data=titanic)

#sns.countplot(x='sex',data=titanic)

"""a=titanic.corr()
sns.heatmap(a,cmap='cool')"""

g=sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
plt.tight_layout()






plt.show()