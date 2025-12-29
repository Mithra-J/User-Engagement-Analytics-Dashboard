import pandas as pd

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\mithr\OneDrive\문서\User-Engagement-Analytics-Dashboard\user_engagement_cleaned.csv")

# Ensure date column is datetime
df['date'] = pd.to_datetime(df['date'])

# 1️⃣ Daily Active Users
dau = df.groupby('date')['user_id'].nunique().reset_index()
dau.columns = ['date', 'daily_active_users']

# 2️⃣ Engagement Metrics
engagement = df.groupby('date').agg(
    total_sessions=('sessions', 'sum'),
    avg_pages_visited=('pages_visited', 'mean'),
    avg_time_spent=('time_spent', 'mean')
).reset_index()

# 3️⃣ Daily Churn Rate
churn = df.groupby('date')['churn_flag'].mean().reset_index()
churn.columns = ['date', 'churn_rate']

# 4️⃣ Combine metrics
metrics = dau.merge(engagement, on='date').merge(churn, on='date')

# 5️⃣ Save aggregated metrics
metrics.to_csv(r"C:\Users\mithr\OneDrive\문서\User-Engagement-Analytics-Dashboard\user_engagement_metrics.csv", index=False)

print("Aggregation complete! Metrics saved as 'user_engagement_metrics.csv'")
print(metrics.head())
