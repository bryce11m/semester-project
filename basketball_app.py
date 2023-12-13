import pandas as pd
import streamlit as st
import plotly.express as px

# Load the merged basketball data
merged_df = pd.read_csv('merged_basketball_data.csv')

# Sidebar: Player Selection
st.sidebar.title('Player Selection')
selected_player = st.sidebar.selectbox('Select a player', merged_df['player'].unique())

# Filter data for the selected player
player_df = merged_df[merged_df['player'] == selected_player]

# Main content
st.title('Basketball Player Statistics')
st.subheader(f'Statistics for {selected_player}')

# Line chart for Points Per Game
fig_points_per_game = px.line(player_df, x='Unnamed: 2_level_0', y='Per Game',
                              labels={'Per Game': 'Points Per Game'}, title='Points Per Game Over the Years',
                              line_group='Per Game')
fig_points_per_game.add_scatter(x=player_df['Unnamed: 2_level_0'], y=player_df['Per Game.1'],
                                mode='lines', name='Other Points', line=dict(dash='dash'))

fig_points_per_game.update_layout(hovermode='closest')  # Enable hover for tooltips
fig_points_per_game.update_traces(hovertemplate='Year: %{x}<br>Points Per Game: %{y:.2f}')

# Description for the Points Per Game chart
st.write("### Points Per Game Over the Years")
st.write("This line chart displays the points per game for the selected player over the years. "
         "Use the hover functionality to see detailed information for each data point.")
st.plotly_chart(fig_points_per_game, use_container_width=True)

# Shooting Percentage Bar Chart
player_df['Shooting.1'] = pd.to_numeric(player_df['Shooting.1'], errors='coerce')

# Bar chart for Top 5 Positions and Shooting Percentages
top_positions = player_df.groupby('position')['Shooting.1'].mean().nlargest(5).reset_index()
fig_top_positions = px.bar(top_positions, x='position', y='Shooting.1',
                           labels={'y': 'Shooting Percentage'}, title='Top 5 Positions and Shooting Percentages')
fig_top_positions.update_layout(hovermode='closest')  # Enable hover for tooltips
fig_top_positions.update_traces(hovertemplate='Position: %{x}<br>Shooting Percentage: %{y:.2f}')

# Description for the Shooting Percentage Bar Chart
st.write("### Top 5 Positions and Shooting Percentages")
st.write("This bar chart displays the average shooting percentage for the top 5 positions played by the selected player. "
         "Use the hover functionality to see detailed information for each bar.")
st.plotly_chart(fig_top_positions, use_container_width=True)

# Add your third graph with an interactive element and description here...

# You can continue adding more graphs with their descriptions.

