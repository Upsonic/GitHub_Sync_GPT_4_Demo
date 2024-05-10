def plot_hist(data, column, bins=10):
    plt.hist(data[column], bins=bins)
    plt.show()
