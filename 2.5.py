import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#doc file data
df = pd.read_csv("C:\\Users\\Nhi\\Desktop\\PTDL\\market.csv")
cn_a = df.loc[((df['Branch'] == 'C')),['Branch','Product line','Gender','Unit price','Quantity','Rating']]

sns.set()
sns.barplot(data = cn_a,x=cn_a['Quantity'],y=cn_a['Rating'])
plt.ylabel('Rating')
plt.xlabel('Số lượng')
plt.title("Biểu đồ thể hiện số lượng mua hàng và mức rating ở chi nhánh C")

plt.style.use('seaborn-v0_8-dark')
plt.show()