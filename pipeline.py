from config import LOCATIONS, FETCH_DATE
from fetch import fetch_crimes, fetch_force_info
from transform import transform
from store import init_db, save

def run():
    print("🚔 Starting UK Crime Data Pipeline...\n")
    init_db()

    # Show Sussex Police info
    force = fetch_force_info()
    if force:
        print(f"  Force: {force.get('name', 'Sussex Police')}")
        description = force.get('description') or ''
        print(f"  {description[:100]}...\n")

    all_records = []
    for location in LOCATIONS:
        print(f"  Fetching crimes: {location['name']}...")
        records = fetch_crimes(location, FETCH_DATE)
        if records:
            all_records.extend(records)
            print(f"    ✓ {len(records)} crimes found")
        else:
            print(f"    ✗ No data returned")

    if not all_records:
        print("\nNo data fetched. Check your connection.")
        return

    df = transform(all_records)
    save(df)

    print(f"\n✅ Pipeline complete!")
    print(f"   Total crimes fetched:  {len(df)}")
    print(f"   Towns covered:         {df['location_name'].nunique()}")
    print(f"   Most common crime:     {df['category_label'].value_counts().index[0]}")
    print(f"   High severity crimes:  {len(df[df['severity'] == 'High'])}")
    print(f"\n   Run visualise.py to see your dashboard.")

if __name__ == "__main__":
    run()