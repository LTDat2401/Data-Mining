import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('C:\Python\data mining\market.csv')

# Create a binary target variable based on a threshold (e.g., Rating > 7 means buy)
data['Buy'] = data['Rating'] > 7

# Extract features and binary target variable
X = data[['Unit price', 'Quantity', 'Tax 5%', 'cogs', 'gross margin percentage', 'gross income']]
y = data['Buy']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Support Vector Machine classifier
model = SVC()

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Calculate the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Plot the confusion matrix using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Not Buy', 'Buy'], yticklabels=['Not Buy', 'Buy'])
plt.title('Confusion Matrix SVM')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Calculate the AUC score
auc_score = roc_auc_score(y_test, y_pred)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_output = classification_report(y_test, y_pred)

# Print the results
print(f'Accuracy: {accuracy}')
print('AUC Score:', auc_score)
print('Classification Report:\n', classification_report_output)
print('Confusion Matrix :\n', conf_matrix)
