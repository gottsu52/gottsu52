# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from PIL import Image

import matplotlib.pyplot as plt

st.title('初めてのstreamlit')
st.write('私の名前は中澤駿です')

x = [30, 20, 15, 5]

plt.pie(x)
plt.show()

text = st.text_input('あなたの名前を教えて下さい')
'あなたの名前は,',text,'です'

condition = st.slider('あなたの今の調子は？', 0,100,80)
'コンディション: ' , condition

option = st.selectbox('好きな数字を教えてください', list (['1番','2番','3番','4番']))
'あなたが選択したのは,',option,'です'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
    
img = Image.open('photo_gyudon_100900.jpg')
st.image(img, caption = 'これは推しです', use_column_width = True)