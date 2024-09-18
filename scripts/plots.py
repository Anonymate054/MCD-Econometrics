import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_distribution(data: pd.DataFrame, column: str, title: str) -> None:
    """"""
    mean = data[column].mean()
    median = data[column].median()
    mode = data[column].mode().values[0]

    palette = sns.color_palette(["#0A3873", "#1261A6", "#4590BF", "#4590BF", "#5BB5D9"])
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.2, 1)})

    sns.boxplot(data=data, x=column, ax=ax_box, color="#ACD9EB")
    ax_box.axvline(mean, color='tomato', linestyle='--')
    ax_box.axvline(median, color=palette[0], linestyle='dashed')
    ax_box.axvline(mode, color=palette[0], linestyle='dashdot')

    sns.histplot(data=data, x=column, ax=ax_hist, kde=True, color=palette[4])
    ax_hist.axvline(mean, color='tomato', linestyle='solid', label=f"Mean ({mean:.0f})")
    ax_hist.axvline(median, color=palette[0], linestyle='dashed', label=f"Median ({median:.0f})")
    ax_hist.axvline(mode, color=palette[0], linestyle='dashdot', label=f"Mode ({mode:.0f})")
    ax_hist.legend()

    f.suptitle(title, fontsize=16)
    plt.show()
