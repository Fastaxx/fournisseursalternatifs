import streamlit as st
import pandas as pd
import page1, page2, page3

PAGES = {
	"Volume d'échanges ARENH" : page1,
	"Prix électricité" : page3,
	"Sources" : page2
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Direction", list(PAGES.keys()))
page = PAGES[selection]
page.app()
