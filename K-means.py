import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('C:\Python\data mining\market.csv')

# Extract relevant features for clustering
X = data[['Unit price', 'Quantity', 'Tax 5%', 'cogs', 'gross margin percentage', 'gross income']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose the number of clusters (you can adjust this based on your analysis)
num_clusters = 3

# Apply K-means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Print the cluster centers (optional)
print('Cluster Centers:')
print(scaler.inverse_transform(kmeans.cluster_centers_))

# Visualize the clustering (2D plot for simplicity)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=data['Cluster'], cmap='viridis')
plt.title('K-means Clustering')
plt.xlabel('Scaled Unit Price')
plt.ylabel('Scaled Quantity')
plt.show()
