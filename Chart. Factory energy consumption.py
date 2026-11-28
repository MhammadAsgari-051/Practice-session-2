
import matplotlib.pyplot as plt

sections = ["Motors", "Lighting", "Cooling", "Heating", "Other"]
energy = [450, 100, 250, 150, 50]

plt.figure(figsize=(8, 6))

plt.pie(  energy,  labels=sections, autopct="%1.1f%%", startangle=90)

plt.title("Factory Energy Consumption")
plt.show()
