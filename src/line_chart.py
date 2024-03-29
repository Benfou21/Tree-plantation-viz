'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME
import plotly.graph_objects as go

def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    
    
    fig = go.Figure()

    
    fig.update_layout(
        annotations=[
            dict(
                text="No data to display. Select a cell in the heatmap for more information.",
                showarrow=False,
                font=dict(size=16)
            )
        ],
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        dragmode=False  
    )
    
    
    
    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    fig.add_shape(type="rect",
        x0=0, y0=0.25, x1=1, y1=0.75,
        xref="paper", yref="paper",
        fillcolor=THEME["pale_color"],
        line_color=THEME["pale_color"],
    )
    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template
    
    
    fig = go.Figure(data=go.Scatter(x=line_data.Date_Plantation, y=line_data.Count, line= dict(color=THEME["line_chart_color"], width =2)))
    
    fig.update_layout(title=f'Trees planted in {arrond} in {year}',
        title_font=dict(size= 24),
        yaxis=dict(
            title='Trees',
            title_font=dict(size=18),
            tickfont=dict(size=THEME["label_font_size"])
        ),
        xaxis=dict
        (
            tickfont=dict(size=THEME["label_font_size"]),
            tickformat="%d %b"
        ),
        hoverlabel=dict(font=dict(family="Roboto", size=16, color="black"))
    )
    
    fig.update_traces(hovertemplate=hover_template.get_linechart_hover_template())
    
    return fig
