import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

gdp_data = pd.read_csv('GDP_data.csv', sep=';')
gdp_data = gdp_data.rename(columns = {'Unnamed: 0': 'Time'})
gdp_data = gdp_data.drop('Unnamed: 5', axis=1)
gdp_data = gdp_data.drop('Unnamed: 6', axis=1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(
        children='GDP Graph',
        style = {
            'textAlign': 'center',
            'color': 'black',
        }),

    html.Div(
        children='''
        You can easily visualise data by using DASH framework. 
        Here, you can understand the flow of GDP change in graph.
        ''',
        style = {
            'textAlign': 'center',
            'color': 'black',
        }),
    dcc.Graph(
       id='gdp_graph',
       figure = {
           'data': [
               go.Scatter(
                   x=gdp_data['Time'],
                   y=gdp_data['Japan'],
                   mode='lines',
                   opacity=0.7,
                   marker={
                       'size':15,
                       'color':'red'
                   },
                   name='Japan'
               ),
               go.Scatter(
                   x=gdp_data['Time'],
                   y=gdp_data['USA'],
                   mode='lines',
                   opacity=0.7,
                   marker={
                       'size':15,
                       'color':'blue'
                   },
                   name='USA'
               ),
               go.Scatter(
                   x=gdp_data['Time'],
                   y=gdp_data['China'],
                   mode='lines',
                   opacity=0.7,
                   marker={
                       'size':15,
                       'color':'yellow'
                   },
                   name='China'
               ),
               go.Scatter(
                   x=gdp_data['Time'],
                   y=gdp_data['Netherlands'],
                   mode='lines',
                   opacity=0.7,
                   marker={
                       'size':15,
                       'color':'black'
                   },
                   name='Netherlands'
               )
           ],
           'layout': go.Layout(
               xaxis = {'title': 'Time'},
               yaxis = {'title': 'GDP'},
               width = 1000,
               height = 500
           )
       }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)