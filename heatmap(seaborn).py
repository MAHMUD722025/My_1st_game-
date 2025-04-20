
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#🕒 ৪ সপ্তাহের সময়ের ডেটা
week_1 = [20, 25, 22, 45, 30]
week_2 = [17, 23, 21, 28, 40]
week_3 = [21, 26, 22, 40, 36]
week_4 = [22, 23, 25, 35, 33]

#🔢 ২D Array তৈরি (4x5)
data = np.array([week_1, week_2, week_3, week_4])

#🎨 Heatmap আঁকা
sns.heatmap(data, cmap='coolwarm', annot=True, fmt='d')  # annot=True মানে ভেতরে সংখ্যাগুলোও দেখাবে

#🖼️ শো করো
plt.title("Weekly Heatmap of Commute Time")
plt.xlabel("Days")
plt.ylabel("Weeks")
plt.tight_layout()
plt.show()
