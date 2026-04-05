import requests

BASE_URL = "https://data.police.uk/api"

def fetch_crimes(location: dict, date: str) -> list[dict]:
    """Fetch crimes near a location for a given month."""
    url = f"{BASE_URL}/crimes-street/all-crime"
    params = {
        "lat":  location["lat"],
        "lng":  location["lng"],
        "date": date,
    }
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        crimes = response.json()

        records = []
        for crime in crimes:
            records.append({
                "location_name":  location["name"],
                "category":       crime.get("category", "unknown"),
                "month":          crime.get("month", date),
                "street":         crime.get("location", {}).get("street", {}).get("name", ""),
                "outcome":        crime.get("outcome_status", {}).get("category", "No outcome yet")
                                  if crime.get("outcome_status") else "No outcome yet",
                "persistent_id":  crime.get("persistent_id", ""),
            })
        return records

    except requests.RequestException as e:
        print(f"  [ERROR] Could not fetch crimes for {location['name']}: {e}")
        return []

def fetch_force_info() -> dict:
    """Fetch basic info about Sussex Police."""
    url = f"{BASE_URL}/forces/sussex"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"  [ERROR] Could not fetch force info: {e}")
        return {}