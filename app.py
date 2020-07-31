import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from components.tabs import *
#from components.callbacks.filter-callbacks import register_filter_callbacks
from components.callbacks.descriptive_callbacks import register_descriptive_callbacks



app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])


server = app.server
app.config['suppress_callback_exceptions']=True

# Layout

app.layout = dbc.Container(
    [
        build_tabs(),
        html.Div(id="tab-content", className="p-12")
    ],
    fluid=True,
    style={"height": "100vh"},
)

# app.layout = html.Div(
#     [
#         html.Div(build_tabs()),
#         html.Div(children=build_descriptive(), id="app-content")
#     ],
#     id="mainContainer",
#     style={"display": "flex", "flex-direction": "column"},
# )

#register_filter_callbacks(app)
register_descriptive_callbacks(app)

# Main
if __name__ == "__main__":
    app.run_server(debug=True)
