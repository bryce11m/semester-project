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
fig_points_per_game = px.line(player_df, x='Unnamed: 2_level_0', y=('Per Game', 'Per Game.1'), 
                              labels={'y': 'Points Per Game'}, title='Points Per Game Over the Years')
fig_points_per_game.update_layout(hovermode='closest')  # Enable hover for tooltips
fig_points_per_game.update_traces(hovertemplate='Year: %{x}<br>Points Per Game: %{y:.2f}')

st.plotly_chart(fig_points_per_game, use_container_width=True)

# Bar chart for Top 5 Positions and Shooting Percentages
top_positions = player_df.groupby('position')['Shooting.1'].mean().nlargest(5).reset_index()
fig_top_positions = px.bar(top_positions, x='position', y='Shooting.1',
                           labels={'y': 'Shooting Percentage'}, title='Top 5 Positions and Shooting Percentages')
fig_top_positions.update_layout(hovermode='closest')  # Enable hover for tooltips
fig_top_positions.update_traces(hovertemplate='Position: %{x}<br>Shooting Percentage: %{y:.2f}')

st.plotly_chart(fig_top_positions, use_container_width=True)
