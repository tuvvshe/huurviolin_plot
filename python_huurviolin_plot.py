
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
plt.figure(figsize=(10, 8))
sns.violinplot(x=data["total_bill"])
plt.show()


plt.figure(figsize=(12, 10))
sns.violinplot(x="day", y="total_bill", data=data)
plt.show()