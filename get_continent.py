import pycountry_convert as pc
import pandas as pd
from geopy.geocoders import Nominatim

cancer_df = pd.read_csv('Global cancer mortality in males and females (2022).csv', encoding="cp1252")
country_df = cancer_df['Country']
geolocator = Nominatim(user_agent="geoapi")

name_corrections = {
    "CÃƒÂ´te d'Ivoire": "Ivory Coast",   # pycountry_convert expects "Ivory Coast"
    "TÃƒÂ¼rkiye": "Turkey"
}

def normalize_country(name):
    return name_corrections.get(name, name)

continent = []
for country in country_df:
    try:
        country = normalize_country(country)
        print(f"Processing {country}")
        country_code = pc.country_name_to_country_alpha2(country)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent.append(pc.convert_continent_code_to_continent_name(continent_code))
    except:
        print(f"Could not process {country}")
        continent.append(None)


cancer_df["Continent"] = continent
cleaned_cancer_df = cancer_df.dropna(subset=['Continent']).copy()
cleaned_cancer_df.to_csv("multi_donutchart_mor_updt.csv", index=False, encoding="utf-8")

