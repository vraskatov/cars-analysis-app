import pandas as pd

cars_df = pd.read_csv('data/autoscout24_edited.csv')
cars_records = cars_df.to_dict('records')
all_years = [year for year
             in range(cars_df.year.min(), cars_df.year.max() + 1)]

