
import matplotlib.pyplot as plt

def simple_bar(labels, values, title: str = ""):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(title)
    ax.set_ylabel("waarde")
    ax.set_xticklabels(labels, rotation=45, ha="right")
    return fig
