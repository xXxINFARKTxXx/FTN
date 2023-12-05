import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

from todo1 import are_assumptions_satisfied

def get_rsquared_adj(model, x, y):
    num_attributes = x.shape[1]
    y_pred = model.predict(sm.add_constant(x, has_constant='add'))

    from sklearn.metrics import r2_score
    r_squared = r2_score(y, y_pred)
    n = len(y_pred)
    p = num_attributes
    adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
    return adjusted_r_squared

def get_fitted_model(x, y):
    x_with_const = sm.add_constant(x, has_constant='add')
    model = sm.OLS(y, x_with_const).fit()
    return model

if __name__ == '__main__':
    alpha = 0.01
    df = pd.read_csv("data/housing.csv", sep=',')
    
    x = df.drop(columns="price")
    y = df["price"]

    x_train, x_val, y_train, y_val = train_test_split(x, y, train_size=0.9,
                                                      shuffle=True,
                                                      random_state=42)

    x_train_c = sm.add_constant(x_train)
    model = sm.OLS(y_train, x_train_c).fit()

    columns_list = x_train_c.columns.tolist()
    i = 0
    while ( i < len(columns_list) ):
        elem = columns_list[i]
        if alpha <= model.pvalues[elem]:
            x_train_c = x_train_c.drop(columns=elem)
            model = sm.OLS(y_train, x_train_c).fit()
            columns_list = x_train_c.columns.tolist()
            i = 0
            continue
        i += 1

    print(model.summary())
    are_assumptions_satisfied(model, x_train_c, y_train, alpha)
    
    ## privet vovanu
    pass