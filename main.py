import streamlit as st
import pandas as pd
from io import StringIO
import prediction
from PIL import Image
import math

st.write('''# Plant Disease Detection''')
st.image("static/background.png")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.image(bytes_data, width=300)
    pred = prediction.predict_image(uploaded_file)
    print(pred)
    st.write(f'''### Disease : {pred['predicted_class']}''')
    st.write(f'''### Confidence : {math.floor((pred['confidence']*100))} %''')

