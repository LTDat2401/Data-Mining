import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#doc file data
df = pd.read_csv("C:\\Users\\Nhi\\Desktop\\PTDL\\market.csv")


#loc ra tung chi nhanh
cn_a = df.loc[((df['Branch'] == 'A')),['Branch','Product line','Unit price','Quantity','Rating']]
cn_b = df.loc[((df['Branch'] == 'B')),['Branch','Product line','Unit price','Quantity','Rating']]
cn_c = df.loc[((df['Branch'] == 'C')),['Branch','Product line','Unit price','Quantity','Rating']]

Sum_QuantityA = cn_a['Branch'].count()
Sum_QuantityB = cn_b['Branch'].count()
Sum_QuantityC = cn_c['Branch'].count()


print('Tổng số lượng hóa đơn bán ra ở chi nhánh A: ',Sum_QuantityA)
print('Tổng số lượng hóa đơn bán ra ở chi nhánh B: ',Sum_QuantityB)
print('Tổng số lượng hóa đơn bán ra ở chi nhánh C: ',Sum_QuantityC)

list = [Sum_QuantityA,Sum_QuantityB,Sum_QuantityC]
fig, ax = plt.subplots()
ax.bar(['A','B','C'],list)
ax.set(title = "Tổng số lượng hóa đơn tại các chi nhánh", ylabel = "số lượng",xlabel = "chi nhánh")
plt.show()
