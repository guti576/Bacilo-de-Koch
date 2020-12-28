from BaciloKoch import classes_df, functions_df
import seaborn as sns
import matplotlib.pyplot as plt


def plot_ORFs_per_class():

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

    #plt.savefig('plots/test.svg', format="svg", dpi=1200)
    plt.show()


def plot_pie_from_dict(dict):
    categorias = list(dict.keys())
    valores = list(dict.values())

    plt.pie(valores, labels=categorias, autopct='%1.1f%%')
    plt.show()


def pairGrid():
    g = sns.PairGrid(classes_df.sort_values("ORFs_in_class", ascending=False),
                     x_vars=["ORFs_in_class"], y_vars=["class_id"],
                     height=10, aspect=.25)

    # Draw a dot plot using the stripplot function
    g.map(sns.stripplot, size=10, orient="h", jitter=False,
          palette="flare_r", linewidth=1, edgecolor="w")

    sns.despine(left=True, bottom=True)
    plt.show()


def pairGrid2():
    fig, axs = plt.subplots(ncols=2)
    sns.PairGrid(classes_df.sort_values("ORFs_in_class", ascending=False),
                     x_vars=["ORFs_in_class"], y_vars=["class_id"],
                     height=10, aspect=.25, ax=axs[0])

    sns.PairGrid(classes_df.sort_values("ORFs_in_class", ascending=False),
                 x_vars=["ORFs_in_class"], y_vars=["class_id"],
                 height=10, aspect=.25, ax=axs[1])

    # Draw a dot plot using the stripplot function
    g.map(sns.stripplot, size=10, orient="h", jitter=False,
          palette="flare_r", linewidth=1, edgecolor="w")

    sns.despine(left=True, bottom=True)
    plt.show()
