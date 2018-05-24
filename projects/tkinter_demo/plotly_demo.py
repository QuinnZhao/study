from plotly.graph_objs import *
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

x = np.random.randn(2000)
y = np.random.randn(2000)
iplot([Histogram2dContour(x=x, y=y, contours=Contours(coloring='heatmap')),
       Scatter(x=x, y=y, mode='markers', marker=Marker(color='white', size=3, opacity=0.3))], show_link=False)