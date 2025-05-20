import dash_bootstrap_components as dbc
from dash import callback, Output, Input, ctx

from data.data_basis import cars_df


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
