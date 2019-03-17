import matplotlib.pyplot as plt


def plot_time_series(series_to_plot,
                     create_plot=True, show_plot=True, summary_stats=False,
                     color='blue', linestyle='-', linewidth=1, alpha=1,
                     title="", ylabel="", xlabel="Date", label_size=14,
                     x_log=False, y_log=False,
                     highlight_0=True, highlight_0_color='black',
                     minmax=True, mean=True, median=True, units="",
                     highlight=None, caption_lift=1.03, ax=None):
    """
    a function to plot a line plot of provided time series

    (optional) highlights a period of time with an orange rectangle
    (optional) plots minmax, mean, median of the provided Series
    (optional) x and y axes can (separately) be set to logarithmic scales
    :type ax: matplotlib axis
    """
    if summary_stats:
        print(ylabel, "summary statistics")
        print(series_to_plot.describe())

    # set font parameters
    font = dict(family='serif', color='darkred', weight='normal', size=16)

    if create_plot:
        # create figure and axis
        f, ax = plt.subplots(1, figsize=(8, 8))

    # plot the time series
    ax.plot(series_to_plot, color=color, linestyle=linestyle,
            linewidth=linewidth, alpha=alpha)

    if y_log:
        # set y scale to logarithmic
        ax.set_yscale('log')

    if x_log:
        # set x scale to logarithmic
        ax.set_xscale('log')

    if highlight_0:
        # draw a horizontal line at 0
        ax.axhline(0, linestyle='--', linewidth=2, color=highlight_0_color)

    if minmax:
        # highlight min and max
        ser_min = series_to_plot.min()
        ax.axhline(ser_min, linestyle=':', color='red')
        ax.text(series_to_plot.index[len(series_to_plot) // 3], ser_min * caption_lift,
                "Min: {0:.2f}{1}".format(ser_min, units), fontsize=14)
        ser_max = series_to_plot.max()
        ax.axhline(series_to_plot.max(), linestyle=':', color='green')
        ax.text(series_to_plot.index[len(series_to_plot) // 3], ser_max * caption_lift,
                "Max: {0:.2f}{1}".format(ser_max, units), fontsize=14)

    if mean:
        # plot Series mean
        ser_mean = series_to_plot.mean()
        ax.axhline(ser_mean, linestyle='--', color='deeppink')
        ax.text(series_to_plot.index[len(series_to_plot) // 3], ser_mean * caption_lift,
                "Mean: {0:.2f}{1}".format(ser_mean, units), fontsize=14)

    if median:
        # plot Series median
        ser_median = series_to_plot.median()
        ax.axhline(ser_median, linestyle=':', color='blue')
        ax.text(series_to_plot.index[int(len(series_to_plot) * 0.7)], ser_median * caption_lift,
                "Median: {0:.2f}{1}".format(ser_median, units), fontsize=14)

    if highlight:
        ax.axvline(highlight[0], alpha=0.5)
        ax.text(highlight[0], series_to_plot.max() / 2,
                highlight[0], fontsize=14,
                ha='right')
        ax.axvline(highlight[1], alpha=0.5)
        ax.text(highlight[1], series_to_plot.min() / 2,
                highlight[1], fontsize=14,
                ha='left')
        ax.fill_between(highlight, series_to_plot.min() * 1.1,
                        series_to_plot.max() * 1.1, color='orange', alpha=0.2)

    # set axis parameters
    ax.set_title(title, fontdict=font)
    ax.set_xlabel(xlabel, fontdict=font)
    ax.set_ylabel(ylabel, fontdict=font)
    ax.tick_params(labelsize=label_size)

    if show_plot:
        plt.show()