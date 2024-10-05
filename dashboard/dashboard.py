import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = "main_data.csv"

if not os.path.isfile(data_path):
    st.error("File not found. Please check the path.")
else:
    df = pd.read_csv(data_path)

st.title("Bike Usage Analysis Dashboard")
st.write("Welcome to the bike usage analysis dashboard!")
st.markdown("### Data Overview")
st.dataframe(df)
st.markdown("### Key Statistics")
st.write(df.describe())
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
filtered_df = df[
    (df['month'].isin(selected_month)) & 
    (df['weather'].isin(selected_weather)) & 
    (df['season'].isin(selected_season))
]
st.markdown("### Monthly Rentals Analysis")
st.write("1: January\n\n2: February\n\n3: March\n\n4: April\n\n5: May\n\n6: June\n\n7: July\n\n8: August\n\n9: September\n\n10: October\n\n11: November\n\n12: December")
monthly_rentals_avg = filtered_df.groupby('month')['total_rentals'].mean()
fig, ax = plt.subplots(figsize=(10, 5))
colors = sns.color_palette('husl', len(monthly_rentals_avg))
bars = monthly_rentals_avg.plot(kind='bar', color=colors, ax=ax)  
ax.set_title("Average Rentals by Month", fontsize=16)
ax.set_ylabel("Average Rentals", fontsize=12)
ax.set_xlabel("Month", fontsize=12)
ax.set_xticks(range(len(monthly_rentals_avg)))
ax.set_xticklabels(monthly_rentals_avg.index, rotation=45)
for bar in bars.patches:
    ax.annotate(f'{int(bar.get_height())}', 
                (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                ha='center', va='bottom')
st.pyplot(fig)
st.markdown("### Weather Impact on Rentals")
st.write("1: Clear, Few clouds, Partly cloudy\n\n2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist\n\n3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds\n\n4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog")
weather_conditions = {1: 1, 2: 2, 3: 3, 4: 4}
filtered_df['weather'] = filtered_df['weather'].map(weather_conditions)
weather_rentals = filtered_df.groupby('weather')['total_rentals'].mean().reindex(weather_conditions.values(), fill_value=0)
fig, ax = plt.subplots(figsize=(10, 5))
colors = sns.color_palette('coolwarm', len(weather_rentals))  
bars = weather_rentals.plot(kind='bar', color=colors, ax=ax)
ax.set_title("Average Rentals by Weather", fontsize=16)
ax.set_ylabel("Average Rentals", fontsize=12)
ax.set_xlabel("Weather Condition", fontsize=10)
plt.xticks(rotation=45)
for bar in bars.patches:
    ax.annotate(f'{int(bar.get_height())}', 
                (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                ha='center', va='bottom')
st.pyplot(fig)
st.markdown("### Seasonal Analysis")
st.write("1: Spring\n\n2: Summer\n\n3: Fall\n\n4: Winter")
seasonal_rentals = filtered_df.groupby('season')['total_rentals'].mean()
fig, ax = plt.subplots(figsize=(10, 5))
colors = sns.color_palette('Set3', len(seasonal_rentals))  
bars = seasonal_rentals.plot(kind='bar', color=colors, ax=ax)
ax.set_title("Average Rentals by Season", fontsize=16)
ax.set_ylabel("Average Rentals", fontsize=12)
ax.set_xlabel("Season", fontsize=10)
plt.xticks(rotation=0)
for bar in bars.patches:
    ax.annotate(f'{int(bar.get_height())}', 
                (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                ha='center', va='bottom')
st.pyplot(fig)