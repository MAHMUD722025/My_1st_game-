
import numpy as np
import matplotlib.pyplot as plt

#ডেটা তৈরি
week_1 = [20, 25, 22, 45, 30]
week_2 = [17, 23, 21, 28, 40]
week_3 = [21, 26, 22, 40, 36]
week_4 = [22, 23, 25, 35, 33]

data = np.array([week_1, week_2, week_3, week_4])

#Heatmap আঁকা
plt.imshow(data, cmap='coolwarm')
plt.colorbar(label='Time (minutes)')
plt.title("Heatmap of Commute Time")
plt.xlabel("Days")
plt.ylabel("Weeks")
plt.show()
