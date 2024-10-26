# Overview
"Open The Iris" is a data science project focused on an end-to-end analysis of the classic Iris dataset, a staple in machine learning and data science. This project performs tasks such as data loading, summarization, visualization, model evaluation, and prediction, with the goal of classifying iris plants into three species based on their physical characteristics.

## Features
- Data Loading: Load the Iris dataset from an external source.
- Data Summarization: Display the dataset’s dimensions, a preview of the data, statistical summary, and class distribution.
- Data Visualization: Visualize data distributions with univariate (histogram) and multivariate (scatter matrix) plots.
- Model Evaluation: Train and evaluate multiple machine learning models, including Decision Trees, Gaussian Naive Bayes, K-Nearest Neighbors, Logistic Regression, Linear Discriminant Analysis, and Support Vector Machines.
- Prediction: Use the best model to predict the class of iris plants based on their features.
## Technologies Used
- Python
- upyter Notebook or Jupyter Lab
- Pandas for data manipulation
- Matplotlib for data visualization
- Scikit-learn for machine learning model evaluation

## Setup and Installation
Clone the repository:
- In the terminal:

``` 
git clone git@git.us.qwasar.io:my_open_the_iris_174705_ij4vhc/my_open_the_iris.git

cd my_open_the_iris
```

Ensure you have the following Python libraries installed:
- Pandas
- Matplotlib
- Scikit-learn

Open the my_open_the_iris.ipynb file in Jupyter Notebook or Jupyter Lab:

```
jupyter notebook my_open_the_iris.ipynb
```

## Project Structure
- my_open_the_iris.ipynb: The main notebook containing all functions and analysis steps for loading, summarizing, visualizing, and modeling the Iris dataset.
- README.md: Project overview and instructions (this file).

## Usage
The project is organized into functions for each step:

- Data Loading: load_dataset() loads the Iris dataset.
- Data Summarization: summarize_dataset(dataset) provides basic information and statistics.
- Data Visualization:
  - print_plot_univariate(dataset): Displays univariate histograms for each attribute.
  - print_plot_multivariate(dataset): Displays a scatter matrix to show relationships between attributes.
- Model Evaluation: my_print_and_test_models(dataset) trains and evaluates six machine learning models, outputting accuracy and consistency metrics for each.

## Example Output
```
DecisionTree: 0.958333 (0.041667)
GaussianNB: 0.950000 (0.040825)
KNeighbors: 0.958333 (0.041667)
LogisticRegression: 0.933333 (0.089753)
LinearDiscriminant: 0.975000 (0.038188)
SVM: 0.983333 (0.033333)
```





Notes:
jupyter notebooks

pip install jupyterlab

Open it in the browser:
jupyter notebook

Based on cells
+ to add a cell
Markdown type
Code cell with python
Import cell

Open jupyter lab in the browser
jupyter lab