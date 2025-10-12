import pandas as pd

df = pd.read_csv("dot_plot_data.csv")

# Melt into long format
df_long = df.melt(id_vars=["Cancer Type"],
                  value_vars=["New incidence cases", "Mortality cases"],
                  var_name="Type of Cases",
                  value_name="Number of Cases")

df_long.to_csv("dot_plot_data_check.csv", index=False)