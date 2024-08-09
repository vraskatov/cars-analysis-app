from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from layout_elements.layout_elements import (cars_sold_card, sales_sum_card, best_model_card,
                                             best_make_card, all_years_button, year_dropdown,
                                             )
from layout_elements.graph_style import graph_style

# App Structure:
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY,
                                           'assets/style.css'],
           meta_tags=[dict(name='viewport',
                           content='width=device-width, intial-scale=1.0')]
           )

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2({},
                        'title-of-page',
                        className='text-center text-success my-4'),
                width=12)
    ]),
    dbc.Row([
        dbc.Col(cars_sold_card, width=3),
        dbc.Col(sales_sum_card, width=3),
        dbc.Col(best_model_card, width=3),
        dbc.Col(best_make_card, width=3),
    ]),
    # Gleiche Farben für gleiche Kategorien
    dbc.Row([
        dbc.Col(
            dcc.Graph('offer-pie', figure={}, style=graph_style),
            width=12, lg=6, className='mb-4'),

        dbc.Col(
            dcc.Graph('fuel-bars', figure={}, style=graph_style),
            width=12, lg=6, className='mb-4')
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph('mileages-pie', figure={}, style=graph_style),
            width=12, lg=6, className='mb-4'),
        dbc.Col(
            dcc.Graph('line_or_box', figure={}, style=graph_style),
            width=12, lg=6, className='mb-4'),
    ]),
    dbc.Row([
        dbc.Col(year_dropdown, width=10),
        dbc.Col(all_years_button, width=2)
    ]),
    # Bar Chart with Sum of Sales for each year
    #### THIS ONE IS NOT USED YET
    #     dbc.Col(
    #         dcc.Graph(figure=sums_over_time),
    #         width=12, lg=6),
])


if __name__ == '__main__':
    app.run(debug=True)
