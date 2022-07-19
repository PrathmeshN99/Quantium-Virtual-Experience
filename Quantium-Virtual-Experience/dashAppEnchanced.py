import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)

app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("data/merged.csv")

print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Sales of Pink Morsels by region and date", style={'text-align': 'center'}),

    dcc.RadioItems(['north','south','east','west','all'], 'all',id="selectRegion"),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='selectRegion', component_property='value')]
)
def update_graph(selectRegion):
    print(selectRegion)
    print(type(selectRegion))

    container = "Sales in {} region:".format(selectRegion)

    dff = df.copy()
    if selectRegion=='all':
        pass
    else:
        dff = dff[dff["region"] == selectRegion]

    # Plotly Express
    fig = px.line(dff, x="date", y="sales", title='Sales in US Dollars($)')

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)