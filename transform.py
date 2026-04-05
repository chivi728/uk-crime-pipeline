import pandas as pd

# Map API category slugs to readable names
CATEGORY_LABELS = {
    "anti-social-behaviour":    "Anti-Social Behaviour",
    "burglary":                 "Burglary",
    "robbery":                  "Robbery",
    "vehicle-crime":            "Vehicle Crime",
    "violent-crime":            "Violent Crime",
    "shoplifting":              "Shoplifting",
    "criminal-damage-arson":    "Criminal Damage & Arson",
    "drugs":                    "Drugs",
    "theft-from-the-person":    "Theft from Person",
    "public-order":             "Public Order",
    "other-theft":              "Other Theft",
    "other-crime":              "Other Crime",
    "possession-of-weapons":    "Weapons Possession",
    "bicycle-theft":            "Bicycle Theft",
}

# Severity grouping for reporting
def severity_group(category: str) -> str:
    high = ["violent-crime", "robbery", "possession-of-weapons",
            "criminal-damage-arson"]
    medium = ["burglary", "drugs", "public-order", "theft-from-the-person"]
    if category in high:
        return "High"
    elif category in medium:
        return "Medium"
    else:
        return "Low"

def transform(records: list[dict]) -> pd.DataFrame:
    """Clean and enrich raw crime records."""
    if not records:
        return pd.DataFrame()

    df = pd.DataFrame(records)

    # Add readable category label
    df["category_label"] = df["category"].map(CATEGORY_LABELS).fillna("Other")

    # Add severity group
    df["severity"] = df["category"].apply(severity_group)

    # Clean street names
    df["street"] = df["street"].str.replace("On or near ", "", regex=False).str.strip()

    # Flag resolved vs unresolved crimes
    df["is_resolved"] = ~df["outcome"].isin([
        "No outcome yet",
        "Under investigation",
        "Unable to prosecute suspect",
    ])

    # Reorder columns
    cols = ["month", "location_name", "category", "category_label",
            "severity", "street", "outcome", "is_resolved", "persistent_id"]
    return df[cols]