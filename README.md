# Analyzing-Amazon-Sales-data


**Project:** Analyzing Amazon Sales Data

**Author:** Jumana Haseen

**Date:** 2025

---

## Project Overview

This project performs an end-to-end analysis of Amazon sales data to uncover monthly, yearly and month-year trends. The goal is to extract actionable insights for sales management, forecasting, inventory planning, and marketing strategies.

## Problem Statement

Sales management is crucial in a competitive e‑commerce landscape. The objective of this project is to perform ETL (Extract, Transform, Load) on an Amazon sales dataset and produce insights on:

* Month-wise sales trends
* Year-wise sales trends
* Month-Year (yearly-month-wise) trends

These insights help identify peak seasons, low periods, and recurring patterns to improve decision-making.

## Objectives

1. Identify seasonal patterns (month-wise and month-year-wise).
2. Measure year-over-year growth and long-term trends.
3. Discover customer purchasing behaviour patterns (if customer-level data is present).
4. Provide visualizations and recommendations for inventory and marketing.

## Tech Stack

* Python 3.8+
* Pandas, NumPy
* Matplotlib / Plotly / Altair
* Jupyter Notebook or Google Colab
* SQL (for aggregated queries)



## Installation

1. Clone the repo:

```bash
git clone <repo-url>
cd amazon-sales-analysis
```

2. Create virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Open the Jupyter Notebook for exploratory analysis:

```bash
jupyter notebook notebooks/01-exploration.ipynb
```



## Dataset

Place your dataset CSV(s) in `data/raw/`. Typical columns used in this analysis:

* `order_id`
* `order_date` (YYYY-MM-DD)
* `product_id` / `product_category`
* `price` / `sales_amount`
* `quantity`
* `customer_id` (optional)
* `country` / `region` (optional)

> If dataset column names differ, update the cleaning script to map columns.


## Analysis & Visualizations

Key visualizations you should include:

* **Monthly sales line chart** (time-series) – shows peaks and troughs.
* **Year-over-year bar chart** – compare annual totals.
* **Month-Year heatmap** – months on one axis and years on the other to show recurring seasonal patterns.
* **Top product categories** – bar chart of highest revenue categories.
* **Sales by region** (if geographic data available) – choropleth or bar chart.



## Recommendations

* **Inventory planning:** increase stock before peak months and reduce for low-demand months.
* **Marketing:** run promotions and email campaigns ahead of peak months.
* **Pricing & Discounts:** evaluate discount impact by comparing revenue vs units sold during sale events.

## Future Work

* Add demand forecasting (ARIMA / Prophet / LSTM) for better planning.
* Build an interactive dashboard (Streamlit / Dash / Tableau) for stakeholders.
* Deeper customer segmentation using clustering (RFM analysis).

*This README is a template. I can tailor it to your exact dataset and code (add code snippets, screenshots, or dashboard link). Do you want me to add a short `requirements.txt` and a ready-to-run `etl.py` script?*
