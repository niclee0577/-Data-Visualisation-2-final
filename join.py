import pandas as pd

# Load both datasets
mortality = pd.read_csv("cancer_mortality_updt.csv")
prevalence = pd.read_csv("prevalence cases.csv", encoding="cp1252")

aliases = {
    "Bolivia (Plurinational State of)": "Bolivia",
    "Bosnia Herzegovina": "Bosnia and Herzegovina",
    "Cape Verde": "Cabo Verde",
    "C�te d'Ivoire": "Côte d'Ivoire",
    "Czechia": "Czech Republic",
    "Iran, Islamic Republic of": "Iran",
    "Lao People's Democratic Republic": "Laos",
    "Republic of Moldova": "Moldova",
    "Korea, Democratic People Republic of": "North Korea",
    "Korea, Republic of": "South Korea",
    "Russian Federation": "Russian Federation",  # already matches mortality file
    "Syrian Arab Republic": "Syria",
    "Tanzania, United Republic of": "Tanzania",
    "T�rkiye": "Türkiye",
    "United States of America": "United States",
    "Viet Nam": "Vietnam",
    "French Guyana": "French Guiana",
    "France (metropolitan)": "France",
    "France, Guadeloupe": "Guadeloupe",
    "France, La R�union": "Réunion",
    "France, Martinique": "Martinique",
    "Gaza Strip and West Bank": "Palestine",
    "Congo, Democratic Republic of": "Democratic Republic of the Congo",
    "Congo, Republic of": "Republic of the Congo",
    "The Netherlands": "Netherlands",
    "The Republic of the Gambia": "Gambia",
    "Timor-Leste": "East Timor"  # or keep "Timor-Leste" if you add it to mortality
}

# Apply alias mapping to prevalence dataset
prevalence["Country"] = prevalence["Country"].replace(aliases)

# Now merge on Country
merged = pd.merge(mortality, prevalence, on="Country", how="inner")
merged.to_csv("prevalence_mortality_updt.csv", index=False, encoding="utf-8")
