import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

#### LOAD DATA ####
data = pd.read_csv('Resources/Monatsabrechnung_neu.csv',sep =';')
data = data[['date','balance']]
print('-'*30);print('HEAD');print('-'*30)
print(data.head())

#### PREPARE DATA ####
print('-'*30);print('PREPARE DATA');print('-'*30)
#x = np.array(data['date']).reshape(-1, 1)
y = np.array(data['balance']).reshape(-1, 1)
x = np.arange(y.shape[0]).reshape(-1, 1)
#print(y[:5])
plt.plot(y,'-m')
#plt.show()
polyFeat = PolynomialFeatures(degree=1)
x = polyFeat.fit_transform(x)
#print(x)

#### TRAINING DATA ####
print('-'*30);print('TRAINING DATA');print('-'*30)
model = linear_model.LinearRegression()
model.fit(x,y)
accuracy = model.score(x,y)
print(f'Accuracy:{round(accuracy*100,3)} %')
y0 = model.predict(x)

#### PREDICTION ####
month = 33
print('-'*30);print('PREDICTION');print('-'*30)
print(f'Prediction - Balance after {month} month:',end='')
print(round(int(model.predict(polyFeat.fit_transform([[y.shape[0]+month]])))/1,2),'Euro')

x1 = np.array(list(range(1,y.shape[0]+month))).reshape(-1,1)
y1 = model.predict(polyFeat.fit_transform(x1))
plt.plot(y1,'--r')
plt.plot(y0,'--b')
plt.show()

#forecast: 27.08.20
#month = 33 ==> May 2023
#degree=1 ==> Prediction - Balance after 33 month:230080.0 Euro ==> more realistic than 2nd order :-)
#degree=2 ==> Prediction - Balance after 33 month:369556.0 Euro