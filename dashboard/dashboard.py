<<<<<<< HEAD
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
=======
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from main_data.csv
data_path = "main_data.csv"  # Ganti dengan path yang benar
df = pd.read_csv(data_path)

# Streamlit Dashboard
st.title("Bike Usage Analysis Dashboard")
st.write("Welcome to the bike usage analysis dashboard!")

# Data Overview
st.markdown("### Data Overview")
st.dataframe(df)  # Tampilkan keseluruhan dataset dalam dataframe yang dapat digulir

st.markdown("### Key Statistics")
st.write(df.describe())  # Tampilkan statistik kunci dari dataset

# Filter Data
st.sidebar.header("Filter Data")
selected_month = st.sidebar.multiselect(
    "Select Month", 
    df['month'].unique().tolist(), 
    default=df['month'].unique().tolist()
)

selected_weather = st.sidebar.multiselect(
    "Select Weather", 
    df['weather'].unique().tolist(), 
    default=df['weather'].unique().tolist()
)

selected_season = st.sidebar.multiselect(
    "Select Season", 
    df['season'].unique().tolist(), 
    default=df['season'].unique().tolist()
)

# Filter the DataFrame based on user input
filtered_df = df[
    (df['month'].isin(selected_month)) & 
    (df['weather'].isin(selected_weather)) & 
    (df['season'].isin(selected_season))
]

# Monthly Rentals Analysis
st.markdown("### Monthly Rentals Analysis")
st.write("1: January\n\n2: February\n\n3: March\n\n4: April\n\n5: May\n\n6: June\n\n7: July\n\n8: August\n\n9: September\n\n10: October\n\n11: November\n\n12: December")

# Hitung rata-rata total rental per bulan
monthly_rentals_avg = filtered_df.groupby('month')['total_rentals'].mean()  # Rata-rata total rentals per bulan

# Bar plot dengan warna berbeda untuk setiap bulan
fig, ax = plt.subplots(figsize=(10, 5))
colors = sns.color_palette('husl', len(monthly_rentals_avg))  # Menggunakan palet warna "husl" untuk variasi warna
bars = monthly_rentals_avg.plot(kind='bar', color=colors, ax=ax)  # Warna beragam
ax.set_title("Average Rentals by Month", fontsize=16)
ax.set_ylabel("Average Rentals", fontsize=12)
ax.set_xlabel("Month", fontsize=12)
ax.set_xticks(range(len(monthly_rentals_avg)))
ax.set_xticklabels(monthly_rentals_avg.index, rotation=45)

# Menambahkan label data di atas batang
for bar in bars.patches:
    ax.annotate(f'{int(bar.get_height())}', 
                (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                ha='center', va='bottom')

st.pyplot(fig)

# Weather Impact Analysis
st.markdown("### Weather Impact on Rentals")
st.write("1: Clear, Few clouds, Partly cloudy\n\n2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist\n\n3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds\n\n4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog")

# Ensure that weather condition 4 is included even if no data exists for it
weather_conditions = {1: 1, 2: 2, 3: 3, 4: 4}
filtered_df['weather'] = filtered_df['weather'].map(weather_conditions)

# Include all possible weather conditions in the grouping
weather_rentals = filtered_df.groupby('weather')['total_rentals'].mean().reindex(weather_conditions.values(), fill_value=0)

# Bar plot dengan warna berbeda untuk setiap kondisi cuaca
fig, ax = plt.subplots(figsize=(10, 5))
colors = sns.color_palette('coolwarm', len(weather_rentals))  # Palet warna untuk variasi
bars = weather_rentals.plot(kind='bar', color=colors, ax=ax)
ax.set_title("Average Rentals by Weather", fontsize=16)
ax.set_ylabel("Average Rentals", fontsize=12)
ax.set_xlabel("Weather Condition", fontsize=10)
plt.xticks(rotation=45)

# Menambahkan label data di atas batang
for bar in bars.patches:
    ax.annotate(f'{int(bar.get_height())}', 
                (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                ha='center', va='bottom')

st.pyplot(fig)

# Seasonal Analysis
st.markdown("### Seasonal Analysis")
st.write("1: Spring\n\n2: Summer\n\n3: Fall\n\n4: Winter")

# Seasonal Rentals Analysis
seasonal_rentals = filtered_df.groupby('season')['total_rentals'].mean()

# Bar plot dengan warna berbeda untuk setiap musim
fig, ax = plt.subplots(figsize=(10, 5))
colors = sns.color_palette('Set3', len(seasonal_rentals))  # Menggunakan palet warna "Set3"
bars = seasonal_rentals.plot(kind='bar', color=colors, ax=ax)
ax.set_title("Average Rentals by Season", fontsize=16)
ax.set_ylabel("Average Rentals", fontsize=12)
ax.set_xlabel("Season", fontsize=10)
plt.xticks(rotation=0)

# Menambahkan label data di atas batang
for bar in bars.patches:
    ax.annotate(f'{int(bar.get_height())}', 
                (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                ha='center', va='bottom')

st.pyplot(fig)
>>>>>>> b010cce (revisi submission notebook.ipynb, requirements.txt, dan dashboard.py)
