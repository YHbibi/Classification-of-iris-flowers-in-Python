# Import libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()

# Create the decision tree model
tree_clf = DecisionTreeClassifier()

# Train the model on the dataset
tree_clf.fit(iris.data, iris.target)

# Plot the decision tree
plt.figure(figsize=(15,15))
plot_tree(tree_clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()
