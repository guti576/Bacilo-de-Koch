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
   
## Instalación
Las dependencias del proyecto se encuentran recogidas en el fichero _requirements.txt_ . Para proceder
con la instalación ejecute el siguiente comando:

`pip install -r requirements.txt`

## Testing
El paquete incluye una serie de test unitarios que garantizan el correcto funcionamiento de las funciones recogidas
en el paquete. Además, se ha hecho uso de la librería Coverage.py para evaluar el grado de cobertura de los tests
definidos. Para conocer más detalles del paquete Coverage.py consulte la documentación oficial en la página 
[https://coverage.readthedocs.io/en/coverage-5.3.1/]()

Para lanzar los test, ejecutar el siguiente comando en un terminal:

`coverage run -m unittest discover`

Esto generará un informe que se puede consultar mediante el siguiente comando:

`coverage report -m`

## Licencia
El material recogido en este repositorio se recoge bajo licenciamiento 
Creative Commons Atribución/Reconocimiento-NoComercial-CompartirIgual 4.0 Licencia Pública Internacional — CC BY-NC-SA 4.0

Consulte la página [https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.es]() para más información
o bien lea el archivo license.txt 



