import csv

import streamlit as st
import pandas as pd
from donut.out import show_line_chart
from typing import List

st.write('上传csv文件，进行数据转换 :wave:')
file = st.file_uploader('上传文件', type=['csv'], key=None)


@st.cache
def get_data(cache_file):
    csv_file = pd.read_csv(cache_file,header=0)
    st.write(csv_file)
    base_timestamp = csv_file.iloc[:, 0]
    st.write(base_timestamp)
    base_values = csv_file.iloc[:, 1]
    st.write(base_values)

    # list=csv_file.values.tolist()
    # base_timestamp= list[0]
    # print(base_timestamp)
    # base_values = list[1]
    # base_labels = list[2]
    # st.write(df)
    #
    # base_timestamp = []
    # base_values = []
    # 默认无标签
    base_labels = []
    # for i, line in enumerate(file.getvalue().split('\n')):
    #     line.split(',')
        # reader = csv.reader(file)
    # next(reader)
    # for i in reader:
    #     base_timestamp.append(int(i[0]))
    #     base_values.append(float(i[1]))
    #     base_labels.append(int(i[2]))
    show_line_chart(False,base_timestamp,base_values,"test")

b=st.button("ok")
if b:
    df = get_data(file)

st.info('info')