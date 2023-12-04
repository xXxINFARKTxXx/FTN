import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sb

import line_pretpostavke as line

import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    ## read data
    df = pd.read_csv('data/housing.csv', sep =',')
    x = df['lotsize(m^2)']
    y = df['price']

    ## build model
    x_with_const = sm.add_constant(x)
    model = sm.OLS(y,x_with_const).fit()
    y_pred = model.predict(x_with_const)

    intercept, slope = model.params

    ## show model
    sb.scatterplot(data=df, x='lotsize(m^2)', y='price')
    plt.plot(x, y_pred, 'b', label=f'y = {slope:.2f} x + {intercept:.2f}')
    plt.legend(title='simple regression')
    plt.show()





    ## t-test check 1 TODO1.1
    print(line.linear_assumption(model, x_with_const, y))





    ## t-test check 2 TODO1.2
    print(line.linear_assumption(model, x_with_const, y, 0.01))





    ## confidence interval TODO1.3
    low_intercept, low_slope = model.conf_int(alpha=0.01)[0]
    high_intercept, high_slope = model.conf_int(alpha=0.01)[1]

    low_border = low_slope * x + low_intercept
    high_border = high_slope * x + high_intercept

    sb.scatterplot(data=df, x='lotsize(m^2)', y='price')
    plt.plot(x, y_pred)
    plt.plot(x, low_border)
    plt.plot(x, high_border)

    plt.show()





    # prediction interval TODO1.4
    ## prepare plot
    pred_intervals = model.get_prediction(x_with_const).summary_frame(0.05)

    plt.fill_between(df["lotsize(m^2)"],
                        pred_intervals["obs_ci_lower"],
                        pred_intervals["obs_ci_upper"],
                        color='b',
                        alpha=.1)
    sb.scatterplot(data=df, x='lotsize(m^2)', y='price') ## всю исходную дату
    plt.plot(x, y_pred) ## график предсказания
    plt.plot(x, low_border) ## нижнюю границу доверительного интервала
    plt.plot(x, high_border) ## верхнюю границу доверительного интревала

    ## init min_lotsize independent variable frame
    lotsize = 450
    lotsize_with_const = sm.add_constant([0, lotsize])
    ## inti value frame in model and take it summary
    pred_intervals = model.get_prediction(lotsize_with_const).summary_frame(0.05)
    
    ## get values from predicted interval frame
    lotsize_mean = pred_intervals['mean'][1]
    lotsize_obs_ci_lower = pred_intervals['obs_ci_lower'][1]
    lotsize_obs_ci_upper = pred_intervals['obs_ci_upper'][1]

    ## draw results on plot
    plt.plot(lotsize, lotsize_mean, '.')
    plt.plot(lotsize, lotsize_obs_ci_lower, '.')
    plt.plot(lotsize, lotsize_obs_ci_upper, '.')

    plt.show()
    pass