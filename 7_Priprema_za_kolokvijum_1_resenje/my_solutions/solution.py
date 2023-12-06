from utils_nans1 import *
from sklearn.model_selection import train_test_split

alpha = 0.05
rand_state = 42
train_part = 0.8

df_train = pd.read_csv("data/train.csv")
df_test = pd.read_csv("data/test.csv")

if __name__ == '__main__':
    ## check nans
    print(df_train.isna().sum())

    ## fixing train NANs
    df_train['zvanje'] = df_train['zvanje'].interpolate(method='spline', order=3, limit_direction='both')
    df_train['zvanje'] = df_train['zvanje'].round(0)

    df_train['godina_doktor'] = df_train['godina_doktor'].interpolate(method='spline', order=3, limit_direction='both')
    df_train['godina_doktor'] = df_train['godina_doktor'].round(0)

    ## drop 'pol Zenski' because of collinearity with 'pol Muski'
    print(perfect_collinearity_assumption(sm.add_constant(df_train), plot=False))
    df_train = df_train.drop(columns=['pol Zenski'])
    print(perfect_collinearity_assumption(sm.add_constant(df_train), plot=False))

    ## build model
    x_train = df_train.drop(columns=['plata'])
    y_train = df_train['plata']

    ## create model
    model = get_fitted_model(x_train, y_train)
    print(model.summary(), '\n\n')
    ## drop 'godina_iskustva' because p_value > p_treshhold
    ## then recreate and check
    x_train = x_train.drop(columns=['godina_iskustva'])
    model = get_fitted_model(x_train, y_train)
    print(model.summary(), '\n\n')
    ## drop 'pol Muski' because p_value > p_treshhold
    ## then recreate and check
    x_train = x_train.drop(columns=['pol Muski'])
    model = get_fitted_model(x_train, y_train)
    print(model.summary(), '\n\n')

    print("Tests:")
    print(linear_assumption(model, sm.add_constant(x_train), y_train, plot=False))
    print(independence_of_errors_assumption(model, sm.add_constant(x_train), y_train, plot=False))
    print(normality_of_errors_assumption(model, sm.add_constant(x_train), y_train, plot=False))
    print(equal_variance_assumption(model, sm.add_constant(x_train), y_train, plot=False))
    print("Metrics:")
    ## prep x_val, then count metrics
    x_test = df_test.drop(columns=['plata'])
    y_test = df_test['plata']
    x_test = x_test.drop(columns=['pol Muski', 'godina_iskustva', 'pol Zenski'])
    print(get_rmse(model, x_test, y_test))

    pass
