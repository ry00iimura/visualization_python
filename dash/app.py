import dash
import dash_core_components as dcc
import dash_html_components as html

# create an app instance
app = dash.Dash(__name__)

# create graph
app.layout = html.Div(
    children = [
        html.H1('Hello Dash',),
        dcc.Graph(
            id = 'first-graph',
            figure = {
                'data':[
                    {'x':[1,2,3,4],
                     'y':[3,2,4,6],
                     'type':'bar',
                     'name':'Tokyo',
                    },
                    {'x':[1,2,3,4],
                     'y':[2,4,3,2],
                     'type':'bar',
                     'name':'Osaka'}
                    ],
                'layout':{
                    'title':'graph-1 Tokyo vs Osaka'
                }
            }
        )
    ]
)

# execute
if __name =='__main__':
    app.run_server(debug=True)
