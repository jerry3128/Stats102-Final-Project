import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
df['ln_units'] = np.log(df['units'])
features = ['Tree Width', 'Decomposition Overhead Ratio', 'Average Depth', 'Sum of Join node distances', 'Branching Factor', 'Bag Adjacency Factor', 'Bag Connectedness Factor', 'Bag Neighborhood Coverage Factor']

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

def polynomialLinearRegression(df_train, df_predict):
    X = df_train[features]
    y = df_train['units']
    X_predict = df_predict[features]
    y_predict = df_predict['units']
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    predictions = model.predict(poly.fit_transform(X_predict))

    mse = mean_squared_error(y_predict, predictions)
    plt.scatter(X_predict['Tree Width'], y_predict  , color = 'blue'  , alpha = 0.5)
    plt.scatter(X_predict['Tree Width'], predictions, color = 'orange', alpha = 0.5)
    return mse
    # print(f"MSE: {mse / 1e14}")
    # plt.show()
    
mse = 0
for i in range(5):
    l=i*2
    r=l+2
    df_predict = df.groupby('Graph ID', group_keys=False).apply(lambda g: g.iloc[l:r])
    df_train = df.drop(df_predict.index)
    mse += polynomialLinearRegression(df_train, df_predict)

print("mse value: ", mse / 1e14)
# plt.show()
