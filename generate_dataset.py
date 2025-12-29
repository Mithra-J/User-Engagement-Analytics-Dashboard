import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# Settings
n_users = 1000
n_days = 30
# Generate users
users = [f"user_{i}" for i in range(1, n_users+1)]
# Generate random engagement data
data = []
start_date = datetime(2025, 12, 1)
for day in range(n_days):
    current_date = start_date + timedelta(days=day)
    for user in users:
        sessions = np.random.poisson(1)  # avg 1 session/day
        pages = np.random.randint(1, 10)
        time_spent = np.random.randint(30, 600)  # seconds
        churn = np.random.choice([0,1], p=[0.9,0.1])
        data.append([user, current_date.date(), sessions, pages, time_spent, churn])
# Create DataFrame
df = pd.DataFrame(data, columns=["user_id","date","sessions","pages_visited","time_spent","churn_flag"])
import os
print("Current working directory:", os.getcwd())
# Save CSV
df.to_csv("user_engagement.csv", index=False)
