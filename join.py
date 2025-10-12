import pandas as pd

# Load both datasets
mortality = pd.read_csv("cancer_mortality_updt.csv")
prevalence = pd.read_csv("prevalence cases.csv", encoding="cp1252")
incidence = pd.read_csv("Global cancer mortality in males and females (2022).csv", encoding="cp1252")
prevalence_mortality = pd.read_csv("prevalence_mortality_updt.csv",encoding="cp1252")


# Define alias dictionary
aliases = {
    "Russia": "Russian Federation",
    "Turkey": "TÃƒÆ’Ã‚Â¼rkiye",
    "C“te d?Ivoire": "CÃƒÆ’Ã‚Â´te d'Ivoire",
    "R�union": "Réunion",
    "Brunei": "Brunei Darussalam",
    "Cape Verde": "Cabo Verde"
}


# aliases = {
#     "Bolivia (Plurinational State of)": "Bolivia",
#     "Bosnia Herzegovina": "Bosnia and Herzegovina",
#     "Cape Verde": "Cabo Verde",
#     "C�te d'Ivoire": "Côte d'Ivoire",
#     "Czechia": "Czech Republic",
#     "Iran, Islamic Republic of": "Iran",
#     "Lao People's Democratic Republic": "Laos",
#     "Republic of Moldova": "Moldova",
#     "Korea, Democratic People Republic of": "North Korea",
#     "Korea, Republic of": "South Korea",
#     "Russian Federation": "Russian Federation",  
#     "Syrian Arab Republic": "Syria",
#     "Tanzania, United Republic of": "Tanzania",
#     "T�rkiye": "Türkiye",
#     "United States of America": "United States",
#     "Viet Nam": "Vietnam",
#     "French Guyana": "French Guiana",
#     "France (metropolitan)": "France",
#     "France, Guadeloupe": "Guadeloupe",
#     "France, La R�union": "Réunion", 
#     "France, Martinique": "Martinique",
#     "Gaza Strip and West Bank": "Palestine",
#     "Congo, Democratic Republic of": "Democratic Republic of the Congo",
#     "Congo, Republic of": "Republic of the Congo",
#     "The Netherlands": "Netherlands",
#     "The Republic of the Gambia": "Gambia",
#     "Timor-Leste": "East Timor"  
# }

# Apply alias mapping to prevalence dataset
incidence["Country"] = incidence["Country"].replace(aliases)


# Now merge on Country
merged = pd.merge(prevalence_mortality, incidence, on="Country", how="inner")

# Countries in incidence but not in prevalence
# missing_from_prevalence = set(incidence["Country"]) - set(prevalence_mortality["Country"])

# Countries in prevalence but not in incidence
missing_from_incidence = set(prevalence_mortality["Country"]) - set(merged["Country"])

# print("Missing from prevalence:", missing_from_prevalence)
print("Missing from incidence:", missing_from_incidence)

merged.to_csv("multi_donutchart_mor_updt.csv", index=False, encoding="utf-8")
