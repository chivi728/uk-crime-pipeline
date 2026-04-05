import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from store import load_all

SEVERITY_COLORS = {
    "High":   "#e74c3c",
    "Medium": "#f39c12",
    "Low":    "#2ecc71",
}

def plot_dashboard():
    df = load_all()
    if df.empty:
        print("No data yet. Run the pipeline first.")
        return

    sns.set_theme(style="darkgrid")
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle("🚔 Sussex Police Crime Data Dashboard", 
                 fontsize=17, fontweight="bold")

    # --- 1. Crime count by town ---
    town_counts = (df.groupby("location_name")
                     .size()
                     .sort_values(ascending=False)
                     .reset_index(name="count"))
    sns.barplot(data=town_counts, x="count", y="location_name",
                palette="Reds_r", ax=axes[0, 0])
    axes[0, 0].set_title("Total Crimes by Town")
    axes[0, 0].set_xlabel("Number of Crimes")
    axes[0, 0].set_ylabel("")

    # --- 2. Crime category breakdown ---
    cat_counts = (df.groupby("category_label")
                    .size()
                    .sort_values(ascending=False)
                    .head(8)
                    .reset_index(name="count"))
    sns.barplot(data=cat_counts, x="count", y="category_label",
                palette="Blues_r", ax=axes[0, 1])
    axes[0, 1].set_title("Top Crime Categories")
    axes[0, 1].set_xlabel("Number of Crimes")
    axes[0, 1].set_ylabel("")

    # --- 3. Severity breakdown pie ---
    sev_counts = df["severity"].value_counts()
    colors = [SEVERITY_COLORS.get(s, "#95a5a6") for s in sev_counts.index]
    axes[1, 0].pie(sev_counts, labels=sev_counts.index,
                   autopct="%1.0f%%", colors=colors, startangle=90)
    axes[1, 0].set_title("Crime Severity Breakdown")

    # --- 4. Resolution rate by town ---
    resolution = (df.groupby("location_name")["is_resolved"]
                    .mean()
                    .mul(100)
                    .round(1)
                    .sort_values(ascending=False)
                    .reset_index())
    resolution.columns = ["location_name", "resolution_pct"]
    sns.barplot(data=resolution, x="resolution_pct", y="location_name",
                palette="Greens_r", ax=axes[1, 1])
    axes[1, 1].set_title("Crime Resolution Rate by Town (%)")
    axes[1, 1].set_xlabel("% Resolved")
    axes[1, 1].set_ylabel("")
    axes[1, 1].set_xlim(0, 100)

    plt.tight_layout()
    plt.savefig("dashboard.png", dpi=150)
    print("  Dashboard saved as dashboard.png")
    plt.show()