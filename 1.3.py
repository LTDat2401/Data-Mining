import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#doc file data
df = pd.read_csv("C:\\Users\\Nhi\\Desktop\\PTDL\\market.csv")

sns.displot(df['Rating'])
plt.axvline(x=np.mean(df['Rating']),c='orange', ls = 'dashed',label='50%')
plt.axvline(x=np.percentile(df['Rating'],25),c= 'green',ls='dashed',label='25%')
plt.axvline(x=np.percentile(df['Rating'],75), c='yellow', ls ='dashed',label='75%')
plt.legend()
plt.show()