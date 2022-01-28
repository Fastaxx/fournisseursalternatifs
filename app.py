import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 


header = st.container()

with header:
	st.title("Fournisseurs alternatifs")
	st.markdown("""
		Analyse 
		""")
	def load_data():
		volume_echange_chemin ='/Users/Louis/GitHub/fournisseursalternatifs/volumes-echanges-re.csv'
		data = pd.read_csv(volume_echange_chemin)
		return load_data

	df = load_data()
	st.write(df)
