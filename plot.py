import pandas as pd
import numpy as np
import plotly.graph_objects as go
from utils import *

def get_blank_fig():
    
    fig = go.Figure()
    
    fig.update_layout(
        plot_bgcolor = background_color,
        paper_bgcolor = background_color,
        font_color =font_color
    )
    
    