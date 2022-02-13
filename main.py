# Importing Essentional libraries
import streamlit as st
import pandas as pd
from typing import List

# Making variables for our project
header = st.container()
dataset = st.container()
features = st.container()
model = st.container()
data = pd.read_csv('cars.csv')
money = []

# Cleaning Dataset
data.dropna(inplace=True)


# All logics are writing here:

def newDataFrame(brands: List[str]):
    """

    :param brands:
    :return:
    """
    for brand in brands:
        j = data.loc[data['Make'] == brand].Invoice.sum()
        money.append(j)

    d = {'Brand': brands, 'Money': money}
    return pd.DataFrame(d)


l = list(data.Invoice)
changed_list = []
for i in l:
    if type(i) == str:
        i = i[1:-1]
        i = i.replace(',', '')
        i = int(i)
    else:
        i = int(i)
    changed_list.append(i)
data.Invoice = changed_list

most_expencive_car = data.loc[data['Invoice'] == data['Invoice'].max()]
most_expencive_car.reset_index(inplace=True)
origin = data

# Sending data to Streamlit and showing on webpage
with header:
    st.title('Streamlit Project on Cars dataset')

with dataset:
    st.header('Cars Dataset')
    st.write(data.head(15))
    st.text("Let`s analyze our dataset!")
    st.write(data.columns)
    st.write(data.describe())

with features:
    st.header("features I have created.")
    st.text("What kind of Car Type is popular and most sold in the World")
    st.write(data['Type'].value_counts())
    st.bar_chart(data['Type'].value_counts())
    st.text("The most expencive car in this dataframe is Porsche")
    st.write(most_expencive_car)
    st.text('The most car sold continent :')
    st.write(data['Origin'].value_counts())
    st.line_chart(data.Origin.value_counts())
    st.text("What kind of engine sizes we have")
    st.write(data['EngineSize'].unique())
    st.text("Which are the most favourable")
    st.write(data['EngineSize'].value_counts())
    st.area_chart(data['EngineSize'].value_counts())
    inp = st.text_input('Which data do you want to know', 'Origin')
    inp = inp.capitalize()
    try:
        st.write(data[inp].value_counts())
    except:
        st.text(f"Please input valid name between values below :")
        st.write(data.columns)
    choose = st.slider('Select cars with it`s horsepower:', min_value=30, max_value=300, step=10)
    sellected = data.loc[data['Horsepower'] >= choose]
    st.write(sellected)
    brands = list(data['Make'].unique())
    brandselect = st.selectbox('Choose brands from DataFrame', brands)
    select_brand = data.loc[data['Make'] == brandselect]
    st.write(select_brand)
    st.text(f'We have {len(select_brand)} of {brandselect} and earned {select_brand["Invoice"].sum()}$')
    newdata = newDataFrame(brands)
    newdata.set_index('Brand', inplace=True)
    st.write("The most profited company for selling cars")
    filtered = newdata.nlargest(len(newdata), 'Money')
    st.write(filtered)
    st.bar_chart(newdata.Money)
