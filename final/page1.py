import streamlit as st
import pandas as pd
import numpy as np

def page1():
    # Function to load and display the CSV file
    def load_and_display_csv(file_path):
        try:
            df = pd.read_csv(file_path)
            # HTML content for styling
            html_content = """
                <div style='background-color: lightblue; padding: 10px; border-radius: 5px;'>
                    <h2>Fichier de présentation des données fournies</h2>     
                </div>
            """
            st.markdown(html_content, unsafe_allow_html=True)
            st.write(df)
            return df
        except FileNotFoundError:
            st.error("Le fichier CSV n'a pas été trouvé. Assurez-vous que le chemin est correct.")
            return None

    # Load and display the CSV file
    df = load_and_display_csv("lambtech2024ia _dataset.csv")

    # Vérifier si le dataframe n'est pas vide
    if df is not None:
        # Obtenir toutes les colonnes pour le tracé
        all_columns = df.columns.tolist()

        if all_columns:
            # Message pour indiquer que les graphiques vont être affichés
            st.write("Graphiques des données fournies")

            # Sélectionner les colonnes pour les axes X et Y
            x_axis = st.selectbox("Choisissez la colonne pour l'axe X", options=all_columns)
            y_axis = st.multiselect("Choisissez les colonnes pour l'axe Y", options=all_columns)

            # Sélectionner le type de graphique
            plot_type = st.selectbox("Choisissez le type de graphique", ["Ligne", "Barres", "Nuage de points"])

            if x_axis and y_axis:
                try:
                    # Convertir les données catégoriques en numériques pour l'axe X si nécessaire
                    if df[x_axis].dtype == 'object':
                        df[x_axis] = df[x_axis].astype('category').cat.codes
                    
                    st.write(f"Graphique(s) de {', '.join(y_axis)} en fonction de {x_axis}")
                    
                    if plot_type == "Ligne":
                        st.line_chart(df.set_index(x_axis)[y_axis])
                    elif plot_type == "Barres":
                        st.bar_chart(df.set_index(x_axis)[y_axis])
                    elif plot_type == "Nuage de points":
                        for col in y_axis:
                            st.write(f"Nuage de points de {col} en fonction de {x_axis}")
                            st.scatter_chart(df[[x_axis, col]].set_index(x_axis))
                except KeyError as e:
                    st.error(f"Erreur: {e}. Vérifiez que les colonnes sélectionnées existent dans le fichier CSV.")
        else:
            st.warning("Le fichier CSV ne contient pas de colonnes à afficher.")
    else:
        st.warning("Aucun graphique à afficher car le fichier CSV n'a pas été chargé correctement.")