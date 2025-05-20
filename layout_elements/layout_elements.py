import plotly.express as px
import dash
from dash import callback, Output, Input, ctx
import dash_bootstrap_components as dbc

from .stylings import common_graph_layout
from data.data_basis import all_years, cars_df


# B: Cards
# ----------
def create_card(header, element_id):
    return dbc.CardBody([
        dbc.CardHeader(header),
        dbc.Card(id=element_id, className='text-center text-success my-4')
    ])


# Task: Uniform looking cards in mobile view!
cars_sold_card = create_card('Cars Sold', 'cars-sold')
sales_sum_card = create_card('Total Sales', 'sum-sales')
best_model_card = create_card('Bestseller Model', 'best-model')
best_make_card = create_card('Bestseller Make', 'best-make')

test_card = create_card('Card for testing', 'test-card')



# Setting all cards to choice time:
@callback(
    Output('cars-sold', 'children'),
    Output('sum-sales', 'children'),
    Output('best-model', 'children'),
    Output('best-make', 'children'),
    Input('year-dropdown', 'value'),
    Input('all-years-button', 'n_clicks')
)
def set_cards_to_year(year_selected, n_clicks):
    triggered_id = ctx.triggered_id

    if triggered_id == 'year-dropdown' and year_selected:
        return generate_card_values(year_selected)
    return generate_card_values()


def generate_card_values(year_selected=None):
    if year_selected:
        cars_selected = cars_df[cars_df.year == year_selected]
    else:
        cars_selected = cars_df

    sales_of_year = cars_selected.shape[0]
    sum_of_year = cars_selected['price'].sum()
    model_of_year = cars_selected['model'].value_counts().idxmax()
    make_of_year = cars_selected['make'].value_counts().idxmax()

    sales_of_year = f"{sales_of_year:,}"
    sum_of_year = f"{sum_of_year / 1e6:,.2f} Mio. €"

    return sales_of_year, sum_of_year, model_of_year, make_of_year


# Callback to clear the dropdown when the button is clicked
@callback(
    Output('year-dropdown', 'value'),
    Input('all-years-button', 'n_clicks')
)
def clear_dropdown(n_clicks):
    if n_clicks is not None:
        return None
    return dash.no_update


# Callback to update the title of the page
@callback(
    Output('title-of-page', 'children'),
    Input('year-dropdown', 'value'),
    Input('all-years-button', 'n_clicks')
)
def update_title(year_selected, n_clicks):
    if year_selected is not None:
        return f'Statistics of {year_selected}'
    else:
        return f'Statistics of {all_years[0]}-{all_years[-1]}'

# callback and a card that were used for testing:
# @callback(
#     Output('test-card', 'children'),
#     Input('year-dropdown', 'value'),
#     Input('all-years-button', 'n_clicks'),
#     State('year-dropdown', 'value')
# )
# def test_callback(year_selected, n_clicks, dropdown_value):
#     triggered_id = ctx.triggered_id
#
#     if triggered_id == 'year-dropdown':
#         if year_selected is not None:
#             cars_selected = cars_df.query(f'year == {year_selected}')
#             selected_size = cars_selected.size
#             return selected_size
#         else:
#             return cars_df.size
#
#     elif triggered_id == 'all-years-button':
#         return cars_df.size
#
#     return cars_df.size
