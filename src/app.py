import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Configuración de la página
st.set_page_config(page_title="Análisis Epigenético", layout="wide")

def load_data():
    """Carga el dataset"""
    try:
        # Intentar diferentes codificaciones
        return pd.read_csv('epigen_nov1.csv', encoding='latin1')  # o 'iso-8859-1'
    except Exception as e:
        st.error(f'Error al cargar el dataset: {e}')
        return None

# Cargar datos
df = load_data()

# Verificar si df se cargó correctamente antes de usarlo
if df is not None:
    st.success('Dataset cargado correctamente')
    # Aquí continúa el resto del código que usa df
else:
    st.error('No se pudo cargar el dataset. Por favor, verifica el archivo y su ubicación.')

# Menú lateral para selección de análisis
análisis_seleccionado = st.sidebar.selectbox(
    "Seleccione el tipo de análisis:",
    ["Vista General", "Análisis por Grupos", "Correlaciones", "Patrones PCA"]
)

if análisis_seleccionado == "Vista General":
    st.header("📊 Vista General de los Datos")
    
    # Mostrar estadísticas básicas
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Dimensiones del Dataset")
        st.write(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    
    with col2:
        st.subheader("Columnas con más valores positivos")
        valores_positivos = (df > 0).sum().sort_values(ascending=False)
        st.bar_chart(valores_positivos.head(10))
    
    # Visualización de datos seleccionados
    st.subheader("Explorador de Variables")
    columnas_seleccionadas = st.multiselect(
        "Seleccione variables para visualizar:",
        df.columns.tolist(),
        default=df.columns[:5].tolist()
    )
    
    if columnas_seleccionadas:
        st.line_chart(df[columnas_seleccionadas])

elif análisis_seleccionado == "Análisis por Grupos":
    st.header("👥 Análisis por Grupos")
    
    # Seleccionar variable para agrupar
    variable_grupo = st.selectbox(
        "Seleccione variable para agrupar:",
        df.columns
    )
    
    # Crear grupos basados en presencia/ausencia
    grupos = df[variable_grupo].map({0: 'Ausente', 1: 'Presente'})
    
    # Seleccionar variables para comparar
    variables_comparar = st.multiselect(
        "Seleccione variables para comparar entre grupos:",
        [col for col in df.columns if col != variable_grupo],
        default=[df.columns[0]]
    )
    
    if variables_comparar:
        for var in variables_comparar:
            fig = px.box(df, y=var, color=grupos,
                        title=f'Distribución de {var} por {variable_grupo}')
            st.plotly_chart(fig)

elif análisis_seleccionado == "Correlaciones":
    st.header("🔄 Análisis de Correlaciones")
    
    # Calculamos correlaciones
    corr_matrix = df.corr()
    
    # Selector de umbral de correlación
    umbral_corr = st.slider(
        "Seleccione umbral de correlación:",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1
    )
    
    # Encontrar correlaciones significativas
    correlaciones_altas = pd.DataFrame()
    for col1 in corr_matrix.columns:
        for col2 in corr_matrix.columns:
            if col1 < col2:  # Evitar duplicados
                corr = corr_matrix.loc[col1, col2]
                if abs(corr) > umbral_corr:
                    correlaciones_altas = correlaciones_altas.append({
                        'Variable 1': col1,
                        'Variable 2': col2,
                        'Correlación': corr
                    }, ignore_index=True)
    
    if not correlaciones_altas.empty:
        st.write("Correlaciones significativas encontradas:")
        st.dataframe(correlaciones_altas.sort_values('Correlación', ascending=False))
        
        # Visualización de correlación seleccionada
        if st.button("Visualizar primera correlación"):
            var1 = correlaciones_altas.iloc[0]['Variable 1']
            var2 = correlaciones_altas.iloc[0]['Variable 2']
            fig = px.scatter(df, x=var1, y=var2, 
                           title=f'Correlación entre {var1} y {var2}')
            st.plotly_chart(fig)

else:  # Patrones PCA
    st.header("🎯 Análisis de Componentes Principales")
    
    # Configuración de PCA
    n_components = st.slider(
        "Número de componentes principales:",
        min_value=2,
        max_value=min(10, df.shape[1]),
        value=3
    )
    
    # Realizar PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    # Visualización de varianza explicada
    st.subheader("Varianza Explicada por Componente")
    varianza_explicada = pd.DataFrame({
        'Componente': range(1, n_components + 1),
        'Varianza Explicada (%)': pca.explained_variance_ratio_ * 100
    })
    fig = px.bar(varianza_explicada, x='Componente', y='Varianza Explicada (%)')
    st.plotly_chart(fig)
    
    # Visualización 3D si hay suficientes componentes
    if n_components >= 3:
        st.subheader("Visualización 3D de Componentes Principales")
        fig = px.scatter_3d(
            x=X_pca[:, 0], y=X_pca[:, 1], z=X_pca[:, 2],
            labels={'x': 'PC1', 'y': 'PC2', 'z': 'PC3'},
            title='Distribución de muestras en espacio PCA'
        )
        st.plotly_chart(fig)

# Añadir información adicional en el sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### Información del Dataset")
st.sidebar.write(f"Total de variables: {df.shape[1]}")
st.sidebar.write(f"Total de muestras: {df.shape[0]}")

# Botón para descargar datos procesados
if st.sidebar.button("Descargar Datos Procesados"):
    csv = df.to_csv(index=False)
    st.sidebar.download_button(
        label="Confirmar Descarga",
        data=csv,
        file_name="datos_procesados.csv",
        mime="text/csv"
    )