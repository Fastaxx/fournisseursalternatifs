import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

def app():
    st.title("Volume d'échanges ARENH")

    data = pd.read_csv('HistoriquevolumesARENH.csv', sep=';', index_col=0, parse_dates=True)
    demande = data[["Demande ARENH", "Plafond ARENH"]]

    st.line_chart(demande)

