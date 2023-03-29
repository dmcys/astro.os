import requests

# List of URLs to scrape for exoplanet names
urls = [
    "https://exoplanetarchive.ipac.caltech.edu/docs/counts_detail.html",
    "https://exoplanets.nasa.gov/alien-worlds/known-exoplanets/",
    "https://en.wikipedia.org/wiki/List_of_exoplanets",
]

# Empty list to store exoplanet names
exoplanets = []

# Loop through each URL and scrape exoplanet names
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        if "exoplanetarchive" in url:
            # Parse table data from Caltech exoplanet archive
            table = response.text.split("<table")[1].split("</table>")[0]
            for row in table.split("<tr>")[1:]:
                name = row.split("<td>")[1].split("</td>")[0]
                exoplanets.append(name)
        elif "nasa.gov" in url:
            # Parse exoplanet names from NASA exoplanet archive
            names = response.text.split('class="planet-name">')[1:]
            for name in names:
                exoplanets.append(name.split("<")[0])
        elif "wikipedia.org" in url:
            # Parse exoplanet names from Wikipedia
            table = response.text.split('id="Confirmed_exoplanets"')[1].split("</table>")[0]
            for row in table.split("<tr>")[2:]:
                name = row.split("<i>")[1].split("</i>")[0]
                exoplanets.append(name)

# Remove duplicates and sort alphabetically
exoplanets = sorted(list(set(exoplanets)))

# Save exoplanet names to a text file
with open("exoplanet_names.txt", "w") as f:
for name in exoplanets:
f.write(name + "\n")

print("Exoplanet names have been saved to exoplanet_names.txt file.")
