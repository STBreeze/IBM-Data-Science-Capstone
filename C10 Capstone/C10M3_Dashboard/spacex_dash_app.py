# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Convert min and max payload to integers
min_payload = int(spacex_df['Payload Mass (kg)'].min())
max_payload = int(spacex_df['Payload Mass (kg)'].max())

# Create a dash application
app = dash.Dash(__name__)

# Create options for the dropdown
Lsites = spacex_df['Launch Site'].unique()
optionsLsite = [{'label': site, 'value': site} for site in Lsites]
optionsLsite.insert(0, {'label': 'All', 'value': 'All'})

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
             style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # Dropdown for site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=optionsLsite,
        value='All',  # Default value
        placeholder='Select a Launch Site',
        searchable=True
    ),
    html.Br(),

    # Pie chart for success counts
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    
    # Slider for payload range
    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        value=[min_payload, max_payload],
        marks={i: str(i) for i in range(min_payload, max_payload + 1, 1000)}
    ),
    html.Br(),

    # Scatter chart for payload vs success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# Callback for updating the pie chart based on site selection
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def pie_chart(selected_site):
    filtered_df = spacex_df
    if selected_site != 'All':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]

    success_counts = filtered_df['class'].value_counts()
    fig = px.pie(success_counts, values=success_counts.values, 
                 names=success_counts.index, 
                 title='Total Success Launches for {}'.format(selected_site),
                 color=success_counts.index,
                 color_discrete_map={0:'coral', 1:'teal'})
    return fig

# Callback for updating the scatter chart based on site selection and payload slider
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def scatter_chart(selected_site, payload_range):
    filtered_df = spacex_df
    if selected_site != 'All':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
    
    # Filter by payload range
    filtered_df = filtered_df[(filtered_df['Payload Mass (kg)'] >= payload_range[0]) & 
                              (filtered_df['Payload Mass (kg)'] <= payload_range[1])]
    
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                     title='Payload vs Success for {}'.format(selected_site),
                     labels={'class': 'Success (1) / Failure (0)', 'Payload Mass (kg)': 'Payload Mass (kg)'},
                     color='Booster Version Category'
                     )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
