'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hover_template = "<b>Neighborhood:</b> %{y}<br>" + \
                     "<b>Year:</b> %{x}<br>" + \
                     "<b>Trees planted:</b> %{z}<extra></extra>"
    return hover_template

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hover_template = "<b>Date:</b> %{x}<br>" + \
                     "<b>Trees:</b> %{y}<extra></extra>"
    return hover_template

