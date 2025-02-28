---
title: "Tecno Pocket Go: Bass Diffusion Analysis"
author: "Your Name"
date: "YYYY-MM-DD"
---

# Introduction

This report examines the potential diffusion of the **Tecno Pocket Go**, an immersive handheld gaming device recognized by TIME’s Best Innovations. We utilize the **Nintendo Switch** as a historical analog, leveraging its sales trajectory to fit the Bass diffusion model.

## 1. Background & Motivation

- **Tecno Pocket Go**: [Link to TIME Best Innovations page].
- **Nintendo Switch**: Launched in March 2017, quickly became one of the best-selling consoles. Perfect comparative case for analyzing handheld console adoption.

## 2. Data Collection

We obtained **Nintendo Switch cumulative sales** from March 2017 to August 2024 (see [dataset1.csv](../data/dataset1.csv)). The data is in millions of units sold worldwide.

| Date     | Cumulative Sales (mil) |
|----------|-------------------------|
| 2017-03  | 1.50                   |
| 2017-09  | 7.63                   |
| ...      | ...                    |
| 2024-08  | 143.42                 |

## 3. Bass Model Overview

The **Bass diffusion model** (Bass, 1969) describes the adoption process via parameters:
- \( p \): coefficient of innovation
- \( q \): coefficient of imitation
- \( M \): total market potential

In **continuous** form for cumulative adoption \( S(t) \):

\[
S(t) = M \frac{1 - e^{-(p+q)\,t}}{1 + \left(\frac{q}{p}\right) e^{-(p+q)\,t}}.
\]

## 4. Parameter Estimation

We used **Python** (`script2.py`) to perform non-linear regression on the cumulative Switch data. Below are the steps:

1. Converted date to a numeric time index \( t = 1, 2, 3, \ldots \)
2. Applied `scipy.optimize.curve_fit` to fit \((p, q, M)\).

### 4.1 Results

- Estimated **p**: 0.02 (example)
- Estimated **q**: 0.40 (example)
- Estimated **M**: 150 million (example)

*(Note: Use the actual estimates from your regression.)*

A plot comparing **actual** vs. **fitted** Nintendo Switch sales is shown below:

![Nintendo Switch Bass Fit](../img/image1.png)

## 5. Predicting Tecno Pocket Go Diffusion

### 5.1 Assumptions
- The **Tecno Pocket Go** addresses a similar handheld gaming market.
- Slightly reduced brand recognition => keep \( p \) ~ 0.018, \( q \) ~ 0.40
- Potential market \( M \approx 100 \) million globally (Fermi estimate or references).

### 5.2 Forecast
Using these parameters in the Bass formula, we estimate:

See: [product_forecast.csv](../data/product_forecast.csv)

## 6. Conclusion

- Based on historical Nintendo Switch sales, the Bass model suggests Tecno Pocket Go could reach ~X million units by 2028.
- Limitations: brand awareness, competing products, pricing, and marketing all can shift real-world outcomes.

## References

1. Bass, F. M. (1969). *A new product growth for model consumer durables*. Management Science, 15(5), 215–227.
2. TIME (2024). *Tecno Pocket Go*. [Link]
3. Statista. (2023). *Global Nintendo Switch Sales Dataset*. [Link]
4. [Any additional references or PDFs used]

