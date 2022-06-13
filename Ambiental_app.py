import streamlit as st
import pandas as pd
import numpy as np
import urllib.request

print('Beginning file download with urllib2...')
@st.experimental_memo
def download_data():
  url = 'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Ov.Miraflores.xlsx'
  filename = 'data.xlsx'
  urllib.request.urlretrieve(url, 'data.xlsx')
  return filename

st.write(download_data())
def download_data2():
  url = 'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Bonilla.xlsx'
  filename = 'data.xlsx'
  urllib.request.urlretrieve(url, 'data.xlsx')
  return filename

st.write(download_data2())

n=st.slider("n", 5,100, step= 1)
chart_data=pd.DataFrame(np.random.randn(n), columns=['data'])
st.line_chart(chart_data)
