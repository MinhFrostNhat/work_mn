import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""x=np.linspace(0,5,11)
y=x**2"""
"""plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()"""

""""# Sub plot 1
plt.subplot(1,2,1)
plt.plot(x,y,'black')

# sub plot 2

plt.subplot(1,2,2)
plt.plot(y,x,'red')
plt.show()"""

# function
"""fig=plt.figure()
axes= fig.add_axes([0.1,0.1,0.7,0.7])
axes.plot(x,y)
axes.set_xlabel('x')
axes.set_ylabel('y')
plt.show()"""

"""fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes1=fig.add_axes([0.2,0.5,0.4,0.3])
axes.plot(x,y)
axes1.plot(y,x)
plt.show()"""



#Matplot lib p2

"""fig,axes=plt.subplots()
axes.plot(x,y)"""
#fig,axes=plt.subplots(nrows=1,ncols=2)
"""axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()"""
"""for i in axes:
    i.plot(x,y)
plt.show()"""

"""fig=plt.figure(figsize=(8,2))
ax=fig.add_axes([0.1,0.1,1,1])
ax.plot(x,y)
plt.show()"""

"""fig=plt.figure()
ax=fig.add_axes([0.2,0.2,0.5,0.5])
ax.plot(x,y)
ax.plot(y,x)
plt.show()"""

# matplot p3

"""fig=plt.figure()
ax=fig.add_axes([0.2,0.2,0.5,0.5])
ax.plot(x,y,'green',linewidth=2)
plt.show()"""

# example

x=np.arange(0,100)
y=x*2
z=x**2

"""fig=plt.figure()
ax=fig.add_axes([0.2,0.2,0.5,0.5])
ax.plot(x,y)
ax.plot(y,z)
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_title('Title')
plt.show()"""

"""fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.9,0.9])
ax1=fig.add_axes([0.2,0.5,0.2,0.2])
ax.plot(x,z)
ax1.plot(x,y)
ax1.set_xlabel('X')
ax1.set_ylabel('y')
ax1.set_xlim([20,30])
ax1.set_ylim([20,50])
plt.show()"""

fig,axes=plt.subplots(ncols=2,nrows=1)

axes[0].plot(x,y,'blue',ls='--')
axes[1].plot(x,z,'red')
plt.tight_layout()
plt.show()













































































