import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)


app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("data/merged.csv")

print(df[:5])
fig = px.line(df, x="date", y="sales", title='Sales in US Dollars($)')
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Sales of Pink Morsels by date", style={'text-align': 'center'}),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure=fig)
])


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)