import pandas as pd
import os


def get_poi_data(county):
    # define vars like condition
    # 
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)

    condition = df['location_id'] == county

    filtered_df = df[condition]
    print(filtered_df['neighborhood_index'])

def sushi_chart():
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)
    locations = df['location_id']
    sushi = df['sushi_index']
    print(locations, sushi)
    # return locations, sushi

sushi_chart()
# get_poi_data('ADAMS')