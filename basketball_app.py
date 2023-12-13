import pandas as pd
import streamlit as st
import plotly.express as px

# Load the merged basketball data
merged_df = pd.read_csv('merged_basketball_data.csv')

# Main content
st.title('Basketball Player Statistics')

# Line chart for Points Per Game with a year range slider
st.header('Points Per Game Over the Years')

# Dropdown for selecting a range of years
year_range_points = st.slider('Select Year Range for Points Per Game',
                              min_value=int(merged_df['Unnamed: 2_level_0'].min()),
                              max_value=int(merged_df['Unnamed: 2_level_0'].max()), value=(2010, 2020))

# Filter data based on the selected year range
filtered_df_points = merged_df[(merged_df['Unnamed: 2_level_0'] >= year_range_points[0]) & 
                                (merged_df['Unnamed: 2_level_0'] <= year_range_points[1])]

# Line chart for Points Per Game
fig_points_per_game = px.line(filtered_df_points, x='Unnamed: 2_level_0', y='Per Game',
                              labels={'Per Game': 'Points Per Game'}, title='Points Per Game Over the Years',
                              line_group='Per Game')
fig_points_per_game.add_scatter(x=filtered_df_points['Unnamed: 2_level_0'], y=filtered_df_points['Per Game.1'],
                                mode='lines', name='Other Points', line=dict(dash='dash'))

fig_points_per_game.update_layout(hovermode='closest')  # Enable hover for tooltips
fig_points_per_game.update_traces(hovertemplate='Year: %{x}<br>Points Per Game: %{y:.2f}')

# Description for the Points Per Game chart
st.write("This line chart displays the points per game for the selected player over the selected range of years. "
         "Use the hover functionality to see detailed information for each data point.")
st.plotly_chart(fig_points_per_game, use_container_width=True)

# Shooting Percentage Bar Chart with a position dropdown
st.header('Top 5 Positions and Shooting Percentages')

# Dropdown for selecting a position
selected_position_shooting = st.selectbox('Select Position for Shooting Percentages',
                                          merged_df['position'].unique())

# Filter data based on the selected position
filtered_df_shooting = merged_df[merged_df['position'] == selected_position_shooting]

# Bar chart for Top 5 Positions and Shooting Percentages
top_positions_shooting = filtered_df_shooting.groupby('position')['Shooting.1'].mean().nlargest(5).reset_index()
fig_top_positions_shooting = px.bar(top_positions_shooting, x='position', y='Shooting.1',
                                    labels={'y': 'Shooting Percentage'}, title='Top 5 Positions and Shooting Percentages')
fig_top_positions_shooting.update_layout(hovermode='closest')  # Enable hover for tooltips
fig_top_positions_shooting.update_traces(hovertemplate='Position: %{x}<br>Shooting Percentage: %{y:.2f}')

# Description for the Shooting Percentage Bar Chart
st.write("This bar chart displays the average shooting percentage for the top 5 positions played by the selected player "
         "over the entire dataset. Use the hover functionality to see detailed information for each bar.")
st.plotly_chart(fig_top_positions_shooting, use_container_width=True)

# Add your third graph with a different interactive element and description here...



