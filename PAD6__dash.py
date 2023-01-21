from dash import Dash,  dash_table, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

fname='winequality.csv'

app=Dash(__name__)

df = pd.read_csv(fname, index_col=0)
head=df.head(10)
cols=df.columns.tolist()

app.layout=html.Div(children=[
    html.H1(children=fname),
    html.Div(children='yet another dash demo app: analyser for '+fname),
    dash_table.DataTable(head.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
    html.Div(children='Choose your model:'),
    dcc.RadioItems(['Linear regression', 'Logistic regression', 'Classification knn'], '', id='model_radio'),
    html.Div(children='Choose column to show:'),
    dcc.Dropdown(cols, '', id='cols_to_show'),
    html.Div(id='plot')
])

@app.callback(
    Output(component_id='plot', component_property='children'),
    Input(component_id='model_radio', component_property='value'),
    Input(component_id='cols_to_show', component_property='value')
)
def update_figure(model_name,y=''):
    if ((model_name == '') or (y == '')):
        return None
    if 'regression' in model_name:
        return dcc.Graph(figure=px.scatter(df, x='pH', y=y))
    elif 'Classification' in model_name:
        return dcc.Graph(figure=px.box(df, x='target', y=y))
    else:
        return None


if __name__ == '__main__':
    app.run_server(debug=True)