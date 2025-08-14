# BTC/USD SMA Crossover Strategy – Algorithmic Trading with Python

# 📌 Overview
This project implements and backtests a **Simple Moving Average (SMA) Crossover Strategy** for BTC/USD to capture trend-following opportunities in cryptocurrency markets.  
The strategy uses:
- **10-day SMA (fast)**  
- **50-day SMA (slow)**  

When the fast SMA crosses above the slow SMA → **Long Entry**  
When the fast SMA crosses below the slow SMA → **Close Position**  

The system avoids lookahead bias, ensures reproducibility, and generates key trading metrics and performance visualizations.

---

# 🚀 Features
- End-to-end pipeline for backtesting:
  - Data preprocessing with **Pandas**
  - SMA computation with **TA library**
  - Trade execution logic
  - Backtesting with custom `BackTester` class
  - Performance metrics & visualization with **Matplotlib**
- Robust check for **lookahead bias**
- PnL and trade history export to CSV

---

# 📊 Key Results (2019–2023 Data)
- **Total Return:** 343.10%  
- **Net Profit:** $3,431.03  
- **Sharpe Ratio:** 5.25  
- **Win Rate:** 56.25%  
- **Max Drawdown:** 37.37%  
- **Total Trades:** 16 (all long trades)  
- **Average Holding Time:** ~44 days  

✅ No lookahead bias detected.  
✅ Strong performance during trending markets.

---

# 📂 Project Structure

main.py (# Main strategy and backtest runner)
Project Report.pdf (# Full project report)
Project Report.rtf (# Alternative project report format)
Project_files/ (# Supporting files/resources)
BTC_2019_2023_1d.csv (# Historical BTC/USD dataset (daily))
