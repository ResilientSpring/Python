import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))

# recipe = ["7.98 USD flour",
#           "75 g sugar",
#           "250 g butter",
#           "300 g berries"]

# data = [float(x.split()[0]) for x in recipe]
# ingredients = [x.split()[-1] for x in recipe]

data = [7.98, 15.39, 4.25, 5.87]

ingredients = ["Taipei Q1", "Taipei Q2", "Rest of TW Q1", "Rest of TW Q2"]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("2024 The distribution of Taiwan's Foreign Direct Investment by Region")

plt.xlabel("參考資料 Reference  https://taipeiecon.taipei/Econ/econ_obs?id=5")

plt.show()
