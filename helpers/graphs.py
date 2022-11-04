import pandas as pd
from dash import dcc
import os
import plotly.express as px

def display1(country):
    df_hosts = pd.read_csv(r"{}/archive/olympic_hosts.csv".format(os.getcwd()))
    df_results = pd.read_csv(r"{}/archive/olympic_results.csv".format(os.getcwd())) 

    #fusionner df_medals & df_hosts pour filter les JO d'étés 
    df = df_results.merge(df_hosts, left_on='slug_game', right_on='game_slug')
    #filtrer : on garde les athlètes de GB médaillés au jeux d'étés
    df.query("country_3_letter_code == @country and game_season == 'Summer'", inplace=True)
    df.dropna(subset=['medal_type'], inplace = True)

    #création du nouveau dataframe qui donne le total de médaillés chaque année
    df = df.groupby(by="game_year").size().reset_index(name='medals')

    return df