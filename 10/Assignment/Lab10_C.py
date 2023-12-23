import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("epldata_final.csv")
df["age2"] = df["age"] ** 2
df["log_page_views"] = np.log2(df["page_views"])
feature_names = [
    "fpl_points",
    "age",
    "age2",
    "log_page_views",
    "new_signing",
    "big_club",
    "position_cat",
]
X = df[feature_names].to_numpy()
y = df["market_value"].to_numpy()
# df.fillna(0, inplace=True)

df.fillna(method="ffill", inplace=True)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=df["region"]
)

scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

reg = LinearRegression(fit_intercept=True)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

print("\nR^2: \t", reg.score(X_test, y_test))

from sklearn.metrics import mean_squared_error, mean_absolute_error

print("\n mean_squared_error : ", mean_squared_error(y_test, y_pred))
print("\n mean_absolute_error : ", mean_absolute_error(y_test, y_pred))
print("\ncoef: \n", reg.coef_)

print("\ninter: \t", reg.intercept_)

print(f"Coef of age and age^2 is {reg.coef_[1]:.5f} and {reg.coef_[2]:.5f}")
print(f"Coef of log2(page_views) is {reg.coef_[3]:.5f}")
print(f"Coef of big_club is {reg.coef_[5]:.5f}")

from sklearn.model_selection import learning_curve
train_size_abs, train_scores, test_scores = learning_curve( reg, X, y,cv=10 ,train_sizes=[0.1,0.25,0.5,0.75,1] ,scoring='neg_mean_squared_error')
for train_size, train_scores, test_scores in zip(train_size_abs, train_scores, test_scores):
    print(f"{train_size} samples were used to train the model")
    print(f"The average train mse is {-train_scores.mean():.2f}")
    print(f"The average test mse is {-test_scores.mean():.2f}")