import pandas as pd
import streamlit as st
import plotly.express as px

# Load the merged basketball data
merged_df = pd.read_csv('merged_basketball_data.csv')

# Convert 'Unnamed: 2_level_0' to integer
merged_df['Unnamed: 2_level_0'] = pd.to_numeric(merged_df['Unnamed: 2_level_0'], errors='coerce')

# Convert 'Per Game' to numeric
merged_df['Per Game'] = pd.to_numeric(merged_df['Per Game'], errors='coerce')

# Convert 'Shooting' to numeric
merged_df['Shooting'] = pd.to_numeric(merged_df['Shooting'], errors='coerce')

# Set the app title
st.title('Basketball Statistics for the Atlanta Hawks')

# Scatter plot for Points Per Game with a year range slider
st.header('Points Per Game Over the Years')

# Dropdown for selecting a range of years
year_range_points = st.slider('Select Year Range for Points Per Game',
                              min_value=int(merged_df['Unnamed: 2_level_0'].min()),
                              max_value=int(merged_df['Unnamed: 2_level_0'].max()), value=(2010, 2020))

# Filter data based on the selected year range
filtered_df_points = merged_df[(merged_df['Unnamed: 2_level_0'] >= year_range_points[0]) & 
                                (merged_df['Unnamed: 2_level_0'] <= year_range_points[1])]

# Scatter plot for Points Per Game
fig_points_per_game = px.scatter(filtered_df_points, x='Unnamed: 2_level_0', y='Per Game',
                                 labels={'Per Game': 'Points Per Game'}, title='Points Per Game Over the Years',
                                 color='Per Game', size='Per Game', opacity=0.7)
fig_points_per_game.update_layout(hovermode='closest')  # Enable hover for tooltips
fig_points_per_game.update_traces(hovertemplate='Year: %{x}<br>Points Per Game: %{y:.2f}')

# Description for the Points Per Game chart
st.write("This scatter plot displays the points per game for the selected player over the selected range of years. "
         "Use the hover functionality to see detailed information for each data point.")
st.plotly_chart(fig_points_per_game, use_container_width=True)

# Bar chart for Shooting Percentage by Position with position selection
st.header('Shooting Percentage by Position')

# Sidebar: Position Selection
selected_position_1 = st.selectbox('Select Position 1', merged_df['position'].unique(), index=0)
selected_position_2 = st.selectbox('Select Position 2', merged_df['position'].unique(), index=1)

# Filter data based on the selected positions
filtered_df_positions = merged_df[(merged_df['position'] == selected_position_1) | (merged_df['position'] == selected_position_2)]

# Bar chart for Shooting Percentage by Position
fig_shooting_percentage = px.bar(filtered_df_positions, x='position', y='Shooting', color='position',
                                  labels={'y': 'Shooting Percentage'}, title='Shooting Percentage by Position')
fig_shooting_percentage.update_layout(hovermode='closest')  # Enable hover for tooltips
fig_shooting_percentage.update_traces(hovertemplate='Position: %{x}<br>Shooting Percentage: %{y:.2f}')

# Set y-axis limits
fig_shooting_percentage.update_yaxes(range=[0, 60], dtick=5)

# Description for the Shooting Percentage by Position chart
st.write("This bar chart displays the shooting percentage for the selected positions. "
         "Use the hover functionality to see detailed information for each bar.")
st.plotly_chart(fig_shooting_percentage, use_container_width=True)


