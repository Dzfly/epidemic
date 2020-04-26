import requests
import json
import time
import matplotlib.pyplot as plt

# # # 抓取疫情数据 # # #
# 数据原来的url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery341019095898772023956_1587643159551&_=1587643159552"
# ...callback=&_=%d" % int(time.time() * 1000) 增加一个时间戳
url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d" % int(time.time() * 1000)
# json.dumps	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象
data = json.loads(requests.get(url=url).json()["data"])
# print(data)
# print(data.keys())

num = data["areaTree"][0]["children"]
# 可以看出有34个省份
print(num)
print(len(num))
# 打印34个省份的名字
for item in num:
    print(item["name"], end=" ")  # 不换行输出,""中间的东西代表输出结果的间隔
else:
    print("n")  # 再变成换行输出，不然后面输出的结果都不会换行

# 显示黑龙江省的所有地区的数据
heilongjiang = num[0]["children"]
for data in heilongjiang:
    print(data)

# 统计全国每个省份的现存确诊人数
total_data = {}
for item in num:
    if item["name"] not in total_data:
        total_data.update({item["name"]: 0})
        # 直接使用提供的总数
        total_data[item["name"]] += int(item["total"]["nowConfirm"])
    # 利用每个城市的数量相加得到总数
    # for city_data in item["children"]:
    #     total_data[item["name"]] += int(city_data["total"]["nowConfirm"])
print(total_data)

# # # 绘制柱状图 # # #
# 设置汉字格式
# sans-serif就是无衬线字体，是一种通用字体族。
# 常见的无衬线字体有 Trebuchet MS, Tahoma, Verdana, Arial, Helvetica,SimHei 中文的幼圆、隶书等等
# 方法一
# import pylab as mpl
# mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 方法二
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams["axes.unicode_minus"] = False

# 获取数据
names = []
nums = []
for k, v in total_data.items():
    names.append(k)
    nums.append(v)
print(names)
print(nums)

# 整体大小
plt.figure(figsize=[10, 6])
# 修改柱状属性
plt.bar(names, nums, width=0.5, color="green")
# x,y轴名称
plt.xlabel("地区", size=12)
plt.ylabel("人数", rotation=90, size=12)
# 标题
plt.title("全国疫情现存确诊人数", size=16)
# x轴的地点名
plt.xticks(list(names), rotation=-45, size=10)
# ha='center', va= 'bottom'代表水平对齐、垂直对齐
for a, b in zip(names, nums):
    plt.text(a, b, b, ha="center", va="bottom", size=10)
plt.show()
