import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv('../titanic.csv', index_col='PassengerId')

print ("\n1st task")
data['Sex'] = pd.factorize(data['Sex'])[0]
prepared_data = data[np.isnan(data['Age']) == False]
X = prepared_data[['Pclass', 'Fare', 'Age', 'Sex']]
Y = prepared_data['Survived']
clf = DecisionTreeClassifier(random_state = 241)
clf.fit(X,Y)
print clf.feature_importances_
