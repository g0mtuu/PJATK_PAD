import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from datetime import datetime
from datetime import date

from streamlit_option_menu import option_menu


def calculate_age(born):
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if age>=115: #zakładam że podany wiek większy niż 100 lat to oczywista omyłka przy podaniu roku urodzenia
        return age-100
    return age

selected = option_menu(
        menu_title="PAD6-streamlit-zadanie_domowe",
        options = ['Ankieta', 'Staty'], # wymagane
        icons= ['archive', 'activity'],
        menu_icon = 'cast',
        default_index=0, # na której stronie będziemy na początku
        orientation='horizontal'
    )

if selected == 'Ankieta':
    st.title(f'Jesteś w zakładce {selected}')
    st.write('Uzupełnij poniższe pola')
    name = st.text_input("Enter your first name")
    surname = st.text_input("Enter your family name")
    if st.button("Submit"):
        result = "Pomyślnie zapisano dane:"
        st.success(result)
        st.info( name.title() + surname.title())

if selected == 'Staty':
    st.title(f'Jesteś w zakładce {selected}')
    data = st.file_uploader("Upload your 'customers' dataset", type=['csv'])
    with st.spinner("Waiting..."):
        if data is not None:
            df = pd.read_csv(data)
            st.success("CSV Loaded")
            st.text("Dataframe head:")
            st.dataframe(df.head(3))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            if st.button("Histogram plot for gender"):
                st.text("Histogram for gender has been loaded")
                fig=px.histogram(df, "gender", labels={"gender": "Gender"}, title="Counts of gender")
                st.plotly_chart(fig, use_container_width=True)
            if st.button("Histogram plot for age"):
                df['dob'] = pd.to_datetime(df['birthdate'], errors='coerce')
                df['age'] = df['dob'].apply(calculate_age)
                st.text("Histogram for age has been loaded")
                fig=px.histogram(df, "age", labels={"age": "Age"}, title="Counts of age")
                st.plotly_chart(fig, use_container_width=True)

