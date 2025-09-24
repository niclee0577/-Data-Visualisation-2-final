import pandas as pd
from geopy.geocoders import Nominatim

cancer_df = pd.read_csv('cancer_mortality.csv', encoding="cp1252")
country_df = cancer_df['Country']
geolocator = Nominatim(user_agent="geoapi")


latitudes = []
longitudes = []
for country in country_df:
    try:
        location = geolocator.geocode(country)
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
    except:
        latitudes.append(None)
        longitudes.append(None)

cancer_df['Latitude'] = latitudes
cancer_df['Longitude'] = longitudes

cleaned_cancer_df = cancer_df.dropna(subset=['Latitude', 'Longitude'])

cleaned_cancer_df.to_csv("cancer_mortality.csv", index=False, encoding="utf-8")





