import json
import requests
import time
import csv
import pandas as pd

url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_= %d" % int(time.time() * 1000)

# html = requests.get(url).text
# unicode_str=json.loads(html)  #将string转化为dict
# new_list = unicode_str.get("data")  #获取data中的内容，取出的内容为str
# f_data = json.loads(new_list)  #对new_list再次进行load，使其变为dict才可使用
# 等同于
f_data = json.loads(requests.get(url=url).json()["data"])
s_data = f_data["chinaDayList"]
print(s_data)

# 日期 确诊总人数 现存确诊人数 疑似人数 死亡人数 治愈人数 无症状感染者
header = ["date", "confirm", "nowConfirm", "suspect", "dead", "heal", "noInfect"]
# newline="" 防止自动换行
with open("data.csv", encoding="UTF-8-sig", mode="w", newline="") as a:
    a_csv = csv.writer(a)
    a_csv.writerow(header)
a.close()


def save_data(obj):
    # a+ 打开一个文件用于读写。
    # 如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    with open("data.csv", encoding="UTF-8", mode="a+", newline="") as b:
        b_csv = csv.writer(b)
        b_csv.writerow(obj)
        print(obj)
    a.close()


length_data = len(s_data)
print(length_data)
i = 0

while i < length_data:
    date = pd.Series(s_data[i]["date"])
    # 修改日期格式，避免被吞0
    for d in date:
        n_date = str(d).replace('.', '/')
    confirm = (s_data[i]["confirm"])
    nowConfirm = (s_data[i]["nowConfirm"])
    suspect = (s_data[i]["suspect"])
    dead = (s_data[i]["dead"])
    heal = (s_data[i]["heal"])
    noInfect = (s_data[i]["noInfect"])
    i += 1
    tap = (n_date, confirm, nowConfirm, suspect, dead, heal, noInfect)
    save_data(tap)

print("Done~")
