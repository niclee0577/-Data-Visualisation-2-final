import pandas as pd

df = pd.read_csv("multi_donutchart_mor_updt.csv")



for col in ["Male","Female","Total Cancer Patients"]:
    df[col] = df[col].astype(str).str.replace(",","").astype(int)

# Aggregate by continent
df = df.groupby("Continent", as_index=False).agg({"Male":"sum","Female":"sum", "Total Cancer Patients": "sum"})

df["male percentage"] = (df["Male"] / df["Total Cancer Patients"] ) * 100
df["female percentage"] = (df["Female"] / df["Total Cancer Patients"] ) * 100

# Keep only the columns we need
df = df[[ "Continent", "male percentage", "female percentage", "Male", "Female"]]

# Melt into long format
df_long = df.melt(id_vars=["Continent", "Male", "Female"],
                  value_vars=["male percentage", "female percentage"],
                  var_name="Gender",
                  value_name="percentage")

df_long.to_csv("multi_donutchart_mor_check_updt.csv", index=False)
