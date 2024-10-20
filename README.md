# ML_in_laboratory

Repositorio con análisis exploratorio para exámenes de laboratorio y sus correlaciones. 

Autor: Eduardo Carlos Fletes Aréchiga

e-mail: eduardo.fletes1892@alumnos.udg.mx
________________________________________________________________________________________________________________

Proyecto para la Maestría en Ciencias de los Datos, Universidad de Guadalajara

El proyecto presenta un análisis exploratorio de datos obtenidos de resultados de estudios sobre estudios de laboratorio.
Ningún nombre, ni datos que puedan involucrar la violación de datos confidenciales ha sido utilizado para la exposición de éste análisis.

# Objetivo

Éste proyecto pretende, pero no está limitado a, mostrar el EDA y avances breves en el proceso ETL

El objetivo final es ofrecer una herramienta a los médicos que interpretan resultados de pruebas de laboratorio, ayudándoles a mejorar el diagnóstico y tratamiento de sus pacientes. Para alcanzar este fin, se planea desarrollar modelos predictivos basados en algoritmos de aprendizaje automático y redes neuronales, capaces de identificar patrones patológicos o conexiones entre diferentes sistemas del cuerpo humano que estén directamente relacionados con la patología del paciente. 
Se anticipa que esta investigación aportará al avance del conocimiento científico en laboratorio y ciencia de datos. 
Los resultados serán difundidos mediante publicaciones académicas y conferencias.



__________________________________________________________________________________________________________________


# Estructura general del repositorio

├── LICENSE           <- MIT License.  
|  
├── README.md         <- Archivo principal descriptivo del proyecto.  
|  
├── CONTRIBUTE.md   <- Cómo contribuir al proyecto.  
|  
├── CITATION.md       <- Formas de citar apropiadamente.  
|  
├── data              <- Información de los datos.  
|  
├── doc               <- Archivos de texto.  
|  
├── results           <- Resultados parciales obtenidos en ésta etapa.  
|  
└── src               <- Archivos código.  

______________________________________________________________

# Pasos realizados

1. **Obtención de resultados**: desde un archivo .xlsx se extrajeron los resultados de examen de laboratorio de 65 pacientes, cada paciente tiene 105 features a analizar en su estudio particular.
2. **Análisis**: Fueron usadas técnicas de exploración y análisis de datos en un archivo jupyter notebook, las herramientas usadas fueron Pandas, Numpy, Matplotlib, Seaborn, Altair, ScikitLearn.
3. **Visualización**: En algunas celdas fueron usadas visualizaciones con Altair, Seaborn y Matplotlib para la comparación visual del lector y elegir, a través de retroalimentación, cuál cumple mejor el objetivo de transmitir la información de manera más eficiente.

# Resultados
El análisis reveló cómo existen relaciones entre distintas áreas que, al principio, no parecían tan evidentes. El uso del dendrograma y las matrices de confusión son útiles para brindar herramientas para establecer dichas relaciones. No se abunda en ello en el presente proyecto, dado que abarca mayormente el EDA y ETL.

# Conclusiones
El análisis exploratorio de resultados de laboratorio ofrece una comprensión rápida y de fácil interpretación del dataset obtenido por parte del laboratorio. Los elementos clave se destacan visualmente en algunos gráficos y en la futura publicación del documento completo. En este documento no se incluyen para evitar una posible identificación de un proyecto de gran similitud con el producto final y, la relación de detección de plagio por parte de software especializado.

# Autor
- Eduardo Carlos Fletes Aréchiga. Estudiante en la Maestría en Ciencia de los Datos, Universidad de Guadalajara, Campus CUCEA.

# Fecha de presentación

20 Octubre 2024.
