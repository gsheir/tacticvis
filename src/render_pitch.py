import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def render_pitch(
    length=120,
    width=80,
    metric="yards",
    pitch_theme="light",
    linecolor="black",
    ax_colour="white",
    figsize=(10, 5),
    figax=None,
):

    """
    Creates a vertical football pitch.

    Parameters:
        pitch_length (integer): length of pitch in yards
        pitch_width (integer): width of pitch in yards
        metric (string): specify distance metric, yards (or metres - not yet available)
        pitch_theme (string): specify 'light' or 'dark' to auto set pitch and line colours
        linecolor (string): specify colour for pitch lines
        ax_colour (string): specify colour for axes background colour
        figsize (tuple): specify (width, height) of figure
        figax (tuple): specify previous (fig, ax) to start from

    """

    if figax == None:
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)
        ax.xlim = (0, length)
        ax.ylim = (0, width)
    else:
        fig, ax = figax

    if pitch_theme == "light":
        linecolor = "black"
        ax_colour = "white"
    elif pitch_theme == "dark":
        linecolor = "white"
        ax_colour = "#303030"

    ax.set_facecolor(ax_colour)

    # Pitch Outline & Centre Line
    ax.plot([0, length], [0, 0], color=linecolor)
    ax.plot([length, length], [0, width], color=linecolor)
    ax.plot([length, 0], [width, width], color=linecolor)
    ax.plot([0, 0], [width, 0], color=linecolor)
    ax.plot([length / 2, length / 2], [0, width], color=linecolor)

    # Left Penalty Area
    ax.plot([18, 18], [width / 2 + 22, width / 2 - 22], color=linecolor)
    ax.plot([0, 18], [width / 2 + 22, width / 2 + 22], color=linecolor)
    ax.plot([0, 18], [width / 2 - 22, width / 2 - 22], color=linecolor)

    # Right Penalty Area
    ax.plot(
        [length - 18, length - 18], [width / 2 + 22, width / 2 - 22], color=linecolor
    )
    ax.plot([length - 18, length], [width / 2 + 22, width / 2 + 22], color=linecolor)
    ax.plot([length - 18, length], [width / 2 - 22, width / 2 - 22], color=linecolor)

    # Left 6 yard box Area
    ax.plot([6, 6], [width / 2 + 10, width / 2 - 10], color=linecolor)
    ax.plot([0, 6], [width / 2 + 10, width / 2 + 10], color=linecolor)
    ax.plot([0, 6], [width / 2 - 10, width / 2 - 10], color=linecolor)

    # #Top Penalty Area
    ax.plot([length - 6, length - 6], [width / 2 + 10, width / 2 - 10], color=linecolor)
    ax.plot([length - 6, length], [width / 2 + 10, width / 2 + 10], color=linecolor)
    ax.plot([length - 6, length], [width / 2 - 10, width / 2 - 10], color=linecolor)

    # #Prepare Circles; 10 yards distance. penalty on 12 yards
    centreCircle = plt.Circle((length / 2, width / 2), 10, color=linecolor, fill=False)
    centreSpot = plt.Circle((length / 2, width / 2), 0.8, color=linecolor)
    bottomPenSpot = plt.Circle((12, width / 2), 0.8, color=linecolor)
    topPenSpot = plt.Circle((length - 12, width / 2), 0.8, color=linecolor)

    # #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(bottomPenSpot)
    ax.add_patch(topPenSpot)

    # #Prepare Arcs
    bottomArc = Arc(
        (11, width / 2),
        height=20,
        width=20,
        angle=270,
        theta1=48,
        theta2=132,
        color=linecolor,
    )
    topArc = Arc(
        (length - 11, width / 2),
        height=20,
        width=20,
        angle=270,
        theta1=228,
        theta2=312,
        color=linecolor,
    )

    # #Draw Arcs
    ax.add_patch(bottomArc)
    ax.add_patch(topArc)

    # Tidy Axes
    plt.xticks([])
    plt.yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.set_aspect("equal")

    return fig, ax


if __name__ == "__main__":
    fig, ax = render_pitch()
    plt.show()
