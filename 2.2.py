import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#doc file data
df = pd.read_csv("C:\\Users\\Nhi\\Desktop\\PTDL\\market.csv")
cn_a = df.loc[((df['Branch'] == 'C')),['Branch','Product line','Gender','Unit price','Quantity','Rating']]

sns.boxplot(data=cn_a,x='Product line',y= 'Rating', hue="Gender",palette='tab10')
plt.title('Biểu đồ về mức cho điểm rating ở nam và nữ trên từng dòng sản phẩm')
plt.legend()
plt.show()