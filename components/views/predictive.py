import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def build_predictive():
    return dbc.Card(
    dbc.CardBody(
        [
            html.P("Predictive", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)





# def build_predictive():
#     return [
#         html.H6("Predictive"),
#         html.Br(),
#         html.P("Here you can see a behaviour over time of the icfes results and different socioeconomic factors in all Colombia")
#     ]