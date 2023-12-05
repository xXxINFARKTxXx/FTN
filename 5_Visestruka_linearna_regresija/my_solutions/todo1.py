import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

import line_pretpostavke as line

def are_assumptions_satisfied(model, x, y, p_value_thresh=0.01):
    print(line.linear_assumption(model, x, y,
                                  p_value_thresh=p_value_thresh, plot=False))
    
    print(line.normality_of_errors_assumption(model, x, y,
                                               p_value_thresh=p_value_thresh, plot=False))

    print(line.independence_of_errors_assumption(model, x, y, plot=False))
    
    print(line.equal_variance_assumption(model, x, y,
                                          p_value_thresh=p_value_thresh, plot=False))
    
    print(line.perfect_collinearity_assumption(x, plot=False))
    pass


if __name__ == '__main__':
    df = pd.read_csv("data/housing.csv", sep=',')
    
    x = df.drop(columns="price")
    y = df["price"]

    x_train, x_val, y_train, y_val = train_test_split(x, y, train_size=0.8,
                                                      shuffle=True,
                                                      random_state=51)

    x_train_c = sm.add_constant(x_train)
    model = sm.OLS(y_train,x_train_c).fit()
    y_pred_train = model.predict(x_train_c)

    are_assumptions_satisfied(model, x_train_c, y_train,
                              p_value_thresh=0.01)

    pass