import numpy as np
import pandas as pds
import matplotlib.pyplot as plt

plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})

x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
y = np.random.randint(low=0, high=100, size=8)

#For Horizontal Bar change plt.bar(x,y) to plt.barh(x,y) and exchange the label name each other.
plt.barh(x, y)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Categories Bar Plot')
plt.show()
