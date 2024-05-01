import pandas as pd
import os
import plotly.express as px


def graph_data():
    with open('data/demographics') as f:
        df = pd.read_csv(f)
    cpi_df = df[['LOCATION_ID','CONSUMER_PRICE_INDEX']]
    print(cpi_df)
    return cpi_df

graph_data()
# Iterate over columns
# for column in df.columns:
#     # Iterate over values in the column
#     for value in df[column]:
#         # Concatenate column name with value
#         print(f"{column.replace('_', ' ').capitalize()}: {value}")

# def get_poi_data(county):
#     # define vars like condition
#     # 
#     with open('data/poi_index_comp', mode='r') as f:
#         df = pd.read_csv(f)

#     condition = df['location_id'] == county

#     filtered_df = df[condition]
#     print(filtered_df['neighborhood_index'])

# def sushi_chart():
#     with open('data/poi_index_comp', mode='r') as f:
#         df = pd.read_csv(f)
#     locations = df['location_id']
#     sushi = df['sushi_index']
#     print(locations, sushi)
#     # return locations, sushi

# sushi_chart()
# get_poi_data('ADAMS')