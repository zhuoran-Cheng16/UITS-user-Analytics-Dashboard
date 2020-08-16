import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd


df = pd.read_csv('sampleapp_UITS_TEAM21/app/login-table/output.csv')

app = dash.Dash(__name__)

PAGE_SIZE = 20

#a='Object not found in AD. Please check the serial Field and make sure it"s a valid AD object.'

app.layout = dash_table.DataTable(
    id='table-paging-and-sorting',
    columns=(

        [{'name': i, 'id': i, 'deletable': True} for i in (df.columns)]
    ),

    style_header={
           'backgroundColor': 'rgb(230, 230, 230)',
           'fontWeight': 'bold'
       },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        },
        {
            'if': {
                'column_id': 'Success',
                'filter_query': '{Success} eq "Error"'
            },
            'backgroundColor': 'red',
            'color': 'white',
        },
    ],
   
  
  
    page_current=0,
    page_size=PAGE_SIZE,
    page_action='custom',

    sort_action='custom',
    sort_mode='single',
    sort_by=[]

)


@app.callback(
    Output('table-paging-and-sorting', 'data'),
    [Input('table-paging-and-sorting', "page_current"),
     Input('table-paging-and-sorting', "page_size"),
     Input('table-paging-and-sorting', 'sort_by')])
def update_table(page_current, page_size, sort_by):
    if len(sort_by):
        dff = df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df
  

    return dff.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
