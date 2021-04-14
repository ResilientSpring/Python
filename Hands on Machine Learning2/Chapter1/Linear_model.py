import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
from sklearn.linear_model import LinearRegression

def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"];
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value");
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True);
    gdp_per_capita.set_index("Country", inplace=True);
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita, left_index=True,
                                  right_index=True);
    full_country_stats.sort_values(by="GDP per capita", inplace=True);
    remove_indices = [0, 1, 6, 8, 33, 34, 35];
    keep_indices = list(set(range(36)) - set(remove_indices));

    return full_country_stats[["GDP per capita", "Life satisfaction"]].iloc[keep_indices];


# Load the data
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/lifesat/oecd_bli_2015.csv"
oecd_bli = pd.read_csv(filepath_or_buffer=url,);
print(oecd_bli);

url2 = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/lifesat/gdp_per_capita.csv"
gdp_per_capita = pd.read_csv(filepath_or_buffer=url2, delimiter='\t', encoding="latin1",
                             na_values="n/a");
print(gdp_per_capita);

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita);
X = np.c_[country_stats["GDP per capita"]];
y = np.c_[country_stats["Life satisfaction"]];

# Visualize the data
country_stats.plot(kind="scatter", x="GDP per capita", y="life satisfaction");
plt.show();

# Select a linear model
model = LinearRegression();

# Train the model
model.fit(X=X, y=y);

# Make a prediction for Cyprus
X_new = [[22587]]; # Cyprus' GDP per capita
print(model.predict(X=X_new));