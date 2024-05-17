import streamlit as st
import pandas as pd
import numpy as np
import cv2
from upload import upload
def page1():
    menu = ["upload file", "Analyse","prediction"]
    choice = st.sidebar.selectbox("Menu", menu)
    # choice =="Analyse"

    if choice == "upload file":
        upload()
    elif choice == "Analyse":
        st.write("bienvenue sur la page d'analyse")
    elif choice == "prediction":
        st.write("bienvenue sur la page de prediction")
