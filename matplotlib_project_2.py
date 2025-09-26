import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\DELL\Downloads\Liverpool.csv")

"""Ques. Home vs Away Performance Gap

Problem:
Does Liverpool perform significantly better at home than away?

Create a side-by-side bar chart comparing average Goals scored and average Goals conceded in Home vs Away matches.

Add exact values above each bar. **bold text**
"""

home_goals = df[df['Is_Home'] == 1]['Goals'].mean()
home_conceded = df[df['Is_Home'] == 1]['Opponent_Goals'].mean()

away_goals = df[df['Is_Home'] == 0]['Goals'].mean()
away_conceded = df[df['Is_Home'] == 0]['Opponent_Goals'].mean()

labels = ['Home', 'Away']
goals_scored = [home_goals, away_goals]
goals_conceded = [home_conceded, away_conceded]

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(len(labels))  # [0, 1] → positions for Home, Away
width = 0.35  # bar width

fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width/2, goals_scored, width, label='Goals Scored', color='green')
bars2 = ax.bar(x + width/2, goals_conceded, width, label='Goals Conceded', color='red')

# Add labels, title, ticks
ax.set_ylabel('Average Goals')
ax.set_title('Liverpool Home vs Away Performance')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),  # 3 points above bar
                    textcoords="offset points",
                    ha='center', va='bottom')

plt.tight_layout()
plt.show()

"""Ques. Match Outcome Breakdown

Problem:
The club’s management wants a clear view of how often matches end in Win, Draw, or Loss.

Create a pie chart showing the distribution of results (Result column).

Use percentages and labels.

Add a title: “Liverpool Match Outcomes”.
"""

h1 = df[df['Result'] == 1]['Result'].value_counts().reset_index()
h2 = df[df['Result'] == 0]['Result'].value_counts().reset_index()
h3 = df[df['Result'] == -1]['Result'].value_counts().reset_index()

g = [h1.iloc[0, 1], h2.iloc[0, 1], h3.iloc[0, 1]]
label = ['Win', 'Draw', 'Loss']

plt.pie(g, labels=label, autopct='%1.1f%%')
plt.title('Liverpool Match Outcomes')
plt.show()

"""Ques. Shot Efficiency vs Goals

Problem:
Is higher shot efficiency actually leading to more goals?

Plot a scatter plot with Shot_Efficiency on the x-axis and Goals on the y-axis.

Add a trend line to show the overall relationship. **bold text**

"""

x = df['Shot_Efficiency']
y = df['Goals']

x = x.replace([np.inf, -np.inf], np.nan)
y = y.replace([np.inf, -np.inf], np.nan)
mask = ~(x.isna() | y.isna())
x, y = x[mask], y[mask]

plt.scatter(x, y, alpha=0.5)

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', label='Trendline')

plt.xlabel("Shot Efficiency")
plt.ylabel("Goals")
plt.title("Shot Efficiency vs Goals")
plt.legend()
plt.show()

"""Ques. Opponent Strength Effect

Problem:
Do Liverpool struggle more against strong teams (high possession opponents)?

Create a line plot of Opponent_Possession vs Goals scored by Liverpool.

Group by Opponent (take average values per opponent) and sort by possession.

Highlight top 3 toughest opponents in red markers. **bold text**
"""

df_grouped = df.groupby("Opponent").agg({
    "Opponent_Possession": "mean",
    "Goals": "mean"
}).reset_index()

df_grouped = df_grouped.sort_values(by="Opponent_Possession")

plt.figure(figsize=(16,10))

plt.plot(df_grouped["Opponent_Possession"], df_grouped["Goals"], marker='o')
top3 = df_grouped.nlargest(3, "Opponent_Possession")
plt.scatter(top3["Opponent_Possession"], top3["Goals"], color="red", s=100, label="Top 3")

plt.xlabel("Opponent Possession (%)")
plt.ylabel("Avg Goals by Liverpool")
plt.title("Opponent Strength Effect on Goals")
plt.legend()
plt.show()

"""Ques. Last 5 Match Momentum

Problem:
Does recent momentum (Last5_Win_Rate) correlate with match outcome?

Create a box plot of Last5_Win_Rate split by Result (Win/Draw/Loss).

Check if higher momentum → more wins. **bold text** *italicized text*
"""

h1 = df[df['Result'] == 1]['Last5_Win_Rate']
h2 = df[df['Result'] == 0]['Last5_Win_Rate']
h3 = df[df['Result'] == -1]['Last5_Win_Rate']

g = [h1, h2,h3]

plt.figure(figsize=(8,6))
plt.boxplot(g, labels=['Win', 'Draw', 'Loss'])
plt.title('Liverpool Match Outcomes')
plt.show()