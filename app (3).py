import pandas as pd
import streamlit as st

# Specify the path to your file
file_path = "Données.xlsx"

st.title("Données de Production Durable")

try:
    # Read all sheets from the Excel file into a dictionary of DataFrames
    excel_data = pd.read_excel(file_path, sheet_name=None)

    st.write("Onglets disponibles et aperçu des données :")
    # Iterate through the dictionary and display each DataFrame
    for sheet_name, df in excel_data.items():
        st.header(f"Onglet : {sheet_name}")
        st.dataframe(df)

except FileNotFoundError:
    st.error(f"Error: File not found at {file_path}")
except Exception as e:
    st.error(f"An error occurred: {e}")
