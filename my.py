import streamlit as st
import time
import numpy as np

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

chart = st.line_chart(np.zeros(shape=(1,1)))
x = np.arange(0, 100*np.pi, 0.1)

for i in range(1, 101):
    y = np.sin(x[i])
    status_text.text("%i%% Complete" % i)
    chart.add_rows([y])
    progress_bar.progress(i)
    time.sleep(0.05)

progress_bar.empty()
