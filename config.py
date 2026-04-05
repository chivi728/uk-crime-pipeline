DB_PATH = "uk_crime.db"

# Sussex Police neighbourhood areas
# These are real Sussex Police force area codes
FORCE = "sussex"

# Crime categories available from the API
CRIME_CATEGORIES = [
    "anti-social-behaviour",
    "burglary",
    "robbery",
    "vehicle-crime",
    "violent-crime",
    "shoplifting",
    "criminal-damage-arson",
    "drugs",
    "theft-from-the-person",
    "public-order",
]

# Locations across Sussex to query
# lat/lng coordinates for key Sussex towns
LOCATIONS = [
    {"name": "Brighton",    "lat": 50.8229, "lng": -0.1363},
    {"name": "Worthing",    "lat": 50.8120, "lng": -0.3714},
    {"name": "Crawley",     "lat": 51.1093, "lng": -0.1872},
    {"name": "Eastbourne",  "lat": 50.7692, "lng": 0.2799},
    {"name": "Hastings",    "lat": 50.8543, "lng": 0.5730},
    {"name": "Lewes",       "lat": 50.8742, "lng": 0.0148},
    {"name": "Chichester",  "lat": 50.8365, "lng": -0.7792},
    {"name": "Horsham",     "lat": 51.0632, "lng": -0.3246},
]

# Date to fetch crimes for (YYYY-MM format)
# Use a recent month — API has a few months lag
FETCH_DATE = "2025-12"