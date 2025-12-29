import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# -------------------------------
# Configuration
# -------------------------------
n_users = 1000
n_days = 30
np.random.seed(42)  # For reproducibility

# Output directory
OUTPUT_DIR = r"C:\Users\mithr\Documents"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "user_engagement.csv")

# -------------------------------
# Generate users
# -------------------------------
users = [f"user_{i}" for i in range(1, n_users + 1)]

# -------------------------------
# Generate engagement data
# -------------------------------
data = []
start_date = datetime(2025, 12, 1)

for day in range(n_days):
    current_date = start_date + timedelta(days=day)
    for user in users:
        sessions = np.random.poisson(1)        # Avg 1 session/day
        pages = np.random.randint(1, 10)       # Pages visited
        time_spent = np.random.randint(30, 600)  # Seconds
        churn = np.random.choice([0, 1], p=[0.9, 0.1])

        data.append([
            user,
            current_date.date(),
            sessions,
            pages,
            time_spent,
            churn
        ])

# -------------------------------
# Create DataFrame
# -------------------------------
df = pd.DataFrame(
    data,
    columns=[
        "user_id",
        "date",
        "sessions",
        "pages_visited",
        "time_spent",
        "churn_flag"
    ]
)

# -------------------------------
# Save dataset
# -------------------------------
df.to_csv(OUTPUT_FILE, index=False)

print(f"Dataset generated successfully at: {OUTPUT_FILE}")
print(f"Total rows: {len(df)}")
