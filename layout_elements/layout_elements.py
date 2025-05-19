import plotly.express as px
import dash
from .stylings import common_graph_layout
from dash import callback, Output, Input, State, dcc, ctx, html
import dash_bootstrap_components as dbc
from .data_basis import all_years, cars_df

# II. Layout Components
# A: Control Elements
# ---------------------
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


# b) General graphs
# Todo: Part of interactivity such as zooming in should be deactivated
# Line plot for sold cars:
year_counts = cars_df.groupby('year').size()
counts_over_time = px.line(
    year_counts,
    year_counts.index,
    year_counts,
    markers='o',
    title='Cars Sold Over Time',
    template='plotly_dark',
)
counts_over_time.update_traces(line_color='#00bc8c')
counts_over_time.update_layout(**common_graph_layout)

# Bar Plot with Sums of Sales:
year_sums = cars_df.groupby('year').price.sum()
sums_over_time = px.bar(
    year_sums,
    year_sums.index,
    year_sums,
    title='Total Sales per Year',
    template='plotly_dark'
)
sums_over_time.update_traces(marker_color='#00bc8c')
sums_over_time.update_layout(**common_graph_layout)
sums_over_time.update_xaxes(tickmode='linear',
                            nticks=year_sums.size,
                            tickangle=-45)



# III. Callbacks


@callback(
    Output('offer-pie', 'figure'),
    Output('fuel-bars', 'figure'),
    Output('mileages-pie', 'figure'),
    Input('year-dropdown', 'value'),
    Input('all-years-button', 'n_clicks')
)
def set_graphs_to_year(year_selected, n_clicks):
    triggered_id = ctx.triggered_id

    if triggered_id == 'year-dropdown' and year_selected is not None:
        cars_selected = cars_df[cars_df.year == year_selected]
        title_suffix = f'in {year_selected}'
    else:
        cars_selected = cars_df
        title_suffix = 'for All Years'

    # Pie with ratios of offer Types:
    # Task: Control the order of the slices and thereby the legend order
    offer_types_order = cars_df.groupby('offerType').price.mean()\
                                                    .sort_values().index
    cmap_offertypes = {
        'Used': '#00bc8c',
        'Demonstration': '#008c69',
        "Employee's car": '#4ee0b3',
        'Pre-registered': '#005940',
        'New': '#80f2d1'
    }

    offertypes_pie = px.pie(
        cars_selected,
        names='offerType',
        color='offerType',
        color_discrete_map=cmap_offertypes,
        title=f'Offer Types {title_suffix}',
        template='plotly_dark',
    )
    offertypes_pie.update_layout(**common_graph_layout)

    cmap_fueltypes = {
        'Electric/Gasoline': '#00bc8c',
        'Diesel': '#008c69',
        'Gasoline': '#005940',
        'Electric': '#80f2d1'

    }
    fuel_counts = cars_selected.fuel.value_counts().iloc[:4]
    fuel_count = px.bar(
        fuel_counts,
        x=fuel_counts.index,
        y=fuel_counts,
        title=f'Top Fuel Types {title_suffix}',
        color_discrete_map=cmap_fueltypes,
        template='plotly_dark',
    )
    fuel_count.update_layout(**common_graph_layout)
    fuel_count.update_traces(marker_color='#00bc8c')

    # Barchart (!) with mileage ratios:
    # Task: write func for generating those cmaps!
    cmap_mileages = {
        'over 200k': '#80f2d1',
        "under 200k": '#4ee0b3',
        'under 150k': '#00bc8c',
        'under 100k': '#008c69',
        'under 50k': '#005940',
    }
    mileage_cat_counts = cars_selected.mileage_bins.value_counts()
    mileages_order = ['under 50k', 'under 100k', 'under 150k',
                      'under 200k', 'over 200k']
    color_nuances = ['#005940', '#008c69', '#00bc8c', '#4ee0b3', '#80f2d1']
    colormap = dict(zip(mileages_order, color_nuances))
    mileages_bars = px.bar(
        mileage_cat_counts,
        mileage_cat_counts,
        mileage_cat_counts.index,
        color_discrete_map=colormap,
        color=mileage_cat_counts.index,
        template='plotly_dark'
    )
    mileages_bars.update_layout(**common_graph_layout)
    mileages_bars.update_layout(
        yaxis=dict(
            categoryorder='array',
            categoryarray=mileages_order
        ),
        showlegend=False
    )


    return offertypes_pie, fuel_count, mileages_bars


@callback(
    Output('line_or_box', 'figure'),
    Input('year-dropdown', 'value'),
    Input('all-years-button', 'n_clicks')
)
def generate_line_or_box(year_selected, n_clicks):
    triggered_id = ctx.triggered_id

    if triggered_id == 'year-dropdown' and year_selected is not None:
        cars_selected = cars_df[cars_df.year == year_selected]
        # Extreme outliers disturb readability of the box > removal:
        price_statistics = cars_selected.price.describe()
        iqr = price_statistics['75%'] - price_statistics['25%']
        upper_whisker = price_statistics['75%'] + 1.5 * iqr
        outliers_removed = cars_selected.query(f'price <= @upper_whisker')

        price_box = px.box(
            outliers_removed,
            x=outliers_removed.price,
            title=f'Price in {year_selected}',
            template='plotly_dark',
            points=False
        )
        price_box.update_traces(fillcolor='#00bc8c',
                                line_color='#009973')
        price_box.update_layout(**common_graph_layout)

        return price_box
    else:
        year_counts = cars_df.groupby('year').size()
        counts_timeline = px.line(
            year_counts,
            year_counts.index,
            year_counts,
            markers='o',
            title='Cars Sold Over Time',
            template='plotly_dark',

        )
        counts_timeline.update_traces(line_color='#00bc8c')
        counts_timeline.update_layout(**common_graph_layout)
        counts_timeline.update_xaxes(tickmode='linear',
                                     nticks=year_sums.size,
                                     tickangle=-45)

        return counts_timeline


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
