import streamlit as st
from streamlit_option_menu import option_menu

def streamlit_menu():  
        # 2. horizontal menu with custom style
    with st.sidebar:
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Upload", "Contact"],  # required
            icons=["house", "cloud-upload", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "4!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu()

if selected == "Home" :
    st.title(f"You have selected {selected}")
elif selected == "Upload" :
    st.title(f"You have selected {selected}")
    st.write("Upload your data here")
elif selected == "Contact" :
    st.title(f"You have selected {selected}")
    st.write("Contact us here")
