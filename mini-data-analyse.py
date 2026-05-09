import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

students = pd.read_csv("students.csv")

print(students.head())

print(students.describe(include="all"))

print(students.math_grade.mean())

print(students.math_grade.median())

print(students.math_grade.mode()[0])

print(students.math_grade.max() - students.math_grade.min())

print(students.math_grade.std())

sns.histplot(x = "math_grade", data = students)
plt.show()
plt.clf()

sns.boxplot(x = "math_grade", data = students)
plt.show()
plt.clf()

print(students.Mjob.value_counts())

print(students.Mjob.value_counts(normalize=True))

sns.countplot(x = "Mjob", data = students)
plt.show()
plt.clf()

students.Mjob.value_counts().plot.pie()
plt.show()
plt.clf()
