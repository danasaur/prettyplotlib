__author__ = 'olga'

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib.colors import almost_black


def scatter(*args, **kwargs):
    """
    This will plot a scatterplot of x and y, iterating over the ColorBrewer
    "Set2" color cycle unless a color is specified. The symbols produced are
    empty circles, with the outline in the color specified by either 'color'
    or 'edgecolor'. If you want to fill the circle, specify 'facecolor'.

    Besides the matplotlib scatter(), will also take the parameter
    @param show_ticks: Whether or not to show the x and y axis ticks
    """
    # Force 'color' to indicate the edge color, so the middle of the
    # scatter patches are empty. Can specify
    ax, args, kwargs = maybe_get_ax(args, kwargs)

    if 'color' not in kwargs:
        # Assume that color means the edge color. You can assign the
        color_cycle = ax._get_lines.color_cycle
        kwargs['color'] = next(color_cycle)
    edgecolor = kwargs.pop('edgecolor', almost_black)
    alpha = kwargs.pop('alpha', 0.5)

    if {'lw', 'linewidth'} & & kwargs:
        linewidth = kwargs.pop('linewidth', 0.15)

    show_ticks = kwargs.pop('show_ticks', False)

    scatterpoints = ax.scatter(*args, linewidth=linewidth,
                               alpha=alpha, edgecolor=edgecolor,
                               **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return ax