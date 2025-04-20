
import pandas as pd
import matplotlib.pyplot as plt

#DataFrame তৈরি
data = {'Work Type': ['Group work', 'Personal work'], 'Percentage': [74, 26]}
df = pd.DataFrame(data)

#Pie (Donut) Chart
plt.figure(figsize=(6,6))
plt.pie(
    df['Percentage'],
    labels=df['Work Type'],
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.4},
    colors=['seagreen', 'lightblue'],
    pctdistance=1.2
)
plt.title('Classroom Collaboration')
plt.legend()
plt.tight_layout()
plt.show()




