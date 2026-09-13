import pandas as pd
import streamlit as st

import streamlit as st
from PIL import Image
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Food Dataset dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

st.title(body="Food Ordering Dashoboard",
         text_alignment="center")

# about dataset section
with st.expander(label="About Food Ordering dataset"):
    st.header("About Food Ordering dataset")
    st.write("This dataset contains information about customers and their online food ordering behavior. It includes demographic, socioeconomic, educational, family, geographic and customer feedback attributes that can be used to understand patterns and factors associated with online food ordering.")

df = pd.read_csv('food-ordering-dataset/online food delivery dataset.csv')

st.subheader(body="Age and Marital Status",
             text_alignment="center")
st.bar_chart(
    data={
        "Age" : df["Age"],
        "Marital Status": df["Marital Status"],
    },
    y="Age",
    x="Marital Status",
    y_label="Customer count",
    x_label="Custommer Marital Status"
)


st.subheader("Customer type and Family size var chart", 
             text_alignment="center")
st.bar_chart(
    data={
        "Customer Type" : df["Customer Type"],
        "Family size": df["Family size"],
    },
    x="Customer Type",
    y="Family size",
)

st.subheader(body="Montly Income and Occuppation",
             text_alignment="center")
st.scatter_chart(
    data={
        "Occupation" : df["Occupation"],
        "Monthly Income" : df["Monthly Income"]
    },
    x="Occupation",
    y="Monthly Income",
)

# Age,Gender,Marital Status,Occupation,Monthly Income,Educational Qualifications,Family size,Customer Type,latitude,longitude,Pin code,Output,Feedback,


# side bar
with st.sidebar:
    st.header("Filters")
    selected_attribute = st.selectbox(label="select attribute",
                                      options={
                                      "Occupation":df["Occupation"],
                                      "Age": df["Age"],
                                      "Customer Type": df["Customer Type"],
                                      "Pin code": df["Pin code"]
                                       },
    )

    selected_attribute_values = st.multiselect(label=selected_attribute,
                                      options=df[selected_attribute].unique(),
                                      placeholder=f"Filter by {selected_attribute}")


st.data_editor(
    data={
        selected_attribute : df[selected_attribute].unique(),
        f"number of {selected_attribute}" : df[selected_attribute].value_counts(),
    },
    num_rows="dynamic", # The user can add or delete rows
)

px.scatter_matrix(df, )