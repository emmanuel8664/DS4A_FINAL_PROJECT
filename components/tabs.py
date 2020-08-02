import dash_core_components as dcc
import dash_html_components as html


from components.views.descriptive import *
from components.views.predictive import *


def build_tabs():
    return  dbc.Tabs(
            [
                dbc.Tab(build_predictive(), label="Forecast"),
                dbc.Tab(build_descriptive(), label="Information"),

            ],
            id="tabs",
            #active_tab="descriptive",
            className="navbar navbar-expand-md",
        )
