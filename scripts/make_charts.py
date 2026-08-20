import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

BG = "#0B0F14"
TEAL = "#4FD1C5"
AMBER = "#E8A33D"
GREY = "#8194A6"
TEXT = "#E8EDF2"

plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": TEXT, "axes.labelcolor": TEXT,
    "xtick.color": GREY, "ytick.color": GREY,
    "axes.edgecolor": "#232E3D", "font.size": 11, "font.family": "sans-serif",
})

def inr(x, pos):
    if x >= 1e5:
        return f"₹{x/1e5:.1f}L"
    return f"₹{int(x):,}"

revenue = pd.read_csv("data/monthly_revenue.csv")
service_mix = pd.read_csv("data/service_mix.csv")
efficiency = pd.read_csv("data/acquisition_efficiency.csv")
retention = pd.read_csv("data/active_clients.csv")

# 1. Revenue trend
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(revenue["month"], revenue["SocialSprout"], color=TEAL, linewidth=2.5, marker="o", markersize=4, label="SocialSprout")
ax.plot(revenue["month"], revenue["ViralNest Media"], color=AMBER, linewidth=2, marker="o", markersize=3, label="ViralNest Media (established)")
ax.plot(revenue["month"], revenue["Boostly Creators"], color=GREY, linewidth=2, marker="o", markersize=3, label="Boostly Creators (budget)")
ax.set_title("Monthly Revenue — 12-Month Trend", color=TEXT, fontsize=13, fontweight="bold", loc="left")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(inr))
ax.tick_params(axis="x", rotation=45)
ax.legend(frameon=False, loc="upper left")
ax.grid(axis="y", color="#1A2330", linewidth=0.7)
for s in ["top", "right"]: ax.spines[s].set_visible(False)
plt.tight_layout()
plt.savefig("charts/revenue_trend.png", dpi=150)
plt.close()

# 2. Market share
avg_rev = revenue[["SocialSprout", "ViralNest Media", "Boostly Creators"]].mean()
fig, ax = plt.subplots(figsize=(6, 5))
wedges, texts, autotexts = ax.pie(
    avg_rev, labels=avg_rev.index, autopct="%1.0f%%", colors=[TEAL, AMBER, GREY],
    wedgeprops={"edgecolor": BG, "linewidth": 2}, textprops={"color": TEXT}
)
for at in autotexts: at.set_color(BG); at.set_fontweight("bold")
ax.set_title("Estimated Bangalore Market Share\n(by avg. monthly revenue)", color=TEXT, fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("charts/market_share.png", dpi=150)
plt.close()

# 3. Service mix
fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.barh(service_mix["service"], service_mix["share_pct"], color=[TEAL, "#7FDBD1", AMBER, "#B8C4D0", GREY])
ax.set_title("SocialSprout Service Mix — Last Quarter", color=TEXT, fontsize=13, fontweight="bold", loc="left")
ax.set_xlabel("Share of client billings (%)")
ax.invert_yaxis()
for s in ["top", "right"]: ax.spines[s].set_visible(False)
for bar, val in zip(bars, service_mix["share_pct"]):
    ax.text(val + 1, bar.get_y() + bar.get_height()/2, f"{val}%", va="center", color=TEXT, fontsize=10)
plt.tight_layout()
plt.savefig("charts/service_mix.png", dpi=150)
plt.close()

# 4. Acquisition efficiency
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(efficiency["business"], efficiency["revenue_per_rupee"], color=[TEAL, AMBER, GREY])
ax.set_title("Revenue Generated per ₹1 of Acquisition Spend", color=TEXT, fontsize=13, fontweight="bold", loc="left")
ax.set_ylabel("₹ revenue per ₹1 spent")
for s in ["top", "right"]: ax.spines[s].set_visible(False)
for bar, val in zip(bars, efficiency["revenue_per_rupee"]):
    ax.text(bar.get_x() + bar.get_width()/2, val + 0.3, f"₹{val}", ha="center", color=TEXT, fontsize=10, fontweight="bold")
plt.tight_layout()
plt.savefig("charts/acquisition_efficiency.png", dpi=150)
plt.close()

# 5. Active clients trend
fig, ax = plt.subplots(figsize=(9, 4))
ax.bar(retention["month"], retention["active_clients"], color=TEAL)
ax.set_title("Active Clients — 12-Month Trend", color=TEXT, fontsize=13, fontweight="bold", loc="left")
ax.set_ylabel("Active clients")
ax.tick_params(axis="x", rotation=45)
for s in ["top", "right"]: ax.spines[s].set_visible(False)
plt.tight_layout()
plt.savefig("charts/active_clients.png", dpi=150)
plt.close()

print("Charts saved.")
