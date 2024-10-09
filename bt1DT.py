import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('C:\Python\data mining\market.csv')

# Create a binary target variable based on a threshold (e.g., Rating > 7 means buy)
data['Buy'] = data['Rating'] > 7

# Trích xuất đặc trưng và biến mục tiêu nhị phân
X = data[['Unit price', 'Quantity', 'Tax 5%', 'cogs', 'gross margin percentage', 'gross income']]
y = data['Buy']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree classifier
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the AUC score
auc_score = roc_auc_score(y_test, y_pred)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_output = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Print the results
print(f'Accuracy: {accuracy}')
print('AUC Score:', auc_score)
print('Classification Report:\n', classification_report_output)
print('Confusion Matrix:\n', conf_matrix)
# Lấy chiều sâu của cây quyết định
tree_depth = model.tree_.max_depth
print(f"Chiều sâu của cây quyết định: {tree_depth}")

# Visualize the confusion matrix as a heatmap using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Not Buy', 'Buy'], yticklabels=['Not Buy', 'Buy'])
plt.title('Confusion Matrix Decision Tree')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Visualize the decision tree (optional)
plt.figure(figsize=(12, 8))
tree.plot_tree(model, feature_names=X.columns, class_names=['Not Buy', 'Buy'], filled=True, rounded=True)
plt.show()
