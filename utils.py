## In this python file, we will start by defining the color codes for each driver, track and even the background for the website.
## We'll import these elements to other python files for references

# Figure formatting
BACKGROUND_COLOR = '#white'
FONT_COLOR = '#d42424'
GRID_COLOR = '#32383e'
GRID_WIDTH = 1

# Plot colors
RED_COLORS = ['white', 'darkred']
RED_COLORS_REVERSED = ['darkred', 'white']

COMPOUND_COLORS = [[0, 'red'], [0.5, 'yellow'], [1, 'white']]

GEAR_SHIFT_COLORS = [
    [0, '#8a1fdb'],
    [1.0 / 7, '#541fdb'],
    [2.0 / 7, '#1f25db'],
    [3.0 / 7, '#1fbcdb'],
    [4.0 / 7, '#1fdb4b'],
    [5.0 / 7, '#dbc51f'],
    [6.0 / 7, '#db7a1f'],
    [1, '#db1f1f']
]

DRIVER_COLORS = {
    '2023': {
        'HAM': 'rgba(0, 210, 190, 0.9)',
        'RUS': 'rgba(0, 210, 190, 0.9)',
        'LEC': 'rgba(220, 0, 0, 0.9)',
        'SAI': 'rgba(220, 0, 0, 0.9)',
        'VER': 'rgba(6, 0, 239, 0.9)',
        'PER': 'rgba(6, 0, 239, 0.9)',
        'GAS': 'rgba(0, 144, 255, 0.9)',
        'OCO': 'rgba(0, 144, 255, 0.9)',
        'HUL': 'rgba(255, 255, 255, 0.9)',
        'MAG': 'rgba(255, 255, 255, 0.9)',
        'ALO': 'rgba(0, 111, 98, 0.9)',
        'STR': 'rgba(0, 111, 98, 0.9)',
        'DEV': 'rgba(43, 69, 98, 0.9)',
        'TSU': 'rgba(43, 69, 98, 0.9)',
        'NOR': 'rgba(255, 135, 0, 0.9)',
        'PIA': 'rgba(255, 135, 0, 0.9)',
        'BOT': 'rgba(144, 0, 0, 0.9)',
        'ZHO': 'rgba(144, 0, 0, 0.9)',
        'SAR': 'rgba(0, 90, 255, 0.9)',
        'ALB': 'rgba(0, 90, 255, 0.9)',
        'DRU': 'rgba(0, 111, 98, 0.9)'
    }
}

TRACK_STATUS_COLORS = {
    'Red': 'rgba(238, 75, 43, 0.25)',
    'Yellow': 'rgba(255, 255, 0, 0.25)',
    'Safety': 'rgba(255, 255, 255, 0.25)',
    'Virtual': 'rgba(255, 255, 255, 0.25)'
}

TRACK_COLOR = 'white'
TURN_COLOR = '#8803fc'

# Other plot formatting
MIN_GAP = 180
MAX_GAP = -10
MIN_SPEED = 50
MAX_SPEED = 350
MARKER_SIZE = 4
LINE_WIDTH = 2

PARAM_FORMAT = {
    'Speed': {
        'name': 'Speed',
        'hovertemplate_prefix': 'Speed: ',
        'hovertemplate_suffix': 'kph',
        'colorscale': RED_COLORS_REVERSED,
        'cmin': MIN_SPEED,
        'cmax': MAX_SPEED,
        'colorbar_title': 'Speed (kph)',
        'ymin': MIN_SPEED,
        'ymax': MAX_SPEED + 85,
        'ytitle': 'Speed (kph)'
    },
    'Throttle': {
        'name': 'Throttle',
        'hovertemplate_prefix': 'Throttle: ',
        'hovertemplate_suffix': '%',
        'colorscale': RED_COLORS_REVERSED,
        'cmin': 0,
        'cmax': 100,
        'ymax': 100.25,
        'colorbar_title': 'Throttle (%)',
        'ymin': -.25,
        'ytitle': 'Throttle (%)'
    },
    'Brake': {
        'name': 'Brake',
        'hovertemplate_prefix': 'Brake: ',
        'hovertemplate_suffix': '%',
        'colorscale': RED_COLORS_REVERSED,
        'colorbar_title': 'Brake (%)',
        'cmin': 0,
        'cmax': 100,
        'ymin': -.25,
        'ymax': 100.25,
        'ytitle': 'Brake (%)'
    },
    'Gear': {
        'name': 'nGear',
        'hovertemplate_prefix': '<i>Gear</i>: ',
        'hovertemplate_suffix': '',
        'colorscale': GEAR_SHIFT_COLORS,
        'cmin': 1,
        'cmax': 8,
        'colorbar_title': 'Gear',
        'ymin': 0.5,
        'ymax': 8.5,
        'ytitle': 'Gear'
    }
}
