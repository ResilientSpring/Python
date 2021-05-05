try:
    import xgboost
except ImportError as ex:
    print("Error: the xgboost library is not installed.")
    xgboost = None


if xgboost is not None:

    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error

    np.random.seed(42)
    X = np.random.rand(100, 1) - 0.5
    y = 3*X[:, 0]**2 + 0.05 * np.random.randn(100)

    X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=49)

    xgb_reg = xgboost.XGBRegressor(random_state=42)
    xgb_reg.fit(X=X_train, y=y_train)
    y_prediction = xgb_reg.predict(X=X_val)
    val_error = mean_squared_error(y_true=y_val, y_pred=y_prediction)
    print("Validation MSE: ", val_error)

    xgb_reg.fit(X=X_train, y=y_train, eval_set=[(X_val, y_val)], early_stopping_rounds=2)

    y_prediction2 = xgb_reg.predict(X=X_val)
    val_error = mean_squared_error(y_true=y_val, y_pred=y_prediction2)
    print("Validation MSE: ", val_error)
