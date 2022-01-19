import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chart_studio as cs
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()

# DATA
df=pd.DataFrame(np.random.randn(100,4),columns='a b c d'.split())

df2=pd.DataFrame({'category':['A','B','C'],'value':[10,20,30]})

df.iplot()
plt.show()























