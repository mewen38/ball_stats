import sqlite3

ball_stats_conn = sqlite3.connect('ball_stats_database.db')
cursor = ball_stats_conn.cursor()
print("goliath online")

avg_query = """SELECT AVG(davis_score), AVG(crank_score), AVG(mike_score) FROM fact_games;"""
cursor.execute(avg_query)
print(cursor.fetchall())