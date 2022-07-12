import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_data_summary(df):
    '''
    This function takes in a dataframe and prints out the shape of the df, number of missing values, 
    columns and their data types, summary statistics of the df, as well as the value counts for categorical variables.
    '''
    # Print out the "shape" of our dataframe - the rows and columns we have to work with
    print(f'The dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('')
    print('-------------------')

    # print the number of missing values in our dataframe
    print(f'There are total of {df.isna().sum().sum()} missing values in the entire dataframe.')
    print('')
    print('-------------------')

    # print some information regarding our dataframe
    print(df.info())
    print('')
    print('-------------------')
    
    # print out summary stats for our dataset
    print('Here are the summary statistics of our dataset')
    print(df.describe())
    print('-------------------')

    print('Here are the categories and their relative proportions')
    # check different categories and proportions of each category for categorical variables
    cat_vars = ['DAC_indicator','grid_outages_county', 'state_code']
    for col in df.columns:
        if col in cat_vars:
            print(df[col].value_counts())
            print('')
            print(f'proportions of {col}')
            print('')
            print(df[col].value_counts(normalize=True,dropna=False))
            print('-------------------')
