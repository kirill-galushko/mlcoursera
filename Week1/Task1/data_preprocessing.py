import numpy as np
import pandas
data = pandas.read_csv('../titanic.csv', index_col='PassengerId')


print ("\n1st task")
print data['Sex'].value_counts().values

print ("\n2nd task")
a = data['Survived'].loc[data['Survived'] == 1].value_counts().values
print np.round(np.true_divide(a, len(data))*100,2)

print ("\n3th task")
a = data['Pclass'].loc[data['Pclass'] == 1].value_counts().values
print np.round(np.true_divide(a, len(data))*100,2)

print ("\n4th task")
print np.round(data['Age'].mean(),2)
print np.round(data['Age'].median(),2)

print ("\n5th task")
print np.round(data[['SibSp','Parch']].corr('pearson').values[1,0],2)

print ("\n6th task")
print data['Name'].loc[data['Sex'] == 'female'].str.split('.').str[1].str.split('(').str[-1].str.split(' ').str[1].str.replace('[(,)]','').value_counts().head(1)