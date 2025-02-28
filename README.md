# Immersive Gaming Innovation: Bass Diffusion Analysis

This repository contains the project files for analyzing the diffusion of the **Tecno Pocket Go** (a handheld gaming device) using the **Bass Diffusion Model**. We compare it to historical sales data from the **Nintendo Switch**, serving as our look-alike innovation.

## 1. Overview of Project

- **Goal**: Estimate Bass Model parameters (p, q, M) from Nintendo Switch sales data (2017–2024), then predict future adoption for the Tecno Pocket Go.
- **Why the Nintendo Switch?** It revolutionized handheld gaming, offering an analogous path for Tecno Pocket Go.

## 2. Contents

- `data/dataset1.csv`: Historical (cumulative) Nintendo Switch global sales (in millions), from March 2017 to August 2024.
- `img/`: Images used in the analysis (plots, product images).
- `report/`: Contains `report_source.md` (the Markdown with our analysis) and the final `report.pdf`.
- `script1.py`: Python script for data loading and cleaning.
- `script2.py`: Python script for Bass Model fitting and predictions.
- `helper_functions.py`: Shared functions (e.g., for the Bass equation).
- `readme.md`: This documentation file.

