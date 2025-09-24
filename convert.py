import pandas as pd
from geopy.geocoders import Nominatim
import pycountry

cancer_df = pd.read_csv('cancer_mortality.csv', encoding="cp1252")
country_df = cancer_df['Country']
geolocator = Nominatim(user_agent="geoapi")
cancer_df.drop(columns=['ISO3'], inplace=True)

latitudes = []
longitudes = []
numeric_code = []
for country in country_df:
    try:
        numeric_code_value = int(pycountry.countries.lookup(country).numeric)
        location = geolocator.geocode(country)
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
        numeric_code.append(numeric_code_value)
    except:
        latitudes.append(None)
        longitudes.append(None)
        numeric_code.append(None)


cancer_df["Numeric Code"] = numeric_code
cancer_df['Latitude'] = latitudes
cancer_df['Longitude'] = longitudes

cleaned_cancer_df = cancer_df.dropna(subset=['Latitude', 'Longitude', 'Numeric Code'])

cleaned_cancer_df.to_csv("cancer_mortality.csv", index=False, encoding="utf-8")





