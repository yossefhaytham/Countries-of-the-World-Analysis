import requests
from bs4 import BeautifulSoup
import pandas as pd


# URL of the website
URL = "https://www.scrapethissite.com/pages/simple/"

# Send HTTP request
response = requests.get(URL)
response.raise_for_status()  # Raise error if request fails

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all country containers
countries = soup.find_all("div", class_="country")

# Prepare data storage
data = []

# Loop through each country
for country in countries:
    name = country.find("h3", class_="country-name").get_text(strip=True)
    capital = country.find("span", class_="country-capital").get_text(strip=True)
    population = country.find("span", class_="country-population").get_text(strip=True)
    area = country.find("span", class_="country-area").get_text(strip=True)

    # Clean numeric values
    population = int(float(population))
    area = float(area)

    data.append({
        "Country": name,
        "Capital": capital,
        "Population": population,
        "Area_km2": area
    })

# Create DataFrame
df = pd.DataFrame(data)

# Optional: sort alphabetically
df = df.sort_values(by="Country").reset_index(drop=True)

# Save to CSV
df.to_csv("countries_data.csv", index=False)

print("Scraping completed successfully.")
print(df.head())
