
import requests
from bs4 import BeautifulSoup

def scrape_books():

    url = "https://books.toscrape.com/"

    # Connect to the website
    response = requests.get(url)

    # Read website HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    book_data = []

    # Extract book information
    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).text

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        # Store information
        book_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    return book_data


# Test the scraper
if __name__ == "__main__":

    data = scrape_books()

    for book in data:
        print(book)
