import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 



st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

latest_iteration = st.empty()
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}') 
    bar.progress(i+1)
    time.sleep(0.1)

option = st.text_input('あなたが好きな数字を教えてください。')


'あなたの好きな数字は', text , 'です '