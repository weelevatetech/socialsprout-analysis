"""
Synthetic (illustrative) dataset for the SocialSprout case study — an Instagram
marketing agency based in Bangalore. Not real company data; built to demonstrate
ElevateTech's analysis workflow. Figures in INR.
"""
import numpy as np
import pandas as pd

np.random.seed(7)

months = pd.date_range("2025-09-01", periods=12, freq="MS").strftime("%b %Y")

# SocialSprout: steady client-base growth, festive-season (Oct-Nov) and New Year (Jan) spikes
base = np.array([4.2, 4.6, 5.8, 6.5, 5.1, 4.4, 4.9, 5.6, 6.2, 6.8, 7.4, 8.1]) * 100000
socialsprout_revenue = base + np.random.normal(0, 15000, size=12)

# Two Bangalore competitor agencies
competitor_a = (base * 1.9 + np.random.normal(0, 30000, 12))   # "ViralNest Media" — larger, established
competitor_b = (base * 0.6 + np.random.normal(20000, 18000, 12))  # "Boostly Creators" — smaller, budget-focused

revenue_df = pd.DataFrame({
    "month": months,
    "SocialSprout": socialsprout_revenue.round(0),
    "ViralNest Media": competitor_a.round(0),
    "Boostly Creators": competitor_b.round(0),
})
revenue_df.to_csv("data/monthly_revenue.csv", index=False)

# Service mix — share of last quarter's client billings
service_mix = pd.DataFrame({
    "service": ["Reels Production", "Influencer Collabs", "Paid Ad Management", "Content Strategy", "Community Management"],
    "share_pct": [34, 27, 21, 11, 7],
})
service_mix.to_csv("data/service_mix.csv", index=False)

# Client acquisition efficiency: ad/outreach spend vs avg monthly revenue
efficiency = pd.DataFrame({
    "business": ["SocialSprout", "ViralNest Media", "Boostly Creators"],
    "monthly_acquisition_spend": [45000, 160000, 22000],
    "avg_monthly_revenue": [revenue_df["SocialSprout"].mean(),
                             revenue_df["ViralNest Media"].mean(),
                             revenue_df["Boostly Creators"].mean()],
})
efficiency["revenue_per_rupee"] = (efficiency["avg_monthly_revenue"] / efficiency["monthly_acquisition_spend"]).round(2)
efficiency.to_csv("data/acquisition_efficiency.csv", index=False)

# Client retention / churn snapshot — active clients per month
active_clients = np.array([14, 15, 17, 19, 18, 17, 18, 20, 22, 24, 26, 29])
retention_df = pd.DataFrame({"month": months, "active_clients": active_clients})
retention_df.to_csv("data/active_clients.csv", index=False)

print(revenue_df)
print()
print(service_mix)
print()
print(efficiency)
print()
print(retention_df)
