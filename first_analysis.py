# 我的第一个数据分析脚本 - 电影评分分析
import pandas as pd

# 手动创建数据（无需爬虫）
data = {
    '电影名称': ['肖申克的救赎', '阿甘正传', '泰坦尼克号', '星际穿越'],
    '评分': [9.7, 9.5, 9.4, 9.3],
    '票房(亿)': [0.58, 6.77, 22, 7.55]
}
df = pd.DataFrame(data)

# 1. 找到最高评分电影
highest_rating = df[df['评分'] == df['评分'].max()]
print("=== 最高评分电影 ===")
print(highest_rating[['电影名称', '评分']])

# 2. 计算平均票房
avg_box_office = df['票房(亿)'].mean()
print("\n=== 平均票房 ===")
print(f"{avg_box_office:.2f} 亿")

# 3. 输出所有数据
print("\n=== 数据集 ===")
print(df)