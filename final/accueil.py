import streamlit as st
from streamlit_option_menu import option_menu
from page1 import page1
from contact import contact

def streamlit_menu():  
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "4!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
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
elif selected == "Projects" :
    st.title(f"You have selected {selected}")
    page1()
elif selected == "Contact" :
    st.title(f"You have selected {selected}")
    contact()