import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# -------------------------------
# Configuration
# -------------------------------
n_users = 1000
n_days = 30
np.random.seed(42)  # Reproducibility

OUTPUT_DIR = r"C:\Users\mithr\Documents"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "user_engagement_raw.csv")

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

    # Simulate fluctuating Daily Active Users (DAU)
    daily_active_count = np.random.randint(600, 1000)

    # Weekend dip (optional but realistic)
    if current_date.weekday() >= 5:  # Saturday / Sunday
        daily_active_count = np.random.randint(500, 800)

    active_today = np.random.choice(
        users,
        size=daily_active_count,
        replace=False
    )

    for user in active_today:
        sessions = np.random.poisson(1)
        pages = np.random.randint(1, 10)
        time_spent = np.random.randint(30, 600)

        # Churn probability based on engagement
        churn_prob = 0.15 if sessions == 0 else 0.05
        churn_flag = np.random.choice([0, 1], p=[1 - churn_prob, churn_prob])

        data.append([
            user,
            current_date.date(),
            sessions,
            pages,
            time_spent,
            churn_flag
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

print("Dataset generated successfully!")
print(f"File path: {OUTPUT_FILE}")
print(f"Total rows: {len(df)}")
print(f"Date range: {df['date'].min()} → {df['date'].max()}")
