"""
A collection of helper functions used in the project.
"""

import numpy as np

def create_time_index(df):
    """
    Converts Date column to a simple integer index (t = 1,2,3,...)
    Assumes data is sorted chronologically.
    """
    df = df.reset_index(drop=True)
    df['t'] = df.index + 1
    return df

def bass_cumulative(t, p, q, M):
    """
    Continuous Bass Model (cumulative form):
    S(t) = M * [1 - exp(-(p+q)*t)] / [1 + (q/p)*exp(-(p+q)*t)]
    """
    return M * (1 - np.exp(-(p+q)*t)) / (1 + (q/p)*np.exp(-(p+q)*t))
