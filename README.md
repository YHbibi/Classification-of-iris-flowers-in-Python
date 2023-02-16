# Classification of iris flowers in Python

---

# Description 

This program uses the popular scikit-learn library to load the Iris dataset and train a decision tree model. 
It then visualizes the decision tree using the graphviz library
The tree shows the rules that the model uses to classify the different types of Iris flowers. 

---

## Load the data

First, we’ve imported some necessary packages for the project.
Next, we load the iris dataset from scikit-learn's built-in datasets.

---

## Model training 

We then create a `DecisionTreeClassifier` object and train it on the entire dataset using the `fit` method. 
Next, we use the `plot_tree` function from scikit-learn's `tree` module to generate a graph object representing the decision tree. 
We set the `feature_names` and `class_names` arguments to the corresponding feature and class names in the iris dataset. 
We also set `filled=True` to color the nodes according to their class distribution. 

---

## Visualize the dataset

Finally, we use matplotlib to display the graph on the screen.
The graph can help us to understand how the model works and to communicate our results to others.


