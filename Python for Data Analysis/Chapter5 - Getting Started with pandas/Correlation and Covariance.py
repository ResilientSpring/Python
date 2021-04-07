import numpy as np
import pandas as pd
import pandas_datareader as web

all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ["AAPL", "IBM", "MSFT", "GOOG"]};

price = pd.DataFrame({ticker: data["Adj Close"] for ticker, data in all_data.items()});

volume = pd.DataFrame({ticker: data["Volume"] for ticker, data in all_data.items()});

returns = price.pct_change();

print(returns.tail());

correlation = returns["MSFT"].corr(returns["IBM"]);
print(correlation);

covariance = returns["MSFT"].cov(returns["IBM"]);
print(covariance);