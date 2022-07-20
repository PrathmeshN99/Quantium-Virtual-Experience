import unittest
import dashAppEnchanced
import plotly.express as px  # (version 4.7.0 or higher)
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)

class TestApp(unittest.TestCase):

    def test_dashAppEnhanced(dashAppEnhanced):
        app = Dash(__name__)
        app.layout = html.Div("Sales of Pink Morsels by region and date", style={'text-align': 'center'},id="h1_text")
    
        dashAppEnchanced.start_server(app)

        dashAppEnchanced.wait_for_contains_text("#h1_test", "Sales of Pink Morsels by region and date", timeout=None)
        dashAppEnhanced.wait_for_element_by_id("selectRegion", timeout=None)
        dashAppEnhanced.wait_for_element_by_id("my_bee_map", timeout=None)
