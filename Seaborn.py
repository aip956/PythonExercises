import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = sns.load_dataset('iris')

# Scatter plot with seaborn
# sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)   
# plt.show()


# Scatter plot with Matplotlib
plt.scatter(iris['sepal_length'], iris['sepal_width'])
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.title('Scatter plot of Iris dataset')
plt.show()