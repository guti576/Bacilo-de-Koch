from BaciloKoch import classes_df, functions_df
import seaborn as sns
import matplotlib.pyplot as plt


def plot_ORFs_per_class():
    fig = sns.barplot(data=classes_df, x="class_id", y="ORFs_in_class")
    fig.set_xticklabels(fig.get_xticklabels(), rotation=90,
                        fontweight='light', fontsize=5)

    plt.savefig('plots/test.svg', format="svg", dpi=1200)


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
