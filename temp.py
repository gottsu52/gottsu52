# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.title('顔面潰し')
st.write('あなたや友人の顔面を塗りつぶします。横顔やマスクは認識しづらいので注意してください。')
st.write('jpg形式のみ対応しています。')

uploaded_file = st.file_uploader("顔面を選択してください", type ='jpg')

if uploaded_file is None :
    st.write('顔面が選択されていません')

else:
    image = Image.open(uploaded_file)
    image.save("uploaded.jpg")
    img_array = np.array(image)
    st.image(img_array,caption = '元画像', use_column_width = True)
    
    left_column, right_column = st.columns(2)
    button = left_column.button('顔面を塗りつぶす')
    
    if button:

        face_cascade_path = "haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(face_cascade_path)

        src = cv2.imread('uploaded.jpg')
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) #グレースケール化
        faces = face_cascade.detectMultiScale(src_gray)

        for (x, y, w, h) in faces:
            src[y: y + h, x: x + w] = [0, 128, 255]
    
        cv2.imwrite('opencv_mosaic_face.jpg', src)

        src2 = Image.open('opencv_mosaic_face.jpg')
        st.image(src2, caption='出力結果', use_column_width = True)
