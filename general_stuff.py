import matplotlib.pyplot as plt

def fix_plot(ax):
    ax.tick_params(which="minor", direction="in", length=3, width=1.3,)
    ax.tick_params(which="major", direction="in", length=6, width=1.3)
    ax.tick_params(which="minor", direction="in", length=3, width=1.3,)
    ax.tick_params(which="major", direction="in", length=6, width=1.3)
    plt.setp(ax.spines.values(), linewidth=1.3)
    plt.setp(ax.spines.values(), linewidth=1.3)