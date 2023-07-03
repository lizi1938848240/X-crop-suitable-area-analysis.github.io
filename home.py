# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:35:23 2023

@author: lenovo
"""

import streamlit as st
import os
from PIL import Image
# 获取当前脚本的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
st.title("X作物适宜区分析")
st.write("这里可以通过气温、降水、海拔、坡向、沟谷线缓冲区对X作物适宜区进行分析")
st.write("X作物可以销售到餐厅、超市等场所，本程序可以进行路径规划分析")
st.write("可以通过机器学习判断是否适宜")
st.write("技术路线图如下：")
# 加载本地图片
image = Image.open(os.path.join(current_dir, "技术路线.png"))

# 在Streamlit中显示图片
st.image(image, caption='Local Image', use_column_width=True)