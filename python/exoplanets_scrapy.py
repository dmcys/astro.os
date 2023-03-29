from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np

# List of exoplanets
exoplanets = ["WASP-121b", "HD 209458b", "KELT-9b", "TRAPPIST-1e", "Proxima Centauri b"]

# Empty arrays to store coordinates
ra = np.zeros(len(exoplanets))
dec = np.zeros(len(exoplanets))

# Loop through each exoplanet and get coordinates
for i, planet in enumerate(exoplanets):
    coords = SkyCoord.from_name(planet)
    ra[i] = coords.ra.deg
    dec[i] = coords.dec.deg

# Save coordinates to a text file
with open("exoplanet_coords.txt", "w") as f:
    for i in range(len(exoplanets)):
        f.write(f"{exoplanets[i]}: {ra[i]:.6f} {dec[i]:.6f}\n")
