import numpy as np
from sklearn.linear_model import LinearRegression

def calculations(received_data):
    x = np.array(received_data["x"]).reshape(-1, 1)
    y = np.array(received_data["y"])

    model = LinearRegression()
    model.fit(x, y)

    processed_data = {
        "Alpha": model.coef_[0],
        "Beta": model.intercept_
    }

    return processed_data
