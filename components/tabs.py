import dash_core_components as dcc
import dash_html_components as html


from components.views.descriptive import *
from components.views.diagnostic import *
from components.views.predictive import *


def build_tabs():
    print('Construcción de la página')
    return  dbc.Tabs(
            [
                dbc.Tab(build_descriptive(), label="Descriptivo"),
                dbc.Tab(build_diagnostic(), label="Diagnóstico"),
                dbc.Tab(build_predictive(), label="Predictive"),
            ],
            id="tabs",
            active_tab="descriptive",
            className="navbar navbar-expand-md",
        )





# def build_tabs():
#     return dcc.Tabs(
#         id="tabs",
#         value='descriptive',
#         children=[
#             dcc.Tab(label='Descriptive', value='descriptive'),
#             dcc.Tab(label='Diagnostic', value='diagnostic'),
#             dcc.Tab(label='Predictive', value='predictive')
#         ],
#         colors={
#             "border": "white",
#             "primary": "white",
#             "background": "Gainsboro"
#         }
#     )


# def build_content_for_tab(tab_name):
#     if tab_name == 'descriptive':
#         return build_descriptive()
#     elif tab_name == 'diagnostic':
#         return build_diagnostic()
#     elif tab_name == 'predictive':
#         return build_predictive()