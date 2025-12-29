import pandas as pd

# Load raw data
df = pd.read_csv(r"C:\Users\mithr\OneDrive\문서\User-Engagement-Analytics-Dashboard\user_engagement_raw.csv")
print("Raw rows:", len(df))

# Clean
df["date"] = pd.to_datetime(df["date"])
df = df.drop_duplicates()
df = df[df["sessions"] >= 0]
df = df[df["time_spent"] > 0]

print("Cleaned rows:", len(df))

# Save cleaned dataset
df.to_csv(r"C:\Users\mithr\OneDrive\문서\User-Engagement-Analytics-Dashboard\user_engagement_cleaned.csv", index=False)
