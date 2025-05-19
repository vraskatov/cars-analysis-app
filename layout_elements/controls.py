from dash import dcc, html
from .data_basis import all_years

year_dropdown = dcc.Dropdown(
    all_years,
    None,
    id='year-dropdown',
    placeholder="Select a Specific Year",
    clearable=True,
    className='dropdown-dark mb-4',
)

all_years_button = html.Button(
    'All Years',
    id='all-years-button',
    n_clicks=0,
    className='mb-4'
)
