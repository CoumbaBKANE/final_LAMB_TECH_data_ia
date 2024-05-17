import streamlit as st

def home():
    # HTML content for styling
    html_content = """
        <div style='background-color: lightblue; padding: 20px; border-radius: 10px; text-align: center;'>
            <h1 style='color: green;'>Prévenir la Fraude dans le Transfert d'Argent au Sénégal</h1>
            <img src="" alt="Prévention de la Fraude" style='width: 100%; max-width: 600px; border-radius: 10px;'>
            <h2 style='color: darkred;'>Les Dangers de la Fraude liée au Gaming</h2>
        </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

    # Adding an image related to fraud prevention
