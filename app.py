import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')
# Encabezado de la app
st.header('Panel interactivo de anuncios de vehículos')
# Botón para mostrar histograma
if st.button('Mostrar histograma de kilometraje'):
    st.write('Distribución del kilometraje de los vehículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
# Botón para mostrar gráfico de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write('Relación entre kilometraje y precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
# Botón para mostrar gráfico de dispersión con condición
if st.button('Mostrar dispersión con condición del vehículo'):
    st.write('Relación entre kilometraje y precio según condición')
    fig = px.scatter(car_data, x='odometer', y='price', color='condition',
                     title='Relación entre kilometraje y precio según condición')
    st.plotly_chart(fig, use_container_width=True)
