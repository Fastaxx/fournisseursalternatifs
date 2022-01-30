import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

def app():
	st.title("Prix électricité")
	df=pd.read_csv('TRVHPHC_2012-2021.csv', sep=';', index_col=0, parse_dates=True)
	st.write(df)
	st.line_chart(df)