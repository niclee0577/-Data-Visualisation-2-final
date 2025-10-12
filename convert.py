import pandas as pd
from geopy.geocoders import Nominatim
import pycountry

cancer_df = pd.read_csv('prevalence cases.csv', encoding="cp1252")
country_df = cancer_df['Country']
geolocator = Nominatim(user_agent="geoapi")
cancer_df = cancer_df.drop(columns=["Numeric Code", "Latitude", "Longitude"], errors='ignore')

aliases = {
    "Bolivia (Plurinational State of)": "Bolivia",
    "Bosnia Herzegovina": "Bosnia and Herzegovina",
    "Cape Verde": "Cabo Verde",
    "Congo, Democratic Republic of": "Democratic Republic of the Congo",
    "Congo, Republic of": "Republic of the Congo",
    "Côte d'Ivoire": "Côte d'Ivoire",
    "Czechia": "Czech Republic",
    "France (metropolitan)": "France",
    "France, Guadeloupe": "Guadeloupe",
    "France, La Réunion": "Réunion",
    "France, Martinique": "Martinique",
    "French Guyana": "French Guiana",
    "Gaza Strip and West Bank": "Palestine",
    "Iran, Islamic Republic of": "Iran",
    "Korea, Democratic People Republic of": "North Korea",
    "Korea, Republic of": "South Korea",
    "Lao People's Democratic Republic": "Laos",
    "Republic of Moldova": "Moldova",
    "Syrian Arab Republic": "Syria",
    "Tanzania, United Republic of": "Tanzania",
    "The Netherlands": "Netherlands",
    "The Republic of the Gambia": "Gambia",
    "United States of America": "United States",
    "Viet Nam": "Vietnam"

}

def normalize_country(name):
    return aliases.get(name, name)

latitudes = []
longitudes = []
numeric_code = []
for country in country_df:
    try:
        cancer_df["Country"] = cancer_df['Country'].normalize_country(country)
        numeric_code_value = int(pycountry.countries.lookup(country).numeric)
        print(f"Processing {country} with numeric code {numeric_code_value}")
        location = geolocator.geocode(country)
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
        numeric_code.append(numeric_code_value)
    except:
        print(f"Could not process {country}")
        latitudes.append(None)
        longitudes.append(None)
        numeric_code.append(None)


cancer_df["NumericCode"] = numeric_code
cancer_df['Latitude'] = latitudes
cancer_df['Longitude'] = longitudes

cleaned_cancer_df = cancer_df.dropna(subset=['Latitude', 'Longitude', 'NumericCode']).copy()
cleaned_cancer_df["NumericCode"] = cleaned_cancer_df["NumericCode"].astype(int)
cleaned_cancer_df.to_csv("multi_donutchart_updt.csv", index=False, encoding="utf-8")









