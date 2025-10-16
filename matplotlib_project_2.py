import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\New folder\Program1\Main\Python Library\Employment_Unemployment_GDP_data.csv")

""" Ques. Global Trend Over Time (Lineplot)
 How has the global unemployment rate changed over the years?

"""

sns.relplot(data=df, x="Year", y="Unemployment Rate", errorbar="ci",  kind="line")

"""Ques.  Sector Distribution
In the most recent year, what’s the employment split (Agri/Industry/Services) across top 5 economies? **bold text**

"""

top5 = df.nlargest(5, "Year")

top5_melted = top5.melt(
    id_vars="Country Name",
    value_vars=['Employment Sector: Agriculture', 'Employment Sector: Industry', 'Employment Sector: Services'],
    var_name="Sector",
    value_name="Employment"
)
sns.catplot(
    data=top5_melted,
    x="Country Name",
    y="Employment",
    hue="Sector",
    kind="bar"
)

plt.show()

"""Ques. Relationship
Is there a correlation between GDP and Unemployment Rate? **bold text**
"""

sns.regplot(data=df, x="Unemployment Rate", y="GDP (in USD)", scatter=True, fit_reg=True)
df["GDP (in USD)"].corr(df["Unemployment Rate"])
plt.show()

"""Ques. Country Philosophy
 Do countries show different employment strategies?
E.g., Are some still agriculture-heavy vs services-heavy? **bold text**
"""

df_sorted = df.sort_values("GDP (in USD)", ascending=False)
unique_top = df_sorted.drop_duplicates("Country Name").head(10)

#print("\nBest row per category:")
#print(unique_top)

top5_melted = unique_top.melt(
    id_vars="Country Name",
    value_vars=['Employment Sector: Agriculture', 'Employment Sector: Industry', 'Employment Sector: Services'],
    var_name="Sector",
    value_name="Employment"
)
sns.catplot(
    data=top5_melted,
    x="Country Name",
    y="Employment",
    hue="Sector",
    kind="bar",
    height=5,     # height of the chart
    aspect=3
)

plt.xticks(rotation=45)
plt.show()

"""Ques. Change Over Time
 For a specific country (say India, USA, Germany), how did sector employment shift from 1991–latest year?
"""

ho = df[df['Country Name'] == 'India'][['Year', 'Employment Sector: Agriculture', 'Employment Sector: Industry', 'Employment Sector: Services']]

top5_melted = ho.melt(
    id_vars="Year",
    value_vars=['Employment Sector: Agriculture', 'Employment Sector: Industry', 'Employment Sector: Services'],
    var_name="Sector",
    value_name="Employment"
)

sns.relplot(
    data=top5_melted,
    x="Year",
    y="Employment",
    hue="Sector",
    kind="line",
    marker="o",
    height=5,
    aspect=3
)

plt.show()

"""Ques. Multi-variable Comparison (Pairplot)
 Compare GDP, Unemployment, and 3 employment sectors simultaneously. **bold text**
"""

cols = ['GDP (in USD)', 'Employment Sector: Agriculture', 'Employment Sector: Industry', 'Employment Sector: Services', 'Unemployment Rate']

sns.pairplot(df[cols], diag_kind="kde", corner=True)
plt.show()

"""Ques. Heatmap (Final Summary)
 Which countries have the highest unemployment vs GDP across years?
"""

p = pd.pivot_table(
    df,
    values="Unemployment Rate",
    index="Country Name",
    columns="Year",
    aggfunc="mean"
)

p_small = p.loc[p.index[:10]]
sns.heatmap(p_small, annot=True, cmap="YlGnBu", linewidths=1)
plt.show()
