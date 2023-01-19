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



            st.success("Loaded")


# st.header('nagłówek')
# st.subheader('pod nagłówek')

# st.text('hello world')

# st.markdown('# this is markdown 1A')
# st.markdown('## this is markdown 2')
# st.markdown('### this is markdown 3')
# st.markdown('# this is markdown 1B')

# st.success('successful')

# st.info('information')

# st.error('system error')

# st.exception('exception occured')

# st.help(range)

# st.write('some text')

# st.write(range(10))

# img = Image.open('testImg.png')
# st.image(img, width=300, caption='simple image')

# dodawanie audio i video
#with open('Richmond.mov', 'rb') as vid_file:
#    vid = vid_file.read()
# st.video(vid)
#
# with open('Armin van Buuren  Tomorrowland Belgium 2018 W2.mp3', 'rb') as audio_file:
#     audio = audio_file.read()
# st.audio(audio)

# # widgets

# # checkbox:
# if st.checkbox("pokaz/hide"):
#     st.text("showing or hiding widget")

# # radio
# status = st.radio("What is your status", ("Active", "Inactive"))

# st.success('You are active') if status == 'Active' else st.warning("Inactive. Please activate")

# # # select box
# occupation = st.selectbox("Your Occupation", ("Programmer", "Data Analyst", "Teacher"))
# st.write("You selected this occupation: ", occupation)


# location = st.multiselect("Where are you based?", ("London", "Warsaw", "Sydney", "San Francisco"))
# st.write("You selected: ", len(location), " locations")

# slider
# level = st.slider("What is your level", 1, 100)

# # buttons
# st.button("Simple button")
# if st.button("About"):
#     st.text("This is a very cool demo")

# # text input
# firstname = st.text_input("Please, enter your 1st name", "Type here...")
# if st.button("Submit"):
#     result = firstname.title()
#     st.success(result)

# # text area
# message = st.text_area("enter your msg")
# if st.button("Submit message"):
#     result2 = message.title()
#     st.success(result2)


# # date input
# today = st.date_input("Today is ", datetime.datetime.now())

# # time
# the_time = st.time_input("the time is ", datetime.time())

# displaying json
# st.text("Display JSON")
# st.json({'name': 'Dominika',
#         'gender': 'female'})

# # # displaying raw code
# st.text("Display raw code")
# st.code("import pandas as pd")

# # displaying raw code
# with st.echo():
#     # this will be shown as a comment
#     import pandas as pd
#     import numpy as np
#     df = pd.DataFrame({'name': ['Dominika', 'Grzegorz'],
#         'gender': ['female', 'male']})
#     df.head()

# # progress bar
# import time
# my_bar = st.progress(0)

# for p in range(100):
#     time.sleep(0.1)
#     my_bar.progress(p + 1)

# # spinner
# with st.spinner("Waiting..."):
#     time.sleep(3)
# st.success("Finished!")

# # SIDEBARS
# st.sidebar.header("About")
# st.sidebar.text("This is a Streamlit Demo")


# # function
# @st.cache
# def run_fxn():
#     return range(50)

# st.write(run_fxn())


# # uploading data
# data = st.file_uploader("Upload your dataset", type=['csv'])
# if data is not None:
#     df = pd.read_csv(data)
#     st.dataframe(df.head(10))

# # Plot
# st.set_option('deprecation.showPyplotGlobalUse', False)
# all_columns_names = df.columns.to_list()
# selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
# plot_data = df[selected_column_names]
# st.area_chart(plot_data)
# st.bar_chart(plot_data)
# st.line_chart(plot_data)
# plot_dataNN = df[selected_column_names].plot(kind='hist')
# st.write(plot_dataNN)
# st.pyplot()

# plot_dataNN = df[selected_column_names].plot(kind='box')
# st.write(plot_dataNN)
# st.pyplot()

# # dataframe
# st.dataframe(df)

# # tables
# st.table(df)