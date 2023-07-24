import pandas as pd

# 创建第一个CSV文件
data1 = {
    "企业名称": ["企业A", "企业B", "企业C", "企业D"],
    "所在行业": ["行业1", "行业2", "行业1", "行业3"]
}
df1 = pd.DataFrame(data1)

# 创建第二个CSV文件
data2 = {
    "行业名称": ["行业1", "行业2", "行业3"],
    "是否政策支持": ["是", "否", "是"]
}
df2 = pd.DataFrame(data2)

# 保存为CSV文件
df1.to_csv("企业信息.csv", index=False)
df2.to_csv("行业信息.csv", index=False)
