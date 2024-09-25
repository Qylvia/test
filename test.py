
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("请选择文件进行上传", type=None)

# 检查是否有文件上传
if uploaded_file is not None:
    # 读取 CSV 文件
    df = pd.read_csv(uploaded_file)

    # 读取第一行数据
    first_row = df.iloc[0]

    # 展示第一行数据
    st.write("First row of the CSV file:")
    st.write(first_row)

