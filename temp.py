# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
from PIL import Image
import cv2
import numpy as np

st.title('顔面隠し')

uploaded_file = st.file_uploader("画像を選択してください", type ='jpg')

left_column, right_column = st.columns(2)
button = left_column.button('顔面を塗りつぶす')
if button:
    image = Image.open(uploaded_file)
    image.save("uploaded.jpg")
    img_array = np.array(image)
    st.image(img_array,caption = '元画像', use_column_width = True)



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