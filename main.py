import numpy as np
import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

print ("\n1st question")
print data['Sex'].value_counts()

print ("\n2nd question")
a = data['Survived'].loc[data['Survived'] == 1].value_counts().values
print np.round(np.true_divide(a, data.__len__())*100,2)

print ("\n3th question")
a = data['Pclass'].loc[data['Pclass'] == 1].value_counts().values
print np.round(np.true_divide(a, data.__len__())*100,2)

print ("\n4th question")
print data['Age'].mean()
print data['Age'].median()

print ("\n5th question")
print data[['SibSp','Parch']].corr('pearson')

print ("\n6th question")
print data['Name'].loc[data['Sex'] == 'female'].str.split('.').str[1].str.split(' ').str[1].str.replace('[(,)]','').value_counts().head(1)