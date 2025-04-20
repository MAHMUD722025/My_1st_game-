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

#Pie Chart: ডিপার্টমেন্ট অনুযায়ী কর্মীর বণ্টন
plt.figure(figsize=(6,6))
df['Department'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'orange', 'skyblue'])
plt.title('🏢 Department-wise Employee Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()



