import os
import plotly.graph_objects as go
from dash import Dash, dcc, html
from rocketlogger.data import RocketLoggerData

# constants
TRIM_START = 3.0  # seconds
TRIM_END = 1.0  # seconds

# input folder
input_folder = os.path.join('./')

# input files
measurement_file = 'data/mirocard_triggered_data_app.rld'

# Load data
data = RocketLoggerData(os.path.join(input_folder, measurement_file))
data = data.merge_channels(True)
data_sample_rate = int(data._header['sample_rate'])


# RAW DATA
I_app = data.get_data('I1').squeeze()[int(TRIM_START*data_sample_rate):-int(TRIM_END*data_sample_rate)]
V_app = data.get_data('V1').squeeze()[int(TRIM_START*data_sample_rate):-int(TRIM_END*data_sample_rate)]


# TIME
t_app = data.get_time()[int(TRIM_START*data_sample_rate):-int(TRIM_END*data_sample_rate)]
t_app = t_app - t_app[0]

# POWER / ENERGY
P_app = 1000 * V_app * I_app

# Subsampling constant
# 10 seemed like a good compromise between detail
# and responsivity
sub = 10

# Main Figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=t_app[::sub], y=P_app[::sub]))


# Set title
fig.update_layout(
    title_text='Mirocard Power Measurments',
    xaxis_title='Time [ms]',
    yaxis_title='Power [mW]',
    template='plotly_white'
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True,
            autorange=True
        )
    )
)

# Run dash app and embed figure in it
app = Dash(__name__)
server = app.server
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
