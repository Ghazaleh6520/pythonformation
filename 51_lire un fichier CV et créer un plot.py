import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("orders.csv")

sales_by_country = orders.groupby("ShipCountry")["Freight"].sum()

sales_by_country.sort_values().plot(kind="barh")
plt.title("Sales by Country")
plt.show()