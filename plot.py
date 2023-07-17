import pandas as pd
import numpy as np
import plotly.graph_objects as go
from utils import *

def get_default_fig():
    """
    Returns a figure with app's default formatting.
    """
    fig = go.Figure()

    fig.update_layout(
        plot_bgcolor=BACKGROUND_COLOR,
        paper_bgcolor=BACKGROUND_COLOR,
        font_color=FONT_COLOR
    )

    return fig

def get_blank_fig():
    """
   The function get_blank_fig() returns a blank figure with specified background color, font color, and axis settings.
    The function first creates a blank figure object using the go.Figure() function.
    Then, the function updates the layout of the figure to set the background color, font color, and axis settings.
    The background color and font color are set using the plot_bgcolor and font_color parameters, respectively.
    The axis settings are set using the showgrid, showticklabels, and zeroline parameters.
    Finally, the function returns the figure object.
    """
    
    fig = go.Figure()
    
    fig.update_layout(
        plot_bgcolor = BACKGROUND_COLOR,
        paper_bgcolor = BACKGROUND_COLOR,
        font_color =FONT_COLOR
    )
    
    fig.update_xases(
        showgrid =False,
        showticklabels = False,
        zeroline = False
        )
    fig.update_yaxes(
        showgrid = False,
        showticklabels = False,
        zeroline = False
    )
    
    return fig

def get_no_data_fig():
    """Returns a message as a figure that the requested race data is not available"""
    
    fig = {
        'layout':{
            'xaxis':{
                'visible':False
            },
            'yaxis': {
                'visible':False
            },
            'annotations':[
                {
                    'text':'No Data Available',
                    'xref': 'paper',
                    'yref':'paper',
                    'showarrow':'False',
                    'font': {
                        'size': 20
                    }
                    }
            ],
            'plot_bgcolor':BACKGROUND_COLOR,
            'paper_bgcolor':BACKGROUND_COLOR
            }
    }
    return fig