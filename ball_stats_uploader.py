# # opens a connection to ball_stats_database.db, takes input for a single game, inserts into DB and repeats for next game up to specified count of games

import sqlite3
import ball_stats_table_creator

# variable definitions
# player_stat_dict will store each player as a key and a list denoting score, goal, assists, saves, shots
player_stat_dict = {}
normal_players = ['davis', 'crank', 'mike']
player_bool_dict = {}

ball_stats_conn = sqlite3.connect('ball_stats_database.db')
cursor = ball_stats_conn.cursor()
print("goliath online")

ball_stats_table_creator.create_ball_stats()
print('fact_games created/exists in ball_stats_database.db')

# store date
print('input game date yyyy-mm-dd')
date_to_store = input()

print('you kick ball how many times tonight?')
number_of_games = int(input())

# validate which players were involved
for player in normal_players:
    print(f'did {player} play? y/n')
    player_response = str(input())
    player_bool_dict[player] = player_response

for game_num in range(number_of_games):
    print(f'logging game {game_num+1}')
    print('you win? y/n')
    win_loss = input()

    print('goals for?')
    goals_for = input()

    print('goals against?')
    goals_against = input()

    print('tournament? y/n')
    tournament = input()

    print('ot? y/n')
    ot = input()

    for player in normal_players:
        if player_bool_dict[player] == 'y':
            print(f'input {player} score, goals, assists, saves, shots')
            player_score = int(input())
            player_goals = int(input())
            player_assists = int(input())
            player_saves = int(input())
            player_shots = int(input())
        else:
            player_score = 0
            player_goals = 0
            player_assists = 0
            player_saves = 0
            player_shots = 0
        player_stat_dict[player] = [player_score, player_goals, player_assists, player_saves, player_shots]
    print('any notes?')
    notes = str(input())

    insert_query = f"""INSERT INTO fact_games (date 
        , win 
        , goals_for 
        , goals_against 
        , tournament 
        , ot 
        , davis_score 
        , davis_goals 
        , davis_assists 
        , davis_saves 
        , davis_shots 
        , crank_score 
        , crank_goals 
        , crank_assists 
        , crank_saves 
        , crank_shots 
        , mike_score 
        , mike_goals 
        , mike_assists 
        , mike_saves 
        , mike_shots 
        , notes 
        )
        VALUES (
        '{date_to_store}', '{win_loss}', {goals_for}, {goals_against}, '{tournament}', '{ot}',
        {player_stat_dict['davis'][0]}, {player_stat_dict['davis'][1]}, {player_stat_dict['davis'][2]}, {player_stat_dict['davis'][3]}, {player_stat_dict['davis'][4]},
        {player_stat_dict['crank'][0]}, {player_stat_dict['crank'][1]}, {player_stat_dict['crank'][2]}, {player_stat_dict['crank'][3]}, {player_stat_dict['crank'][4]},
        {player_stat_dict['mike'][0]}, {player_stat_dict['mike'][1]}, {player_stat_dict['mike'][2]}, {player_stat_dict['mike'][3]}, {player_stat_dict['mike'][4]},
        '{notes}'
        );"""
    # print(insert_query)
    cursor.execute(insert_query)
    print('inserted rows')

ball_stats_conn.commit()

if ball_stats_conn:
    ball_stats_conn.close()
    print("The ball_stats_conn connection is closed")