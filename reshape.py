import pandas as pd

df = pd.read_csv("prevalence_mortality_updt.csv")

# Keep only the columns we need
df = df[["Country", "IncludingNMSCRateIncidence", "IncludingNMSCRateMortality" , "Continent"]]

# Melt into long format
df_long = df.melt(id_vars=["Country", "Continent"],
                  value_vars=["IncludingNMSCRateIncidence", "IncludingNMSCRateMortality"],
                  var_name="Measure",
                  value_name="Value")

# Clean measure names
df_long["Measure"] = df_long["Measure"].replace({
    "IncludingNMSCRateIncidence": "Incidence",
    "IncludingNMSCRateMortality": "Mortality"
})


# Group by Continent and Measure, then calculate mean
continent_avg = (
    df_long.groupby(["Continent", "Measure"])["Value"]
    .mean()
    .reset_index()
)

continent_avg.to_csv("slope.csv", index=False)
