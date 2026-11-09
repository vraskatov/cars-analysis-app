# cars-analysis-app

A responsive dashboard written in Python, built with [Dash](https://dash.plotly.com/), [Plotly](https://plotly.com/python/) and
[Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/).
It visualizes ~46,000 car listings from AutoScout24 Germany (2011–2021) based on the
[Germany Cars Dataset](https://www.kaggle.com/datasets/ander289386/cars-germany) from Kaggle.

## Features
- Shows key figures for the selected time span on cards:
  - number of cars sold
  - total sales in Mio. €
  - bestseller model
  - bestseller make
- Plots the distribution of the data with:
  - a pie chart of offer types (Used, New, Demonstration, ...)
  - a bar chart of the top fuel types
  - a bar chart of mileage categories
  - a line plot of cars sold over time (all years) or a box plot of prices (single year)
- Lets the user switch between all years and a single year via a dropdown and an "All Years" button.
- Uses a dark theme (Bootstrap "Darkly") and a responsive layout that adapts to smaller screens.

## Project Structure
```
cars-analysis-app/
├── app.py                  # entry point, builds the layout and starts the server
├── assets/style.css        # custom styling
├── components/
│   ├── layout_*.py         # layout elements (controls, cards, plots, stylings)
│   └── callbacks/          # callbacks for cards, controls, plots and titles
├── data/
│   ├── autoscout24-germany-dataset.csv   # original dataset from Kaggle
│   ├── autoscout24_edited.csv            # cleaned dataset used by the app
│   └── data_basis.py                     # loads the data
└── analyses/               # Jupyter notebooks for data preparation and exploration
```

## How To Run the App
- install git
- select a folder and clone the repository into it with:\
```git clone https://github.com/vraskatov/cars-analysis-app.git```
- create a virtual environment in the cloned folder and activate it
- pip install the requirements into the environment using:\
```pip install -r requirements.txt```
- then navigate in the terminal into the cloned folder (where the file app.py is) and run:\
```python app.py```\
This starts the app. The app has to be started from this folder, since the data is loaded via a relative path.
- open ```http://127.0.0.1:8050/``` in a tab of your browser.

## Data Preparation & Exploration
The folder `analyses/` contains the Jupyter notebooks that document how the data
was prepared and how the visualizations of the app were developed:
- [editing_csv.ipynb](analyses/editing_csv.ipynb): inspects the distribution of
  mileages, groups them into the categories used in the app (`under 50k` to
  `over 200k`), compares them across the years and exports the cleaned dataset
  `autoscout24_edited.csv`.
- [autoscout24_exploration.ipynb](analyses/autoscout24_exploration.ipynb)
  ([view with interactive plots](https://nbviewer.org/github/vraskatov/cars-analysis-app/blob/main/analyses/autoscout24_exploration.ipynb)):
  computes the global statistics shown on the cards, develops the color mappings
  and ordering of the charts and removes price outliers (1.5 × IQR) for the box plot.

The notebooks are not needed to run the app. To open them, additionally install:\
```pip install jupyterlab matplotlib```\
and start Jupyter with ```jupyter lab```.

## Todos
- Turn the app into a multipage app:
  - global view: visualized statistics of all years with the additional possibility of filtering by year
  - model page: select a given model via dropdown (e.g. Golf) and see statistics specific to that model
- Use the same colors for the same categories across all plots
- Control the order of the slices (and thereby the legend) in the offer types pie chart
- Make the cards look uniform in the mobile view
- Deactivate parts of the plot interactivity such as zooming
- Add the bar chart with total sales per year to the dashboard

## License
This project is licensed under the MIT License, see [LICENSE](LICENSE).
