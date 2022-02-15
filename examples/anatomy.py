import sys
# for development
sys.path.append('./src')
sys.path.append('../src')

from screencastscript import ScreencastScript  # noqa: E402
screencast = ScreencastScript()
"""
===================
screencast-script:
   Anatomy of a figure

https://matplotlib.org/stable/gallery/showcase/anatomy.html
===================

This figure shows the name of several matplotlib elements composing a figure
"""

screencast.i3wm_send_command("ws_2")
screencast.sleep(2)

screencast.take_screenshots(2,8)
screencast.i3wm_send_command_take_screenshots(2,"focus_right")
screencast.take_screenshots(2,12)

screencast.i3wm_send_command_take_screenshots(2,"toggle_fullscreen")
screencast.sleep(2)

screencast.send_input_take_screenshots(2,"""import numpy as np
""")

screencast.sleep(2)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""import matplotlib.pyplot as plt
""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,
    """from matplotlib.ticker import AutoMinorLocator, MultipleLocator

""")

screencast.sleep(4)
screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,"""np.random.seed(19680801)

""")

screencast.send_input_take_screenshots(2,"""X = np.linspace(0.5, 3.5, 100)
Y1 = 3 + np.cos(X)
Y2 = 1 + np.cos(1 + X / 0.75) / 2
Y3 = np.random.uniform(Y1, Y2, len(X))

""")

screencast.sleep(4)

screencast.send_input_take_screenshots(2,"""fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 1, 1, aspect=1)

""")

screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,"""def minor_tick(x, pos):
    if not x % 1.0:
return ""
return f"{x:.2f}"

""")

screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,
    """ax.xaxis.set_major_locator(MultipleLocator(1.000))
""")
screencast.send_input_take_screenshots(2,
    """ax.xaxis.set_minor_locator(AutoMinorLocator(4))
""")
screencast.send_input_take_screenshots(2,
    """ax.yaxis.set_major_locator(MultipleLocator(1.000))
""")
screencast.send_input_take_screenshots(2,
    """ax.yaxis.set_minor_locator(AutoMinorLocator(4))

""")

screencast.take_screenshots(2,4)

# FuncFormatter is created and used automatically
# ax.xaxis.set_minor_formatter(minor_tick)
# the above line throw this error (is not used in this script) :
# TypeError: 'formatter' must be an instance of matplotlib.ticker.Formatter
# not a function

screencast.send_input_take_screenshots(2,"""ax.set_xlim(0, 4)

""")

screencast.send_input_take_screenshots(2,"""ax.set_ylim(0, 4)

""")

screencast.send_input_take_screenshots(2,
    """ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

""")

screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,
    """ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)

""")
screencast.sleep(2)
screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,
    """ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")

""")
screencast.sleep(2)
screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,
    """ax.plot(X, Y3, linewidth=0, marker='o', markerfacecolor='w', markeredgecolor='k')

""")

screencast.sleep(2)
screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,
    """ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')

ax.set_xlabel("X axis label")

ax.set_ylabel("Y axis label")

""")

screencast.take_screenshots(2,4)
screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""ax.legend()

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""def circle(x, y, radius=0.15):
from matplotlib.patches import Circle
from matplotlib.patheffects import withStroke
circle = Circle((x, y),
            radius,
clip_on=False,
zorder=10,
linewidth=1,
edgecolor='black',
facecolor=(0, 0, 0, .0125),
path_effects=[withStroke(linewidth=5, foreground='w')])
←←←←←←←←←←←←ax.add_artist(circle)

""")

screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,"""def text(x, y, text):
    ax.text(x,
y,
text,
backgroundcolor="white",
ha='center',
va='top',
weight='bold',
color='blue')


""")

screencast.take_screenshots(2,4)

screencast.send_input_take_screenshots(2,"""# Minor tick
circle(0.50, -0.10)
text(0.50, -0.32, "Minor tick label")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Major tick
circle(-0.03, 4.00)
text(0.03, 3.80, "Major tick")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Minor tick
circle(0.00, 3.50)
text(0.00, 3.30, "Minor tick")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""
# Major tick label
circle(-0.15, 3.00)
text(-0.15, 2.80, "Major tick label")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# X Label
circle(1.80, -0.27)
text(1.80, -0.45, "X axis label")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Y Label
circle(-0.27, 1.80)
text(-0.27, 1.6, "Y axis label")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Title
circle(1.60, 4.13)
text(1.60, 3.93, "Title")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Blue plot
circle(1.75, 2.80)
text(1.75, 2.60, "Line\\n(line plot)")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Red plot
circle(1.20, 0.60)
text(1.20, 0.40, "Line\\n(line plot)")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Scatter plot
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\\n(scatter plot)")
""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Grid
circle(3.00, 3.00)
text(3.00, 2.80, "Grid")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Legend
circle(3.70, 3.80)
text(3.70, 3.60, "Legend")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Axes
circle(0.5, 0.5)
text(0.5, 0.3, "Axes")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""# Figure
circle(-0.3, 0.65)
text(-0.3, 0.45, "Figure")

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""color = 'blue'

ax.annotate('Spines',
             xy=(4.0, 0.35),
xytext=(3.3, 0.5),
weight='bold',
color=color,
arrowprops=dict(arrowstyle='->',
                 connectionstyle="arc3",
color=color))


""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""ax.annotate('',
            xy=(3.15, 0.0),
xytext=(3.45, 0.45),
weight='bold',
color=color,
arrowprops=dict(arrowstyle='->',
                connectionstyle="arc3",
color=color))


""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.send_input_take_screenshots(2,"""ax.text(4.0,
        -0.4,
"Made with https://matplotlib.org",
fontsize=10,
ha="right",
color='.5')

""")

screencast.send_input_take_screenshots(2,"""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2,8)

screencast.i3wm_send_command("ws_1")
