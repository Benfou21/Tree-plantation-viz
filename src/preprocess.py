

'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'])
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    
    # Converting to datetime
    start = pd.to_datetime(f'{start}-01-01')
    end = pd.to_datetime(f'{end}-12-31')
    
    # Filter
    dataframe = dataframe[(dataframe['Date_Plantation'] >= start) & (dataframe['Date_Plantation'] <= end)]
    
    return dataframe.sort_values(by='Date_Plantation')
    


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    
    
    dataframe['Year'] = dataframe['Date_Plantation'].dt.year
    
    resume = dataframe.groupby(['Arrond_Nom','Year']).count()
    resume = resume.rename(columns={'Arrond': 'Count'})
    
    resume = resume.drop(columns=['Latitude', 'Longitude'])
    
    resume = resume.reset_index()

    return resume


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    
    restructure_df = yearly_df.pivot(index='Arrond_Nom', columns='Year', values='Count')
    
    # Replace empty with 0
    restructure_df = restructure_df.fillna(0)
    return restructure_df


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
    
    # Get the start of the year & end of the year in date format
    start_year = pd.to_datetime(f'{year}-01-01')
    end_year = pd.to_datetime(f'{year}-12-31')
    
    # Filter the data with start and end of the year + Arron
    daily_info = dataframe[(dataframe['Date_Plantation'] >= start_year) & 
                    (dataframe['Date_Plantation'] <= end_year) & 
                    (dataframe['Arrond_Nom'] == arrond)
                    ]
    
    
    daily_info = daily_info.groupby(pd.Grouper(key='Date_Plantation')).count()
    daily_info = daily_info.rename(columns={'Arrond': 'Count'})
    
    # Remove useless cols
    daily_info = daily_info.drop(columns=['Latitude', 'Longitude', 'Year', 'Arrond_Nom'])
    
    # Reset Index
    daily_info = daily_info.reset_index()
    
    # Sort by date
    daily_info = daily_info.sort_values(by='Date_Plantation')
    

    start_date = daily_info['Date_Plantation'].min()
    end_date = daily_info['Date_Plantation'].max()
    
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    complete_df = pd.DataFrame({'Date_Plantation': date_range})
    
    
    daily_info = pd.merge(complete_df, daily_info, on='Date_Plantation', how='left')
    daily_info = daily_info.fillna(0)
    
    return daily_info
