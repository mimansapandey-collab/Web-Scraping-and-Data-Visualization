
import csv
import matplotlib.pyplot as plt

# Read data from CSV file
titles = []
prices = []

with open("products.csv", "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        titles.append(row["Title"][:15])

        # Convert price into number
        price = float(
            row["Price"].replace("£", "").replace("Â", "")
        )

        prices.append(price)


# Create bar chart
plt.figure(figsize=(12, 6))

plt.bar(titles, prices)

plt.xlabel("Book Names")
plt.ylabel("Price (£)")

plt.title("Book Price Comparison")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save graph
plt.savefig("book_prices.png")

# Display graph
plt.show()

print("Graph created successfully!")
