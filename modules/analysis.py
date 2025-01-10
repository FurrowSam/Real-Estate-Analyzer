def calculate_avg_price_per_sqft(df):
    return df.groupby('Location')['Price per Sq Ft'].mean()

def get_summary_statistics(df):
    return df.describe()
