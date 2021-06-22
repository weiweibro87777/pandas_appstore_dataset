import pandas as pd

#讀取資料
data = pd.read_csv("/Users/weichen/Desktop/vscode_/learn/AppleStore.csv") #把 csv 格式的檔案讀取成一個 DataFrame

#觀察資料
# print(data)
print("資料數量：", data.shape)
print("資料欄位：", data.columns)
print("================================")

#分析資料：評分的各種統計數據
condition = data["user_rating"] <= 5
data = data[condition]
print("應用程式的評分平均數：", data["user_rating"].mean())
print("應用程式的評分中位數：", data["user_rating"].median())
print("前一千個應用程式的平均評分：", data["user_rating"].nlargest(500).mean())

#分析資料：價格的各種統計數據
print("應用程式的平均價格：", data["price"].mean())
print("================================")
print("總共有幾個應用程式：", data.shape[0])
condition = data['price'] == 0
print("免費的應用程式有幾個：", data[condition].shape[0])
condition = data['price'] > 0
print("收費的應用程式有幾個：", data[condition].shape[0])
condition = (data["price"] > 1) & (data["price"] < 2)
print("價格大於 1美金 且小於 2美金 的應用程式有幾個：", data[condition].shape[0])
result = data['price'].max()
print("最貴的應用程式多少美金：", result)

#資料應用：關鍵字搜尋應用程式名稱
print("================================")
keywords = input("請輸入關鍵字：")
print("================================")
condition = data["track_name"].str.contains(keywords, case = False)
print(data[condition]["track_name"])
print("================================")
print("包含關鍵字的應用程式數量", data[condition].shape[0])