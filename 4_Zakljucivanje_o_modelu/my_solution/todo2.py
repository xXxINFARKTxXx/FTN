import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sb

import line_pretpostavke as line

import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    df = pd.read_csv('data/skincancer.csv')

    ## TASK1
    x = df['Lat']
    y = df['Mort']

    alpha = 0.05
    
    x_c = sm.add_constant(x)
    model = sm.OLS(y,x_c).fit()
    y_pred = model.predict(x_c)

    sb.scatterplot(data=df, x='Lat', y='Mort')
    plt.plot(x, y_pred)

    pred_int = model.get_prediction(x_c).summary_frame(alpha)
    plt.fill_between(df['Lat'],
                    pred_int['obs_ci_lower'],
                    pred_int['obs_ci_upper'],
                    color='b', alpha=.1)


    ns_lat = 45.2396
    ns_lat_c = sm.add_constant([0, ns_lat])
    min_max_ns_pred = model.get_prediction(ns_lat_c).summary_frame(alpha)

    min_max_ns_mean = min_max_ns_pred['mean'][1]
    min_max_ns_lower = min_max_ns_pred['obs_ci_lower'][1]
    min_max_ns_upper = min_max_ns_pred['obs_ci_upper'][1]

    plt.plot(ns_lat, min_max_ns_mean, '.')
    plt.plot(ns_lat, min_max_ns_lower, '.')
    plt.plot(ns_lat, min_max_ns_upper, '.')

    plt.show()

    ## TASK2

    print('(T-Test):', line.linear_assumption(model, x_c, y))
    print('(DW-Test):', line.independence_of_errors_assumption(model, x_c, y))
    print('(AD-Test):', line.normality_of_errors_assumption(model, x_c,y))
    print('(GQ-Test):', line.equal_variance_assumption(model, x_c, y))

    ## TASK3

    x_c = sm.add_constant(x)
    model = sm.OLS(y,x_c).fit()
    y_pred = model.predict(x_c)

    sb.scatterplot(data=df, x='Lat', y='Mort')
    plt.plot(x, y_pred)

    pred_int = model.get_prediction(x_c).summary_frame(alpha)
    plt.fill_between(df['Lat'],
                    pred_int['obs_ci_lower'],
                    pred_int['obs_ci_upper'],
                    color='b', alpha=.1)


    ns_lat = 90
    ns_lat_c = sm.add_constant([0, ns_lat])
    min_max_ns_pred = model.get_prediction(ns_lat_c).summary_frame(alpha)

    min_max_ns_mean = min_max_ns_pred['mean'][1]
    min_max_ns_lower = min_max_ns_pred['obs_ci_lower'][1]
    min_max_ns_upper = min_max_ns_pred['obs_ci_upper'][1]

    plt.plot(ns_lat, min_max_ns_mean, '.')
    plt.plot(ns_lat, min_max_ns_lower, '.')
    plt.plot(ns_lat, min_max_ns_upper, '.')

    plt.show()

    pass