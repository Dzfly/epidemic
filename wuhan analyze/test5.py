import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wuhan data.csv")
print(df)

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams["axes.unicode_minus"] = False

x_date = df["date"]
y_confirmAdd = df["confirmAdd"]

plt.title("Wuhan Epidemic data")
plt.plot(x_date, y_confirmAdd, color="red", linewidth=2.0, linestyle="-", label="确诊总人数")
plt.xticks(rotation=90)

plt.legend()
plt.show()
