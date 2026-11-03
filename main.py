
import csv
import matplotlib.pyplot as plt
from scraper import scrape_books

print("======================================")
print(" WEB SCRAPING AND DATA VISUALIZATION")
print("======================================")

# STEP 1: Scrape website data
print("\nStep 1: Collecting book data...")

books = scrape_books()

print("Total books collected:", len(books))


# STEP 2: Save data in CSV
print("\nStep 2: Saving data...")

with open("products.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["Title", "Price", "Availability"]
    )

    writer.writeheader()
    writer.writerows(books)

print("Data saved successfully!")


# STEP 3: Prepare data for graph
titles = []
prices = []

for book in books:

    titles.append(book["Title"][:15])

    price = float(
        book["Price"].replace("£", "").replace("Â", "")
    )

    prices.append(price)


# STEP 4: Create graph
print("\nStep 3: Creating graph...")

plt.figure(figsize=(12, 6))

plt.bar(titles, prices)

plt.xlabel("Book Names")
plt.ylabel("Price (£)")

plt.title("Book Price Comparison")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("book_prices.png")

print("Graph saved successfully!")

plt.show()

print("\n======================================")
print(" PROJECT COMPLETED SUCCESSFULLY!")
print("======================================")

