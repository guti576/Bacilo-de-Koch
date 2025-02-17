from BaciloKoch import classes_df, functions_df
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_ORFs_per_class():
    '''
    Función que nos permite representar el número de ORFs que pertenecen a cada clase. Debido al
    extenso número de clases, se ha subdividido las clases en tres grupos diferentes, aportando mayor
    legibilidad al conjunto. El tipo de gráfica escogido es de barras, que nos permite detectar
    fácilmente clases con más o menos ORFs asociados.
    '''

    fig, axs = plt.subplots(ncols=3)

    first_third = round(classes_df.shape[0]/3)
    second_third = first_third + round(classes_df.shape[0]/3)

    sns.barplot(data=classes_df[:first_third], y="class_id", x="ORFs_in_class", ax=axs[0])
    sns.barplot(data=classes_df[(first_third+1):second_third], y="class_id", x="ORFs_in_class", ax=axs[1])
    sns.barplot(data=classes_df[(second_third+1):], y="class_id", x="ORFs_in_class", ax=axs[2])

    # Definimos los ejes para mayor legibilidad
    axs[0].set_yticklabels(axs[0].get_yticklabels(), fontweight='light', fontsize=7)
    axs[1].set_yticklabels(axs[1].get_yticklabels(), fontweight='light', fontsize=7)
    axs[2].set_yticklabels(axs[2].get_yticklabels(), fontweight='light', fontsize=7)

    axs[0].set_xlabel("")
    axs[1].set_xlabel("Número de ORFs por clase")
    axs[2].set_xlabel("")
    axs[0].set_ylabel("Clase")
    axs[1].set_ylabel("")
    axs[2].set_ylabel("")

    plt.show(block=False)


def bar_two_axis(resultDict, labels):
    '''
    Función que permite representar, para cada tipo de patrón requerido, el número de clases
    que pertenecen al mismo y el promedio de ORFs relacionado. Se emplea una gráfica de barras
    con dos ejes (derecha e izquierda). Por tanto, para cada parámetro tendremos dos barras
    asociadas.
    :param resultDict: diccionario con los valores a representar
    :param labels: etiquetas que pondremos a cada patrón representado
    '''

    df = pd.DataFrame(data=resultDict)

    # Definimos el segundo eje
    ax = df.plot(kind='bar', secondary_y=['Número de clases']) # legend=None
    ax.set_ylabel('Promedio de ORFs relacionanado')
    ax.right_ax.set_ylabel('Número de clases')
    ax.right_ax.legend(["Número de clases"], loc=10, bbox_to_anchor=(0.8, 1.1))

    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xticklabels(labels, rotation=0)
    ax.legend(loc=10, bbox_to_anchor=(0.2, 1.1))

    plt.show(block=False)


def plot_bar_chart(dict):
    '''
    Simple gráfica de barras que permite representar los resultados del ejercicio 3.
    :param dict: diccionario con los valores resultantes para cada valor de M
    '''

    df = pd.DataFrame(data=dict)

    plt.figure()
    sns.barplot(data=df, x="M", y="Num. de clases")
    plt.show(block=True)


def plot_exercise_separator(number):
    '''
    Imprime una cabecera por pantalla para diferencias los distintos ejercicios que se
    plantean en la práctica.
    :param number: número del ejercicio
    '''
    print("\n")
    print("*" * 30)
    print("Ejercicio " + number)
    print("*" * 30)
    print("\n")
