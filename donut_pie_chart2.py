import pandas as pd
import matplotlib.pyplot as plt

data = {'Work Type': ['Group Collaboration Work', 'Personal Work'], 'Percentage': [74, 26]}
df = pd.DataFrame(data)

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    df['Percentage'],
    labels=df['Work Type'],
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.4},
    colors=['seagreen', 'lightblue'],
    textprops={'fontsize': 12},
    pctdistance=1.2
)

for autotext in autotexts:
    autotext.set_fontsize(14)
    autotext.set_color('black')

plt.title("📊 Classroom Collaboration", fontsize=16)
plt.tight_layout()
plt.show()
