from dash import callback, Output, Input

from data.data_basis import all_years


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
