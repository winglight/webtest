import streamlit as st
import pandas as pd

# 读取CSV文件
df1 = pd.read_csv("企业信息.csv")
df2 = pd.read_csv("行业信息.csv")

# 创建Streamlit交互界面
st.title("企业政策支持查询")

# 显示企业信息表格
st.subheader("企业信息表格")
st.dataframe(df1)

# 显示行业信息表格
st.subheader("行业信息表格")
st.dataframe(df2)

# 输入企业名称并查询政策支持
company_name = st.text_input("请输入企业名称：")
if company_name:
    result = df1[df1["企业名称"] == company_name]
    if not result.empty:
        industry = result["所在行业"].iloc[0]
        support = df2[df2["行业名称"] == industry]["是否政策支持"].iloc[0]
        st.success(f"企业'{company_name}'所在行业为'{industry}'，是否政策支持：{support}")
    else:
        st.warning("未找到该企业信息，请检查输入的企业名称是否正确。")


