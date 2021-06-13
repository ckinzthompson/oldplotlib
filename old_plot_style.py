## how to: import plot_style at the start of a file

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')
matplotlib.rcParams["axes.spines.right"] = False
matplotlib.rcParams["axes.spines.top"] = False

width = 1.5
fontsize = 12
matplotlib.rcParams["font.family"] ='Helvetica'
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["figure.figsize"] = (4,3)
matplotlib.rcParams["axes.labelsize"] = 20
matplotlib.rcParams["lines.linewidth"] = width
matplotlib.rcParams["lines.markersize"] = 10
matplotlib.rcParams["xtick.labelsize"] = fontsize
matplotlib.rcParams["ytick.labelsize"] = fontsize
matplotlib.rcParams["axes.labelsize"] = fontsize + 2
matplotlib.rcParams["xtick.major.width"] = width
matplotlib.rcParams["ytick.major.width"] = width
matplotlib.rcParams["axes.linewidth"] = width
matplotlib.rcParams["figure.subplot.left"] = .175
matplotlib.rcParams["figure.subplot.right"] = .9
matplotlib.rcParams["figure.subplot.bottom"] = .175
matplotlib.rcParams["figure.subplot.top"] = .9
