import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from PIL import Image

# Load the dataset
@st.cache_data

def load_data():
    path = r"C:\Users\sunil\Downloads\Uber Trip Analysis"
    files = [os.path.join(path, f) for f in os.listdir(path) if "uber-raw-data" in f]

        # Read and concatenate
    dfs = [pd.read_csv(file) for file in files]
    df = pd.concat(dfs, ignore_index=True)
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df['Hour'] = df['Date/Time'].dt.hour
    df['Day'] = df['Date/Time'].dt.day
    df['DayOfWeek'] = df['Date/Time'].dt.dayofweek
    df['Month'] = df['Date/Time'].dt.month
    df['Count'] = 1
    return df

df = load_data()

# Sidebar options
st.sidebar.title("🔍 Uber Trip Analysis")
model_choice = st.sidebar.selectbox("Select Prediction Model", ["Random Forest", "Gradient Boosting", "Decision Tree", "XGBoost"])

# Title and intro image
st.title("🚖 Uber Trip Demand Forecasting")
st.image("https://images.unsplash.com/photo-1561139892-109fa0e6f9b6", use_column_width=True)

# Exploratory charts
st.header("📈 Trip Demand Analysis")
st.plotly_chart(px.histogram(df, x="Hour", nbins=24, title="Trip Distribution by Hour"))
st.plotly_chart(px.histogram(df, x="DayOfWeek", nbins=7, title="Trip Distribution by Day of Week"))

# Aggregate data for prediction
df_hourly = df.set_index('Date/Time').resample('H').count()['Count'].reset_index()
df_hourly['Hour'] = df_hourly['Date/Time'].dt.hour
df_hourly['Day'] = df_hourly['Date/Time'].dt.day
df_hourly['DayOfWeek'] = df_hourly['Date/Time'].dt.dayofweek
df_hourly['Month'] = df_hourly['Date/Time'].dt.month

X = df_hourly[['Hour', 'Day', 'DayOfWeek', 'Month']]
y = df_hourly['Count']

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

# Train model
if model_choice == "Random Forest":
    model = RandomForestRegressor()
elif model_choice == "Gradient Boosting":
    model = GradientBoostingRegressor()
elif model_choice == "Decision Tree":
    model = DecisionTreeRegressor()
else:
    model = XGBRegressor(objective='reg:squarederror')

model.fit(X_train, y_train)
predictions = model.predict(X_test)
mape = mean_absolute_percentage_error(y_test, predictions)

# Display predictions
st.header("📊 Predictions vs Actual")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(y_test.values, label="Actual", color='blue')
ax.plot(predictions, label="Predicted", color='red')
ax.set_title("Predicted vs Actual Trip Counts")
ax.legend()
st.pyplot(fig)

st.success(f"Model Performance (MAPE): {mape:.2%}")

# Insights and best timings
st.header("💡 Travel Insights")
peak_hours = df['Hour'].value_counts().sort_values(ascending=False).head(3).index.tolist()
least_busy = df['Hour'].value_counts().sort_values(ascending=True).head(3).index.tolist()
st.markdown(f"**🚀 Best Hours to Book a Ride (Least Busy):** {least_busy}")
st.markdown(f"**🔥 Peak Hours (Avoid if Possible):** {peak_hours}")

# Footer
st.markdown("---")
st.markdown("Created by **Sunil Naik** | Powered by Streamlit, XGBoost, and Uber NYC Data")
