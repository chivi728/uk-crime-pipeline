import sqlite3
import pandas as pd
from config import DB_PATH

def init_db():
    """Create crimes table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS crimes (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            month           TEXT,
            location_name   TEXT,
            category        TEXT,
            category_label  TEXT,
            severity        TEXT,
            street          TEXT,
            outcome         TEXT,
            is_resolved     INTEGER,
            persistent_id   TEXT
        )
    """)
    conn.commit()
    conn.close()

def save(df: pd.DataFrame):
    """Append records to SQLite."""
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("crimes", conn, if_exists="append", index=False)
    conn.close()
    print(f"  Saved {len(df)} records to {DB_PATH}")

def load_all() -> pd.DataFrame:
    """Load all stored crime records."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM crimes", conn)
    conn.close()
    return df