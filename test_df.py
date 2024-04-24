import pandas as pd
import os


def get_poi_data(county):
    # define vars like condition
    # 
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)

    condition = df['location_id'] == county

    filtered_df = df[condition]
    print(filtered_df)

get_poi_data('ADAMS')