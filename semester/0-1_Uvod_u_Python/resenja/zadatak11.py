import numpy as np


def stocks_share(years, total_stocks):
    total_years = np.sum(years)
    single_year = total_stocks / total_years
    stocks = np.round(years * single_year)
    return stocks


if __name__ == "__main__":
    years = np.array([2, 3, 4, 6, 1, 2, 4, 8])
    stocks = stocks_share(years, 1000)
    print(stocks)
    print(sum(stocks))
