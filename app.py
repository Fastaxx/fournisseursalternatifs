import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import page1, page2

PAGES = {
	"Volume d'échanges ARENH" : page1,
	"Sources" : page2
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Direction", list(PAGES.keys()))
page = PAGES[selection]
page.app()
