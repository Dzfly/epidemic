import requests
import json
import time
import csv
import pandas as pd

url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_= %d" % int(time.time() * 1000)

f_data = json.loads(requests.get(url=url).json()["data"])
s_data = f_data["wuhanDayList"]
print(s_data)

header = ["date", "confirmAdd"]
with open("wuhan data.csv", encoding="UTF-8-sig", mode="w", newline="") as a:
    a_csv = csv.writer(a)
    a_csv.writerow(header)
a.close()


def save_data(obj):
    with open("wuhan data.csv", encoding="UTF-8", mode="a+", newline="") as b:
        b_csv = csv.writer(b)
        b_csv.writerow(obj)
        print(obj)
    a.close()


length_data = len(s_data)
print(length_data)
i = 0

while i < length_data:
    date = pd.Series(s_data[i]["date"])
    for d in date:
        n_date = str(d).replace('.', '/')
    Add = (s_data[i]["wuhan"]["confirmAdd"])
    i += 1
    tap = (n_date, Add)
    save_data(tap)

print("Done~")
