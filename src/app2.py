import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Segmentación de Pacientes", layout="wide")

def load_data():
    """Carga el dataset"""
    try:
        return pd.read_csv('epigen_nov1.csv', encoding='latin1')
    except Exception as e:
        st.error(f'Error al cargar el dataset: {e}')
        return None

def classify_patient(row):
    """
    Clasifica pacientes según el número de valores '1' en la fila:
    - 11-15 unos: 'Healthy'
    - 16-20 unos: 'Mild'
    - 21-25 unos: 'Severe'
    """
    count_ones = (row == 1).sum()
    if 11 <= count_ones <= 15:
        return 'Healthy'
    elif 16 <= count_ones <= 20:
        return 'Mild'
    elif 21 <= count_ones <= 25:
        return 'Severe'
    else:
        return 'No clasificado'

# Título
st.title("🏥 Análisis de Segmentación de Pacientes")

# Cargar datos
df = load_data()

if df is not None:
    # Aplicar la clasificación
    df['Clasificación'] = df.apply(classify_patient, axis=1)
    
    # Mostrar distribución de clasificaciones
    st.header("📊 Distribución de Pacientes")
    
    # Conteo de pacientes por clasificación
    clasificacion_counts = df['Clasificación'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de pie
        fig_pie = px.pie(
            values=clasificacion_counts.values,
            names=clasificacion_counts.index,
            title="Distribución de Clasificaciones"
        )
        st.plotly_chart(fig_pie)
    
    with col2:
        # Gráfico de barras
        fig_bar = px.bar(
            x=clasificacion_counts.index,
            y=clasificacion_counts.values,
            title="Conteo por Clasificación",
            labels={'x': 'Clasificación', 'y': 'Número de Pacientes'}
        )
        st.plotly_chart(fig_bar)
    
    # Estadísticas detalladas
    st.header("📈 Estadísticas por Clasificación")
    
    # Mostrar el número de unos por paciente
    df['Cantidad_Unos'] = df.iloc[:, :-1].sum(axis=1)
    
    fig_box = px.box(
        df,
        x='Clasificación',
        y='Cantidad_Unos',
        title="Distribución de Valores de elementos por Clasificación",
        points="all"
    )
    st.plotly_chart(fig_box)
    
    # Tabla de resumen
    st.header("📋 Resumen Detallado")
    resumen = pd.DataFrame({
        'Total Pacientes': clasificacion_counts,
        'Porcentaje': (clasificacion_counts / len(df) * 100).round(2),
        'Promedio Unos': df.groupby('Clasificación')['Cantidad_Unos'].mean().round(2)
    })
    st.dataframe(resumen)
    
    # Opción para descargar resultados
    if st.button("Descargar Resultados"):
        csv = df.to_csv(index=False)
        st.download_button(
            label="Confirmar Descarga",
            data=csv,
            file_name="clasificacion_pacientes.csv",
            mime="text/csv"
        )
    
else:
    st.error("No se pudo cargar el dataset. Por favor, verifica el archivo y su ubicación.")
    
    # Botón para descargar resultados
    if st.button("Descargar Resultados"):
        csv = df.to_csv(index=False)
        st.download_button(
            label="Confirmar Descarga",
            data=csv,
            file_name="segmentacion_pacientes.csv",
            mime="text/csv"
        )