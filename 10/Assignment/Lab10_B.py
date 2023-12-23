import numpy as np
import matplotlib.pyplot as plt
def simple_linear_regression_fit(x_train: np.ndarray, y_train: np.ndarray) -> np.ndarray:
    """
    Inputs:
    x_train: a (num observations by 1) array holding the values of the predictor variable
    y_train: a (num observations by 1) array holding the values of the response variable

    Returns:
    beta_vals:  a (num_features by 1) array holding the intercept and slope coeficients
    """
    x_bar = np.mean(x_train)
    y_bar = np.mean(y_train)
    top = 0
    down = 0 
    for i in range(3):
        top += (x_train[i] - x_bar) * (y_train[i] -y_bar)
        down += (x_train[i] - x_bar)**2
    beta_1 = top / down
    beta_0 = y_bar - beta_1 * x_bar
    
    return np.array([beta_0, beta_1])


def main():
    #B-1
    x_train = np.array([[1], [2], [3]])
    y_train = np.array([2, 2, 4])
    plt.scatter(x_train , y_train)
    print('B-1')
    print("Shape of X_train:", x_train.shape)
    print("Shape of y_train:", y_train.shape)
    #B-2
    beta = simple_linear_regression_fit(x_train, y_train)
    print()
    print('B-2')
    print("beta_0:",beta[0])
    print("beta_1", beta[1])
    plt.figure(figsize=(12,8))
    plt.subplot(121)
    plt.scatter(x_train ,y_train)
    plt.title('B-2')
    plt.plot(x_train, beta[0] + beta[1] * x_train ,label ='B-2')
    plt.legend()
    #B-3
    from sklearn.linear_model import LinearRegression
    linear_model = LinearRegression(fit_intercept=True)
    linear_model.fit(x_train,y_train)
    print()
    print('B-3')
    print("Inter(beta0):", linear_model.intercept_)
    print("Coef(beta1):", linear_model.coef_)
    linear_r2 = linear_model.score(x_train, y_train)
    plt.subplot(122)
    plt.scatter(x_train ,y_train)
    plt.title('B-3')
    plt.plot(x_train, linear_model.predict(x_train), c='r' ,label ='B-3, $R^2=%.2f$' % linear_r2)
    plt.xlabel('X_train')
    plt.ylabel('y_train')
    plt.legend()
    plt.show()
    pass


if __name__ == "__main__":
    main()