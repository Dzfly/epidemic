import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df)

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams["axes.unicode_minus"] = False

x_date = df["date"]
y_confirm = df["confirm"]
y_nowConfirm = df["nowConfirm"]
y_suspect = df["suspect"]
y_dead = df["dead"]
y_heal = df["heal"]
y_noInfect = df["noInfect"]

plt.title("Epidemic data")
plt.plot(x_date, y_confirm, color="red", linewidth=2.0, linestyle="--", label="确诊总人数")
plt.plot(x_date, y_nowConfirm, color="green", linewidth=2.0, linestyle="-", label="现存确诊人数")
plt.plot(x_date, y_suspect, color="orange", linewidth=2.0, linestyle="-", label="疑似人数")
plt.plot(x_date, y_dead, color="black", linewidth=2.0, linestyle="--", label="死亡人数")
plt.plot(x_date, y_heal, color="purple", linewidth=2.0, linestyle="--", label="治愈人数")
plt.plot(x_date, y_noInfect, color="gray", linewidth=2.0, linestyle="-", label="无症状感染者人数")
# 修改横坐标名称的摆放角度
plt.xticks(rotation=90)

plt.legend()
plt.show()
