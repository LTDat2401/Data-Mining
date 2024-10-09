import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#doc file data
df = pd.read_csv("C:\\Users\\Nhi\\Desktop\\PTDL\\market.csv")
cn_a = df.loc[((df['Branch'] == 'C')),['Branch','Product line','Gender','Unit price','Quantity','Rating']]

sns.boxplot(data=cn_a,x='Product line',y= 'Quantity', hue="Gender",palette='tab20b')
plt.title("Biểu đồ thể hiện mức mua hàng ở nam và nữ trên từng dòng sản phẩm ở chi nhánh C")
plt.legend()
plt.show()