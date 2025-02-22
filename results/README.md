
# Carpeta de resultados 
---
En esta carpeta se anexan sólo algunos archivos con relevancia del análisis exploratorio

Se pueden usar estas visualizaciones para: 

## imagen 1 ejemplo EDA
- ver cómo se distribuyen categorías por tipo de paciente, moderado, severo y saludable.
![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Grafico_1.png)

## imagen 2 ejemplo EDA
- cuántas características tiene mal la persona más *enferma*, según una clasificación a conveniencia para este dataset.
![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Grafico_2.png)

## imagen 3 ejemplo EDA
- observar cuáles variables tienden a aparecer juntas y, el número de ocurrencias de las mismas.
![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Gr%C3%A1fico_3.png)

## imagen 4 ejemplo EDA
- ver el uso del dendrograma para observar cómo se comportan algunas características junto a las otras.
![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Grafico_4.png)
---

# Ampiación del Análisis Final

El análisis inicial de este proyecto ya contaba con visualizaciones con el uso de Altair, y para fortalecer el análisis en este proyecto final, se utilizó Python para leer los documentos con los resultados de los pacientes en PDF y Streamlit para mostrar algunos de los resultados del análisis en una App dinámica.

Los resultados de los pacientes originalmente se generan en formato PDF, y es necesario bajar de este formato la información necesaria para este análisis, esto se desarrolla con la librería PyMuPDF de Python.

En el caso de Streamlit, esta herramienta resulta de gran valor para hacer publicaciones con resultados del análisis en una App dinámica, mediante gráficos de barras, gráficos circulares, diagramas de caja (boxplots) y tablas de resumen. Las siguientes imágenes corresponden a la creación y ejecución de Streamlit con los nombres verdaderos de las variables para que pueda ser apreciada su utilidad y funcionalidad.
---
## Imágenes reales de la ejecución de Streamlit

### Ejemplo 1
En el siguiente gráfico se puede apreciar el análisis de resultado mostrando un gráfico de barras y un comparativo de las variables metales pesados y químicos.

![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Screenshot%202024-11-30%20074209.png)

### Ejemplo 2
La siguiente imagen muestra el mismo caso, pero ahora la comparativa se hace entre parásitos y esporas.

![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Screenshot%202024-11-30%20074223.png)

### Ejemplo 3
Estas variables de análisis en las comparativas se llevan a cabo mediante un menú despegable, mostrado en la siguiente imagen:

![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Screenshot%202024-11-30%20074234.png)

### Ejemplo 4
Y por último, se muestra una imagen de segmentación de pacientes, en la que se incluye vía Streamlit un diagrama circular, un gráfico de barras y, boxplot. Notar que al pasar el puntero sobre los boxplots, aparecen detalles estadísticos con su explicación de conformación.

![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Screenshot%202024-11-30%20074248.png)

---
Si tienes alguna contribución, acude a la carpeta de CONTRIBUTIONS para ver las formas en que puedes ayudar a mejorar el presente proyecto.

