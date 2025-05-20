import dash
from dash import callback, Output, Input, ctx
import dash_bootstrap_components as dbc

from data.data_basis import all_years, cars_df




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
