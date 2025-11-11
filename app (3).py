
import streamlit as st
import pandas as pd

st.title("📊 Tableau de bord - Production durable")

# Lecture du fichier de données
try:
    df = pd.read_excel("Données.xlsx")
    st.success("✅ Fichier 'Données.xlsx' chargé avec succès !")

    # Afficher un aperçu
    st.subheader("Aperçu des données :")
    st.dataframe(df.head())

    # Quelques statistiques simples
    st.subheader("📈 Statistiques descriptives :")
    st.write(df.describe())

except FileNotFoundError:
    st.error("❌ Le fichier 'Données.xlsx' est introuvable dans le dépôt GitHub.")
except Exception as e:
    st.error(f"⚠️ Une erreur est survenue lors du chargement : {e}")
