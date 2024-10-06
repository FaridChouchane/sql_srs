import streamlit as st
import pandas as pd
import duckdb

st.write("""
         # SQL SRS
         Space Repetition System SQL Practice
         """)

option = st.selectbox(
    "What do you like to review ?",
    ["Joins", "GroupBy", "Windows Functions"],
    index = None,
    placeholder = "Select a theme...",

)

st.write("You selected :", option)


data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label = "Entrez votre input : ")

    if sql_query:
        try:
            # Exécuter la requête SQL
            result = duckdb.query(sql_query).df()
            st.write(f"Vous avez entré la query suivante : {sql_query}")
            st.dataframe(result)  # Afficher le résultat sous forme de tableau
        except Exception as e:
            # Afficher une erreur si la requête échoue
            st.error(f"Erreur lors de l'exécution de la requête : {e}")
    else:
        st.info("Veuillez entrer une requête SQL.")  # Message si aucune requête n'est entrée