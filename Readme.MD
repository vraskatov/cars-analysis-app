## Cars Analysis App

This is an Analysis App written in Python, built with Dash and based on a 
cars dataset obtained from Kaggle.

To start the app run app.py.

### What has been done so far:

To achieve a responsive behavior dash_bootstrap_components has been used.
The main goal of the app at this stage is to give the user a dashboard for the
data with the options of looking globally or by year at the data, visualizing 
different aspects of the given year with cards and plots.

### The road ahead:

Multipage Approach:
At this point of time only two pages are planned:
* global view: the visualized statistics of all years
with the additional possibility of filtering by year
* model page: a page where the user can select a given model via dropdown 
(e.g. Golf) and sees statistics specific to that model
