from BaciloKoch import classes_df, functions_df
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_ORFs_per_class(action='save'):
    '''
    Función que nos permite representar el número de ORFs que pertenecen a cada clase. Debido al
    extenso número de clases, se ha subdividido las clases en tres grupos diferentes, aportando mayor
    legibilidad al conjunto. El tipo de gráfica escogido es de barras, que nos permite detectar
    fácilmente clases con más o menos ORFs asociados.

    @:param action: si "save" se guarda el gráfico en la carpeta "plot". En caso contrario
    se muestra por pantalla el gráfico.
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

    if action == "save":
        plt.savefig('plots/ORFs_por_clase.png')
    else:
        plt.show(block=False)


def bar_two_axis(resultDict, labels):

    df = pd.DataFrame(data=resultDict)

    # plot
    ax = df.plot(kind='bar', secondary_y=['Número de clases'])
    ax.set_ylabel('Promedio de ORFs relacionanado')
    ax.right_ax.set_ylabel('Número de clases')

    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xticklabels(labels, rotation=0)

    plt.show(block=True)
