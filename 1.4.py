import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#doc file data
df = pd.read_csv("C:\\Users\\Nhi\\Desktop\\PTDL\\market.csv")

plt.figure(figsize=(10,6))
plt.style.use('classic')
ax= sns.boxenplot(x = df['Quantity'],y= df['Product line'])
ax.set_title(label= 'Biểu đồ phân bố số lượng bán ở các dòng sản phẩm', fontsize='16')
ax.set_xlabel(xlabel = "Số lượng bán",fontsize = 16)
ax.set_ylabel(ylabel = "Dòng sản phẩm", fontsize = 16)
plt.show()