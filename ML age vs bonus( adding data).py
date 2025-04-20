

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#📊 Step 1: কৃত্রিম ডেটা তৈরি
data = {
    'Name': ['Sakib', 'Ratul', 'Nishat', 'Shuvo', 'Riya'],
    'Age': [29, np.nan, 33, 27, 31],
    'Department': ['IT', 'HR', 'Sales', 'IT', 'HR'],
    'Salary': [50000, 45000, np.nan, 47000, 52000]
}
df = pd.DataFrame(data)

#🧹 Step 2: ডেটা ক্লিনিং
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

#💰 Step 3: নতুন Bonus কলাম যোগ
df['Bonus'] = df['Salary'] * 0.10

#🎨 Step 4: ভিজুয়ালাইজেশন

#Pie Chart: ডিপার্টমেন্ট অনুযায়ী 


#Line Plot: বয়স অনুযায়ী Bonus
plt.figure(figsize=(8,5))
plt.plot(df['Age'], df['Bonus'], marker='o', linestyle='-', color='purple')
plt.title('📈 Bonus vs Age')
plt.xlabel('Age')
plt.ylabel('Bonus')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()



