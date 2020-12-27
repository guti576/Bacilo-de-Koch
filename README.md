# Bacilo-de-Koch

## Introducción
Este paquete Python permite realizar un **análisis de datos con información genética sobre el Bacilo de Koch**.
En particular, de las pautas abiertas de lectura de los genes del Bacilo de Koch. Se puede ampliar información en el 
siguiente enlace: [https://es.wikipedia.org/wiki/Mycobacterium_tuberculosis]()

![Bacilo de Koch](data/bacilo_pic.jpg)

## Módulos del paquete
El paquete está constituido por los
siguientes módulos:

1. **_read_functions_**: funciones para cargar la información sobre "clases" y "funciones" del
   Bacilo de Koch. La información  leída de los ficheros origen se inserta en dataFrames de pandas
   que nos permitirán realizar cálculos y representaciones de forma sencilla. Se ha escogido esta
   metodología de trabajo por ser una librería ampliamente utilizada en la comunidad.

2. **_calc_functions_**: implementa funciones que nos permiten realizar cálculos en relación a las
   "clases" y "funciones" del Bacilo de Kock.

3. **_plot_functions_**: funciones que permite la representación gráfica de resultados. Se hace uso
    de la librería seaborn, ampliamente utilizada en la comunidad de científicos de datos y que
   presenta un nivel superior de abstracción sobre matplotlib.



