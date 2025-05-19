import plotly.express as px
from .data_basis import cars_df
from stylings import common_graph_layout

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
