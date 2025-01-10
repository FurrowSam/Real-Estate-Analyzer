import folium
from folium.plugins import HeatMap

def create_map(df):
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)
    for _, row in df.iterrows():
        popup = f"Price: ${row['Price']:,}<br>Location: {row['Location']}"
        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=popup).add_to(m)
    return m

def save_map(map_object, filepath):
    map_object.save(filepath)
