from dash import Dash, dcc, html, Input, Output
import pandas as pd
import helpers.graphs as hg
import plotly.express as px
import os

app = Dash(__name__)
app.title = "Dashboard JO"

app.layout = html.Div(className= 'main', children=[
    html.H1("Dessine moi les JO 🏃"),    
    html.Div(className = 'details', children=[
        html.Div(id='flag-container'),
        dcc.Dropdown(options =[{'label': 'France', 'value': 'FRA'},
       
       {'label': 'Royaume-Uni', 'value': 'GBR'}],value = 'FRA', id='demo-dropdown'),
        html.P(id = 'title-container')
    ]),
    html.Div(id='dd-output-container'),
    html.Div(id='top10-output-container'),    
    html.Footer(" © Tous droits réservés - Cosmodev")
    ]
)

@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(country):
    df = hg.display1(country=country)
    
    fig = px.bar(df, x=df["game_year"], y=df["medals"], width=1000, height=500, title="Total des médailles par éditions des jeux olympiques",
                 labels={
                     "medals": "Médailles remportés",
                     "game_year": "Année",
                 },)

    fig.update_layout(
        plot_bgcolor='#eff',
        paper_bgcolor='#fff',
        font_color='#111'
    )
    return dcc.Graph(
        figure= fig
    )

    
@app.callback(
    Output('title-container', 'children'),
    Input('demo-dropdown', 'value')
)
def change_title(country):
    return country    
    
@app.callback(
    Output('flag-container', 'children'),
    Input('demo-dropdown', 'value')
)
def change_flag(country):
    return html.Img(src='assets/flag_{}.png'.format(country)),

@app.callback(
    Output('top10-output-container','children'),
    Input('demo-dropdown','value')
)
def update_output(country):
    df = hg.display2(country=country)    
    fig = px.bar(df, x=df.athlete_full_name, y=df.total_metals, color = df.total_metals, title="Les 10 meilleurs athètes et leurs médailles obtenus", labels={
                     "total_metals": "Médailles remportés",
                     "athlete_full_name": "Athlètes" })
    return dcc.Graph(
        figure= fig
    )
    
    

if __name__ == '__main__':
    app.run_server(debug=True)