# %%
import pandas as pd

# %%
def load_dataset():
    url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
    dataset = pd.read_csv(url, header=None)
    dataset.columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    return dataset

# %%
def summarize_dataset(dataset):
    # Print dataset dimensions
    print("\nDataset shape: ")
    print(dataset.shape)

    # Print first 20 rows
    print("\nFirst 20 rows: ")
    print(dataset.head(20))

    # Statistical summary
    print("\nStatistical summary: ")
    print(dataset.describe())

    # Class distribution
    print("\nClass distribution: ")
    print(dataset.groupby('class').size())



# %%
dataset = load_dataset()
summarize_dataset(dataset)

# %% [markdown]
# # Visualization

# %%
# Univariate Plots
from pandas import read_csv
import matplotlib.pyplot as plt

def print_plot_univariate(dataaset):
    dataset.hist()
    plt.show()

print_plot_univariate(dataset)

# %% [markdown]
# # Multivariate Plots

# %%
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

def print_plot_multivariate(dataset):
    scatter_matrix(dataset)
    plt.show()

print_plot_multivariate(dataset)

# %% [markdown]
# # Part 4: Model Training and Testing

# %%
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC

def my_print_and_test_models(dataset):
    array = dataset.values
    X = array[:, 0:4]
    y = array[:, 4]

    # Split dataset into training and validation sets
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.2, random_state=1)

    # Prepare models
    models = []
    models.append(('DecisionTree', DecisionTreeClassifier()))
    models.append(('GaussianNB', GaussianNB()))
    models.append(('KNeighbors', KNeighborsClassifier()))
    models.append(('LogisticRegression', LogisticRegression(solver='liblinear')))
    models.append(('LinearDiscriminant', LinearDiscriminantAnalysis()))
    models.append(('SVM', SVC(gamma='auto')))

    # Evaluate each model
    for name, model in models:
        kfold = KFold(n_splits=10, random_state=1, shuffle=True)
        cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
        print(f'{name}: {cv_results.mean():.6f} ({cv_results.std():.6f})')

my_print_and_test_models(dataset)



# %%



