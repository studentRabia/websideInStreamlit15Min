import streamlit as st
import pandas as pd                 #Pandas ka use data ko manage karne, read karne aur manipulate karne ke liye hota hai (jaise CSV file).
import matplotlib.pyplot as plt     # matplotlib ek plotting library hai jo Python mein charts banane ke liye use hoti hai


st.title("Simple Data Dashbord")

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_colum =st.selectbox("Select column to filter by ",columns)
    unique_value = df[selected_colum].unique()
    selected_value = st.selectbox("Select Value ", unique_value)


    filtered_df = df[df[selected_colum] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column ",columns)
    y_column = st.selectbox("Select y-axis column ",columns)

    if st.button("Geerate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting on file upload...")




