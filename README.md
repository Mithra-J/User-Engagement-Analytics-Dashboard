# 📊 User Engagement Analytics Dashboard

> End-to-end data pipeline that generates, cleans, and aggregates user engagement data for Power BI visualization.

## 🚀 What You Get

Track key engagement metrics with an automated analytics pipeline:

- **Daily Active Users (DAU)** & **Session Analytics**
- **Behavioral Metrics** (page views, time spent)
- **Churn Intelligence** & retention tracking

---

## 📁 Project Structure

```
User-Engagement-Analytics-Dashboard/
│
├── data/
│   ├── user_engagement_raw.csv       # Synthetic raw dataset
│   ├── user_engagement_cleaned.csv   # Processed dataset
│   └── user_engagement_metrics.csv   # Dashboard-ready metrics
│
├── generate_dataset.py               # Creates synthetic data
├── clean_dataset.py                  # Data cleaning pipeline
├── aggregate_dataset.py              # Metrics computation
└── README.md
```

---

## ⚡ Quick Start

```bash
# 1. Generate synthetic data (1,000 users × 30 days)
python generate_dataset.py

# 2. Clean and validate data
python clean_dataset.py

# 3. Compute daily metrics
python aggregate_dataset.py

# 4. Load data/user_engagement_metrics.csv into Power BI
```

---

## 🛠 Tech Stack

- Python, Pandas
- Power BI
- CSV-based ETL pipeline

---

## 📈 Dashboard Features

- **📉 Trend Analysis** – DAU and session patterns over time
- **📊 Engagement Metrics** – Average pages visited and time spent
- **🎯 Churn Tracking** – Daily retention indicators
- **🔍 Interactive Filters** – Date range slicers

---

## 💡 Key Features

✅ Complete ETL pipeline from raw data to insights  
✅ Reproducible workflow with modular scripts  
✅ Production-quality code structure  
✅ Easy to adapt for real business data  

---

⭐ **Star this repo if you found it helpful!**
