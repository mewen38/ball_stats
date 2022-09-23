import sqlite3

ball_stats_conn = sqlite3.connect('ball_stats_database.db')
cursor = ball_stats_conn.cursor()
print("goliath online")

print('input game_id to retrieve')
game_id = input()
select_query = f"""SELECT * FROM fact_games WHERE game_id = {game_id};"""
cursor.execute(select_query)
print(cursor.fetchall())