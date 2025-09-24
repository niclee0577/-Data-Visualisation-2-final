import pandas as pd
from geopy.geocoders import Nominatim
import pycountry

cancer_df = pd.read_csv('cancer_mortality.csv', encoding="cp1252")
country_df = cancer_df['Country']
geolocator = Nominatim(user_agent="geoapi")
cancer_df = cancer_df.drop(columns=["Numeric Code", "Latitude", "Longitude"], errors='ignore')



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


cancer_df["NumericCode"] = numeric_code

cancer_df['Latitude'] = latitudes
cancer_df['Longitude'] = longitudes

cleaned_cancer_df = cancer_df.dropna(subset=['Latitude', 'Longitude', 'NumericCode']).copy()
cleaned_cancer_df["NumericCode"] = cleaned_cancer_df["NumericCode"].astype(int)
cleaned_cancer_df.to_csv("cancer_mortality.csv", index=False, encoding="utf-8")





