# UK Crime Data Pipeline 🚔

A Python ETL pipeline that extracts real crime data from the official UK Police API for key Sussex towns, transforms it with Pandas, and generates a visual dashboard using Matplotlib and Seaborn.

---

## 📊 Dashboard Output

| Crimes by Town | Top Crime Categories |
|---|---|
| Bar chart ranking Sussex towns by total recorded crimes | Bar chart showing the most frequent crime categories |

| Severity Breakdown | Resolution Rate |
|---|---|
| Pie chart showing High / Medium / Low severity split | Bar chart showing % of crimes resolved per town |

---

## 🛠️ Tech Stack

- **Data Source:** UK Police Open Data API (data.police.uk) — no API key required
- **Python:** requests, pandas, matplotlib, seaborn
- **Database:** SQLite
- **Environment:** WSL Ubuntu, VS Code

---

## 📁 Project Structure

```
uk_crime_pipeline/
│
├── config.py         # Force area, locations and settings
├── fetch.py          # API requests to data.police.uk
├── transform.py      # Data cleaning and enrichment
├── store.py          # SQLite database operations
├── visualise.py      # Dashboard chart generation
├── pipeline.py       # Main ETL orchestrator
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### 1. Extract
Connects to the official UK Police API and fetches recorded street crimes for 8 Sussex towns — Brighton, Worthing, Crawley, Eastbourne, Hastings, Lewes, Chichester and Horsham — for a specified month.

### 2. Transform
- Maps raw API category slugs to human-readable labels
- Adds a **severity group** (High / Medium / Low) based on crime category
- Cleans street name strings
- Flags crimes as resolved or unresolved based on outcome status

### 3. Load
Appends transformed records to a local SQLite database (`uk_crime.db`), building up historical data across multiple pipeline runs.

### 4. Visualise
Reads all stored records from SQLite and generates a 4-panel PNG dashboard showing crime counts, category breakdown, severity split and resolution rates by town.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- WSL Ubuntu or Linux terminal
- Internet connection (API calls to data.police.uk)

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/uk-crime-pipeline.git
cd uk-crime-pipeline
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure settings (optional)
Update `config.py` to change the target month or locations:
```python
FETCH_DATE = "2024-09"   # YYYY-MM format

LOCATIONS = [
    {"name": "Brighton", "lat": 50.8229, "lng": -0.1363},
    # add more towns here
]
```

### 5. Run the pipeline
```bash
python pipeline.py
```

### 6. Generate the dashboard
```bash
python -c "from visualise import plot_dashboard; plot_dashboard()"
```

---

## 🗺️ Towns Covered

| Town | Latitude | Longitude |
|---|---|---|
| Brighton | 50.8229 | -0.1363 |
| Worthing | 50.8120 | -0.3714 |
| Crawley | 51.1093 | -0.1872 |
| Eastbourne | 50.7692 | 0.2799 |
| Hastings | 50.8543 | 0.5730 |
| Lewes | 50.8742 | 0.0148 |
| Chichester | 50.8365 | -0.7792 |
| Horsham | 51.0632 | -0.3246 |

---

## 🔍 Sample API Endpoint

**Street crimes near Brighton — September 2024**
```
https://data.police.uk/api/crimes-street/all-crime?lat=50.8229&lng=-0.1363&date=2024-09
```

**Sussex Police force info**
```
https://data.police.uk/api/forces/sussex
```

---

## 🔒 Note on API Access
This project uses the UK Police open data API which is completely free and requires no API key or authentication. Data is publicly available under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

---

## 👤 Author
Jose Reina — Data Engineering Portfolio Project

