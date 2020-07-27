import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.filters import Filter
from components.data_controllers.diagnostic_data import diagnostic_data
from components.plots import diagnostic_plots

diagnostic_data = diagnostic_data()
filtro = Filter()

def build_diagnostic():
    #return get_filtros()
    return dbc.Card(
        html.Div
        (
            [
                dbc.Row
                (
                    [
                        dbc.Col
                        (
                            html.Div
                            (
                                filtro.get_filtro()
                            ),
                            md=4
                        ),
                        dbc.Col
                        (
                            html.Div
                            (
                                id="diagnostic-right-column",
                                className="eight columns",
                                children=build_content()
                            ),
                        )
                        # dbc.Col(html.Div([
                        # dcc.Graph(figure=fig)
                        # ]),md=8)
                        #dbc.Col(dbc.Row([dbc.Col(html.Div("Content1"),md=6),dbc.Col(html.Div("Content2"),md=6)]),md=8),
                    ]
                ),
            ]
        )
    )

def build_content():
    figuras = get_figuras()
    return [
        dbc.Row
        (
            [
                dbc.Col
                (
                    html.Div
                    (
                        dcc.Graph(figure=figuras['bar'])
                    ),
                    md=12
                ),
                dbc.Col
                (
                    html.Div
                    (
                        #dcc.Graph(figure=figuras['boxplot'])
                    ),
                    md=12
                ),
                dbc.Col
                (
                    html.Div
                    (
                        #children = [dcc.Graph(figure=figuras['scatter'])]
                    ),
                    md=12
                )
            ]
        )
    ]

def get_figuras():
    figuras = {}
    figuras['bar'] = get_bar()
    #figuras['boxplot'] = get_boxplot()
    #figuras['scatter'] = get_scatter()
    return figuras

def get_bar():
    df = diagnostic_data.get_bar()
    histograma = diagnostic_plots.get_bar(df, diagnostic_data.get_eje_x(), diagnostic_data.get_eje_y())
    return histograma

def get_boxplot():
    df = diagnostic_data.get_boxplot()
    boxplot = diagnostic_plots.get_boxplot(df, diagnostic_data.get_eje_x(), diagnostic_data.get_eje_y())
    return boxplot

def get_scatter():
    df = diagnostic_data.get_scatter()
    scatter = diagnostic_plots.get_scatter(df, diagnostic_data.get_eje_x(), diagnostic_data.get_eje_y())
    return scatter

# def build_diagnostic():
#     return [
#         html.H6("Diagnostic"),
#         html.Br(),
#         html.P("Here you can see a behaviour over time of the icfes results and different socioeconomic factors in all Colombia")
#     ]