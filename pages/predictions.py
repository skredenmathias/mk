# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

# Imports from this application
from app import app

# Load model
# pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Test predictions

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])
