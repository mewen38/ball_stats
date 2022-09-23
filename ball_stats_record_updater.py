import sqlite3

updates = []

ball_stats_conn = sqlite3.connect('ball_stats_database.db')
cursor = ball_stats_conn.cursor()
print("goliath online")

print('input game_id to update')
game_id = input()
select_query = f"""SELECT * FROM fact_games WHERE game_id = {game_id};"""
cursor.execute(select_query)
print(cursor.fetchall())

print('how many updates you wanna make dude?')
update_count = int(input())

# input indefinite number of updates
print("what updates you wanna make dude?  type 'col_name = new_val'")
for i in range(update_count):
    update_col_val = input()
    updates.append(update_col_val)

print("'are you sure you want to commit updates? type 'me sure'")
answer = input()
if answer == 'me sure':
    for update in updates:
        update_query = f"""
        UPDATE fact_games
        SET {update}
        WHERE game_id = {game_id}
        ;
        """
        cursor.execute(update_query)
        ball_stats_conn.commit()
else:
    print('unsure, exiting uncommitted')

print('record updated...')
select_query = f"""SELECT * FROM fact_games WHERE game_id = {game_id};"""
cursor.execute(select_query)
print(cursor.fetchall())

