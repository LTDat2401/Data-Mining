import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#doc file data
df = pd.read_csv("C:\\Users\\Nhi\\Desktop\\PTDL\\market.csv")

sns.boxplot(x=df['Gender'],y= df['Quantity'])
plt.legend()
plt.show()