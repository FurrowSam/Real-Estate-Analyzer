import pandas as pd

def clean_data(data_path):
    df = pd.read_csv(data_path)
    df['Price'] = df['Price'].str.replace('[\$,]', '', regex=True).astype(float)
    df['Area'] = df['Area'].str.replace('sq ft', '').str.replace(',', '').astype(float)
    df = df.dropna()
    df['Price per Sq Ft'] = df['Price'] / df['Area']
    return df
