# Immersive Gaming Innovation: Bass Diffusion Analysis

This repository contains the project files for analyzing the diffusion of the **Tecno Pocket Go** (a handheld gaming device) using the **Bass Diffusion Model**. We compare it to historical sales data from the **Nintendo Switch**, serving as our look-alike innovation.

## 1. Overview of Project

- **Goal**: Estimate Bass Model parameters (p, q, M) from Nintendo Switch sales data (2017–2024), then predict future adoption for the Tecno Pocket Go.
- **Why the Nintendo Switch?** It revolutionized handheld gaming, offering an analogous path for Tecno Pocket Go.

## 2. Contents

- `data/dataset1.csv`: Original (cumulative) Nintendo Switch sales data (2017–2024).
- `data/dataset1_cleaned.csv`: Cleaned version of the original dataset.
- `data/nintendo_switch_sales_yearly.csv`: End-of-year data extracted from the cleaned dataset.
- `data/product_forecast.csv`: Forecast output for the Tecno Pocket Go.
- `img/`: Images used in the analysis (e.g., plots of Switch data and Bass fit).
- `report/`: Contains `report_source.md` (the Markdown with our analysis) and potentially `report.pdf`.
- `script1.py`: Python script for data loading and cleaning.
- `script2.py`: Python script for Bass Model fitting and predictions.
- `helper_functions.py`: Shared functions (e.g., the Bass equation).
- `readme.md`: This documentation file.
