import requests

# Make a GET request to the API to retrieve confirmed exoplanet names
response = requests.get("https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_name")

# Parse the response JSON and extract the exoplanet names
exoplanet_names = [row["pl_name"] for row in response.json()]

# Print the exoplanet names
print(exoplanet_names)
