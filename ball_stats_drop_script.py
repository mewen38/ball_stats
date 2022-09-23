import sqlite3

ball_stats_conn = sqlite3.connect('ball_stats_database.db')
cursor = ball_stats_conn.cursor()
print("goliath online")

print("are you sure you want to drop fact_games? type 'drop fact_games'")
answer = input()

if answer == 'drop fact_games':
    # # drop_table code
    drop_table_query = """DROP TABLE IF EXISTS fact_games;"""
    cursor.execute(drop_table_query)
    print('fact_games dropped')

# verify dropped by querying
try:
    select_query = """SELECT * FROM fact_games;"""
    cursor.execute(select_query)
    print(cursor.fetchall())
    print('results found, drop failed')
except:
    print('exception: confirmed fact_games was dropped and does not exist')