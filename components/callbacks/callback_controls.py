from dash import callback, Output, Input, dash


# Callback to clear the dropdown when the button is clicked
@callback(
    Output('year-dropdown', 'value'),
    Input('all-years-button', 'n_clicks')
)
def clear_dropdown(n_clicks):
    if n_clicks is not None:
        return None
    return dash.no_update
