'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template
import plotly.graph_objects as go
import plotly.io as pio
from template import THEME

def get_figure(data):
    '''
        Generates the heatmap from the given dataset.
        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    
    fig = px.imshow(data)

    # Set title of color bar to 'Trees'
    fig.update_layout(coloraxis_colorbar=dict(title='Trees')) 

    # Set dragmode to False in the layout
    fig.update_layout(
        dragmode=False,
        xaxis=dict
        (
            title='Year',
            tickmode='linear',
            title_font=dict(size=18),
            tickfont=dict(size=THEME["label_font_size"]),
        ),
        yaxis=dict
        (
            title='Neighborhood',
            title_font=dict(size=18),
            tickfont=dict(size=THEME["label_font_size"]),
        ),
        
        hoverlabel=dict(font=dict(family="Roboto", size=16, color="black"))
    )
    

    fig.update_traces(hovertemplate=hover_template.get_heatmap_hover_template())

    # Include the hover template
   

    return fig

