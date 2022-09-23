import sqlite3

ball_stats_conn = sqlite3.connect('ball_stats_database.db')
cursor = ball_stats_conn.cursor()
print("goliath online")

print('input full query')
full_query_input = input()
full_query = f"""{full_query_input}"""
cursor.execute(full_query)
print(cursor.fetchall())