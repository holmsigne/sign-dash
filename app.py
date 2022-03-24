import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import calendar

import plotly.express as px
import plotly.graph_objects as go

import datamodel
order = datamodel.get_data()
#df_year = datamodel.get_year()
#df_month = datamodel.get_month()

fig_employee = px.bar(order, 
    x='employee', 
    y='total', 
    color='type', 
    color_discrete_sequence=['rgb(139,224,164)', 'rgb(230,245,201)'],
    text='total', 
    title='Sales by Employee',
    hover_data=[], 
    labels={'total':'Total sales', 'employee':'Employee', 'type':'Product Type'})
fig_employee.update_traces(texttemplate='%{text:0.3s}', textposition='outside')
fig_employee.update_layout(uniformtext_minsize=5, uniformtext_mode='hide', xaxis_tickangle=80)

fig_product = px.bar(order, 
    x='productname', 
    y='total', 
    color='type', 
    color_discrete_sequence=['rgb(139,224,164)', 'rgb(230,245,201)'],
    text='total', 
    title='Sales by Product',
    hover_data=[],
    labels={'total':'Total sales', 'productname':'Product', 'type':'Product Type'})
fig_product.update_traces(texttemplate='%{text:0.2s}', textposition='outside')
fig_product.update_layout(uniformtext_minsize=5, uniformtext_mode='hide', xaxis_tickangle=80)

dash_app = dash.Dash(__name__)
app = dash_app.server

# Layout
dash_app.layout = html.Div(
    children=[
        html.Div(className='row',
                children=[html.Div(className='eight columns div-for-charts bg-grey',
                            children=[
                                dcc.Graph(id="sales_employee", figure=fig_employee),
                                dcc.Graph(id="sales_product", figure=fig_product)
                            ]
                    ),
                ]
            )
        ]
)

# Runs app
if __name__ == '__main__':
    dash_app.run_server(debug=True)
