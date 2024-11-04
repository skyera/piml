import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/refs/heads/master/iris.csv"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pd.read_csv(url, names=names)

print("dataset dimensions: ", dataset.shape)
print("Head of dataset:")
print(dataset.head(20))

print("Statistics of dataset:")
print(dataset.describe())

print("Class distribution of dataset:")
print(dataset.groupby("class").size())

dataset.plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.show()


dataset.hist()
plt.show()

scatter_matrix(dataset)
plt.show()
