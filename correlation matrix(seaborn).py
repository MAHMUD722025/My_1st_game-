import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#📚 কৃত্রিম ডেটাসেট
data = {
    'Math': [90, 80, 75, 60, 95],
    'Physics': [85, 78, 70, 65, 92],
    'Chemistry': [88, 82, 72, 66, 94],
    'Biology': [75, 70, 68, 80, 85]
}

df = pd.DataFrame(data)

#🧠 Step: Correlation ম্যাট্রিক্স তৈরি
correlation_matrix = df.corr()

#🔥 Heatmap তৈরি
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("📈 Subject-wise Correlation Heatmap", fontsize=14)
plt.tight_layout()
plt.show()