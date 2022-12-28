import pandas as pd
from dash import Dash, dash_table, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("C:\\Users\\SebastianPC\\Desktop\\winequelity.csv")

app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children="DASH HW"),
    html.Div(children='''
        Wczyta dane z pliku winequality.csv do tabeli pandas i je wyświetli jako tabelę (10 wierszy). 
    '''),

    html.Table(dash_table.DataTable(df.head(10).to_dict('records'), [{"name": i, "id": i} for i in df.columns])),

    html.Div([
        dcc.RadioItems(
            id='radio',
            options=[
                {'label': 'MODEL REGRESJI', 'value': 'regression'},
                {'label': 'MODEL KLASYFIKACJI', 'value': 'classification'},
            ],
            value='regression'
        )
    ]),
    html.Div([
        dcc.Dropdown(
            id='userDropdown',
            value='fixed acidity',
            options=df.columns[1:]
        )
    ]),
    html.Div(id='wykres')
])


@app.callback(
    Output(component_id='wykres', component_property='children'),
    Input(component_id='radio', component_property='value'),
    Input(component_id='userDropdown', component_property='value')
)
def update_output_div(setGraph, userSelect):
    if setGraph == 'regression':
        return dcc.Graph(
            figure=px.bar(df, y='pH', x=userSelect, color='target')
        )
    elif setGraph == 'classification':
        return dcc.Graph(
            figure=px.density_heatmap(df, y='target', x=userSelect)
        )
    else:
        return "Nie rozpoznano komendy"


if __name__ == '__main__':
    app.run_server(debug=True)
