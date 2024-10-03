import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title for the dashboard
st.title("Bike Usage Analysis Dashboard")
st.write("Welcome to the bike usage analysis dashboard!")

# Sidebar filters
st.sidebar.header("Filter Data")
month_filter = st.sidebar.multiselect(
    "Select Month for Analysis", 
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 
    default=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
)

location_filter = st.sidebar.multiselect(
    "Select Location", 
    ['Station A', 'Station B', 'Station C', 'Station D'], 
    default=['Station A', 'Station B', 'Station C', 'Station D']
)

# Seasonal Analysis Data
df_filtered = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Usage': [500, 450, 480, 550, 600, 700, 750, 800, 780, 760, 730, 690]
})

# Supply vs Demand Data
df_supply_demand = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Bikes Available': [600, 550, 570, 620, 700, 800, 850, 900, 880, 860, 840, 800],
    'Bikes Rented': [500, 450, 480, 550, 600, 700, 750, 800, 780, 760, 730, 690]
})

# Time of Day Usage Data
df_time_usage = pd.DataFrame({
    'Hour': list(range(24)),
    'Usage': [50, 20, 10, 5, 3, 5, 15, 40, 80, 100, 120, 130, 140, 160, 150, 140, 130, 110, 100, 90, 80, 60, 40, 30]
})

# Location-based Data
df_location_usage = pd.DataFrame({
    'Location': ['Station A', 'Station B', 'Station C', 'Station D'],
    'Usage': [500, 300, 700, 200]
})

# Performance Data
df_performance = pd.DataFrame({
    'Bike ID': ['Bike 1', 'Bike 2', 'Bike 3', 'Bike 4'],
    'Total Rides': [100, 150, 80, 120],
    'Avg Duration (min)': [30, 35, 25, 40]
})

# Vertical Layout (Card-Based)
st.subheader("Analysis Overview")

# Card 1: Seasonal Analysis
st.markdown("### Seasonal Analysis: Monthly Bike Usage")
fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=df_filtered[df_filtered['Month'].isin(month_filter)], x='Month', y='Usage', marker="o", ax=ax)
ax.set_title("Bike Usage by Month")
ax.set_ylabel("Number of Bikes Used")
ax.set_xlabel("Month")

#  text labels untuk the line chart
for i, usage in enumerate(df_filtered['Usage']):
    ax.text(i, usage, str(usage), ha='center', va='bottom')

st.pyplot(fig)

# Card 2: Supply vs Demand Analysis
st.markdown("### Supply vs Demand Analysis")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df_supply_demand['Month'], df_supply_demand['Bikes Available'], label="Bikes Available", marker="o")
ax.plot(df_supply_demand['Month'], df_supply_demand['Bikes Rented'], label="Bikes Rented", marker="o")
ax.set_title("Supply vs Demand")
ax.set_ylabel("Number of Bikes")
ax.set_xlabel("Month")

#  text labels untuk Bikes Available dan Bikes Rented
for i, val in enumerate(df_supply_demand['Bikes Available']):
    ax.text(i, val, str(val), ha='center', va='bottom')

for i, val in enumerate(df_supply_demand['Bikes Rented']):
    ax.text(i, val, str(val), ha='center', va='bottom')

ax.legend()
st.pyplot(fig)

# Card 3: Time of Day Usage
st.markdown("### Time of Day Bike Usage")
fig, ax = plt.subplots(figsize=(10, 4))
sns.barplot(x='Hour', y='Usage', data=df_time_usage, palette='Paired', ax=ax)
ax.set_title("Bike Usage by Time of Day")
ax.set_ylabel("Number of Bikes Used")
ax.set_xlabel("Hour of Day")

#  text labels untuk the bar chart
for i, usage in enumerate(df_time_usage['Usage']):
    ax.text(i, usage, str(usage), ha='center', va='bottom')

st.pyplot(fig)

# Card 4: Location-based Analysis
st.markdown("### Location-based Analysis")
fig, ax = plt.subplots(figsize=(10, 4))
sns.barplot(x='Location', y='Usage', data=df_location_usage[df_location_usage['Location'].isin(location_filter)], palette='Set2', ax=ax)
ax.set_title("Bike Usage by Location")
ax.set_ylabel("Number of Bikes Used")
ax.set_xlabel("Location")

# text labels untuk the bar chart
for i, usage in enumerate(df_location_usage['Usage']):
    ax.text(i, usage, str(usage), ha='center', va='bottom')

st.pyplot(fig)

# Card 5: Performance Analysis
st.markdown("### Performance Analysis")
st.write(df_performance)

# Sidebar information
st.sidebar.markdown("### Gunakan filter untuk mempersempit analisis.")
st.sidebar.markdown("Anda dapat memilih bulan atau lokasi tertentu untuk menyesuaikan visualisasi.")
