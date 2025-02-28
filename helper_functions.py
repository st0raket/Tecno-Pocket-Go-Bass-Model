import numpy as np

def create_time_index(df):
    df = df.reset_index(drop=True)
    df['t'] = df.index + 1
    return df

def bass_cumulative(t, p, q, M):
    return M * (1 - np.exp(-(p+q)*t)) / (1 + (q/p)*np.exp(-(p+q)*t))
