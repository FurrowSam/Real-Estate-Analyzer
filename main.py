import pandas as pd
from modules.scraper import scrape_real_estate_data
from modules.data_cleaning import clean_data
from modules.analysis import calculate_avg_price_per_sqft
from modules.visualization import create_map, save_map

# Step 1: Scrape data
base_url = "https://www.zillow.com/homes/for_sale/Pittsburgh,-PA_rb/"
property_data = scrape_real_estate_data(base_url, pages=5)

# Step 2: Save raw data
raw_data_path = 'data/raw_data.csv'
pd.DataFrame(property_data).to_csv(raw_data_path, index=False)

# Step 3: Clean data
cleaned_data = clean_data(raw_data_path)
cleaned_data_path = 'data/cleaned_data.csv'
cleaned_data.to_csv(cleaned_data_path, index=False)

# Step 4: Analyze data
avg_price_per_sqft = calculate_avg_price_per_sqft(cleaned_data)
print(avg_price_per_sqft)

# Step 5: Visualize data
map_object = create_map(cleaned_data)
save_map(map_object, 'data/real_estate_map.html')
