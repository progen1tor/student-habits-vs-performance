import pandas as pd 

def load_df(path: str = '../data/raw.csv') -> pd.DataFrame:
    df = pd.read_csv(path)
    return df 