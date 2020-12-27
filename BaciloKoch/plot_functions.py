from BaciloKoch import classes_df, functions_df
import seaborn as sns
import matplotlib.pyplot as plt


def plot_ORFs_per_class():
    sns.set_theme(style="whitegrid")
    sns.barplot(data=classes_df, x="class_id", y="ORFs_in_class")
    plt.show()
