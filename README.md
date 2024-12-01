# Análisis de resultados de exámenes de laboratorio epigenetics

Repositorio con análisis exploratorio para exámenes de laboratorio y sus correlaciones. 

Autor: Eduardo Carlos Fletes Aréchiga

e-mail: eduardo.fletes1892@alumnos.udg.mx
________________________________________________________________________________________________________________

Proyecto para la Maestría en Ciencias de los Datos, Universidad de Guadalajara

El proyecto presenta un análisis exploratorio de datos obtenidos de los exámenes de laboratorio de distintas personas.
En el presente estudio no se presenta ningún nombre, ni datos que puedan involucrar la violación de datos confidenciales de las personas que se hicieron los exámenes de laboratorio.

# Objetivo

Éste proyecto pretende, pero no está limitado, a mostrar el Anlaisis Exploratorio de Datos (EDA por sus siglas en Inglés) y avances breves en el proceso de Extracción, Transformación y Carga de Datos (ETL por sus siglas en Inglés).

El objetivo final es ofrecer una herramienta a los médicos que interpretan resultados de pruebas de laboratorio, ayudándoles a mejorar el diagnóstico y tratamiento de sus pacientes. Para alcanzar este fin, se planea desarrollar modelos predictivos basados en algoritmos de aprendizaje automático y redes neuronales, capaces de identificar patrones patológicos o conexiones entre diferentes sistemas del cuerpo humano que estén directamente relacionados con la patología del paciente. 
Se anticipa que esta investigación aportará al avance del conocimiento científico en laboratorio y ciencia de datos. 
Los resultados serán difundidos mediante publicaciones académicas y conferencias.
________________________________________________________________________________________________________________

# Resultados del Análisis EDA

El análisis reveló cómo existen relaciones entre distintas áreas que, al principio, no parecían tan evidentes. El uso del dendrograma y las matrices de confusión son útiles para brindar herramientas para establecer dichas relaciones. No se abunda en ello en el presente proyecto, dado que abarca mayormente el EDA y ETL.
________________________________________________________________________________________________________________

# Resultados del Proyecto Final

El análisis inicial de este proyecto ya contaba con visualizaciones con el uso de Altair, y para fortalecer el análisis en este proyecto final, se utilizó Python para leer los documentos con los resultados de los pacientes en PDF y Streamlit para mostrar algunos de los resultados del análisis en una App dinámica.

Los resultados de los pacientes originalmente se generan en formato PDF, y es necesario bajar de este formato la información necesaria para este análisis, esto se desarrolla con la librería PyMuPDF de Python.

En el caso de Streamlit, esta herramienta resulta de gran valor para hacer publicaciones con resultados del análisis en una App dinámica, mediante gráficos de barras, gráficos circulares, diagramas de caja (boxplots) y tablas de resumen. 

En el siguiente gráfico se puede apreciar el análisis de resultado mostrando un gráfico de barras y un comparativo de las variables metales pesados y químicos.

![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Screenshot%202024-11-30%20074209.png)

La siguiente imagen muestra el mismo caso, pero ahora la comparativa se hace entre parásitos y esporas.

![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Screenshot%202024-11-30%20074223.png)

Estas variables de análisis en las comparativas se llevan a cabo mediante un menú despegable, mostrado en la siguiente imagen:

![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Screenshot%202024-11-30%20074234.png)

Y por último mostramos una imagen con una imagen de segmentación de pacientes, en la que se incluye vía Streamlit un diagrama circular, un gráfico de barras un boxplot 

![]( https://github.com/edd885/Tecnicas-de-machine-learning-en-an-lisis-de-resultados-de-laboratorio/blob/main/results/Screenshot%202024-11-30%20074248.png)






__________________________________________________________________________________________________________________

# Estructura general del repositorio

    ├── LICENSE                           <- MIT License.
    |  
    ├── README.md                         <- Archivo principal descriptivo del proyecto.  
    |  
    ├── CONTRIBUTE.md                     <- Cómo contribuir al proyecto.  
    |  
    ├── CITATION.md                       <- Formas de citar apropiadamente.  
    |  
    ├── data                              <- Información de los datos.  
        |── lab_analysis_github.xlsx      <- Archivo con la data del análisis
        |── README.md                     <- Descripción de la información contenida
    |
    ├── doc                               <- Archivos de texto.  
        |── README.md                     <- Descripción y planteamiento, Objetivo final, Justificación/Relevancia
    |  
    ├── results                           <- Resultados parciales obtenidos en esta etapa. 
        |── archivos.png                  <- Resultado de challenge terrorismo 
        └── README.md                     <- Resultados escritos del proyecto intermedio y final.
            |── Carpeta de resultados     <- Resultados escritos del proyecto intermedio.
            └── Result de análisis final  <- Resultados escritos del proyecto final.
    |  
    └── src                               <- Archivos de código.  
        |── eduardo_lab_analysis.ipynb    <- Jupyter Notebook con el código del análisis
        └── README.md                     <- Descripción del Jupyter Notebook.
______________________________________________________________

# Pasos realizados

1. **Obtención de resultados**: desde un archivo .xlsx se extrajeron los resultados de examen de laboratorio de 65 pacientes, cada paciente tiene 105 features a analizar en su estudio particular.
2. **Análisis**: Fueron usadas técnicas de exploración y análisis de datos en un archivo jupyter notebook, las herramientas usadas fueron Pandas, Numpy, Matplotlib, Seaborn, Altair, ScikitLearn.
3. **Visualización**: En algunas celdas fueron usadas visualizaciones con Altair, Seaborn y Matplotlib para la comparación visual del lector y elegir, a través de retroalimentación, cuál cumple mejor el objetivo de transmitir la información de manera más eficiente.

# Conclusiones
El análisis exploratorio de resultados de laboratorio ofrece una comprensión rápida y de fácil interpretación del dataset obtenido por parte del laboratorio. Los elementos clave se destacan visualmente en algunos gráficos y en la futura publicación del documento completo. En este documento no se incluyen para evitar una posible identificación de un proyecto de gran similitud con el producto final y, la relación de detección de plagio por parte de software especializado.

# Autor
- Eduardo Carlos Fletes Aréchiga. Estudiante en la Maestría en Ciencia de los Datos, Universidad de Guadalajara, Campus CUCEA.

# Fecha de presentación

20 Octubre 2024.
