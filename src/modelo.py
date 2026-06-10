from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def treinar_modelo(serie, modelo_nome, t0):

    y = serie.values
    X = np.arange(len(y)).reshape(-1, 1)

    X_train = X[:t0]
    X_test = X[t0:]

    y_train = y[:t0]
    y_test = y[t0:]

    if modelo_nome == "Regressão Linear":
        modelo = LinearRegression()
    else:
        modelo = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

    modelo.fit(X_train, y_train)

    previsao = modelo.predict(X_test)

    mae = mean_absolute_error(y_test, previsao)

    rmse = np.sqrt(
        mean_squared_error(y_test, previsao)
    )

    return y_test, previsao, mae, rmse