# 🚖 Uber Trip Analysis (April – September 2014)

This project analyzes six months of Uber pickup data in New York City using data science techniques. It focuses on identifying travel patterns, uncovering peak demand hours, and building predictive models to forecast ride volume — offering insights valuable for operations, city planning, and urban mobility optimization.

---

## 📌 Project Objectives

- Understand temporal trends in Uber pickups (hourly, daily, monthly)
- Identify peak hours, busiest weekdays, and top-performing Uber bases
- Visualize trip density across time and geography
- Build machine learning models to predict future ride demand
- Provide actionable insights for transportation planning

---

## 📁 Dataset Overview

- **Source:** [FiveThirtyEight GitHub](https://github.com/fivethirtyeight/uber-tlc-foil-response)
- **Period Covered:** April 1, 2014 – September 30, 2014
- **Data Points:** 4.53 million+
- **Columns:**
  - `Date/Time` – Timestamp of the pickup
  - `Lat`, `Lon` – Pickup location
  - `Base` – Affiliated Uber partner base

---

## ⚙️ Technologies Used

- **Language:** Python
- **Notebook:** Jupyter
- **Libraries:** 
  - `pandas`, `numpy` – Data manipulation
  - `matplotlib`, `seaborn`, `plotly` – Visualization
  - `scikit-learn`, `xgboost` – Machine Learning
  - `pyxlsb` – For handling `.xlsb` binary Excel data

---

## 🧼 Data Preprocessing

- Merged `.xlsb` files from six months
- Converted Excel serial dates to datetime
- Extracted features: `Hour`, `Weekday`, `Month`, `Date`
- Ensured no missing or corrupt values
- Sorted chronologically and prepared for EDA

---

## 📊 Exploratory Data Analysis (EDA)

- **Trips per Hour:** Peak between **5 PM–7 PM**, aligning with evening commute
- **Trips per Weekday:** **Friday and Saturday** are the busiest
- **Monthly Trends:** Gradual increase in ride volume, with **September** peaking
- **Heatmaps:** Reveal weekday rush hour vs. weekend night surges
- **Base Analysis:** B02617 and B02598 handled the majority of trips
- **Geographic Visualization:** High density in Manhattan, lower in outer boroughs

---

## 🧠 Feature Engineering

- Created time-based features (`Hour`, `Day`, `Month`, etc.)
- Aggregated metrics for grouped analysis
- Flagged `RushHour`, `IsWeekend` for pattern segmentation
- Spatial potential: Latitude/Longitude for zone clustering (future)

---

## 🤖 Machine Learning Models

| Model                     | MAE     | RMSE     | R² Score |
|--------------------------|---------|----------|----------|
| Random Forest Regressor  | ~127.91 | ~33774.6 | ~0.92    |
| Gradient Boosting        | ~124.59 | ~30091.5 | ~0.9343  |
| XGBoost Regressor        | ~105.30 | ~162.5   | ~0.92    |

- **Best Model:** XGBoost gave the most accurate results with excellent generalization.

---

## 🧬 Ensemble Models

- **Voting Regressor:** Averaged predictions for a slight boost in accuracy
- **Stacking Regressor:** Combined models with a meta-learner (Linear Regression), achieving:
  - **MAE:** ~100.2
  - **R²:** ~0.935

---

## 🔍 Key Insights

- **Busiest Hours:** 5 PM to 7 PM due to evening commute and social travel
- **Most Active Days:** Friday and Saturday, driven by nightlife and events
- **Peak Month:** September, reflecting adoption growth and post-summer routines
- **Base Dominance:** A few Uber bases handled a majority of trip volume

---

## 🚀 Future Scope

- Incorporate drop-off data for full trip analysis
- Add external factors like weather, traffic, and events
- Apply time series forecasting (Prophet, ARIMA, LSTM)
- Build real-time dashboards using Streamlit or Dash
- Extend to other cities or platforms (e.g., Lyft, Ola)

---

## 📂 Folder Structure

