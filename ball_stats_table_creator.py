import sqlite3

def create_ball_stats():
    ball_stats_conn = sqlite3.connect('ball_stats_database.db')
    cursor = ball_stats_conn.cursor()
    create_table_query = """CREATE TABLE IF NOT EXISTS fact_games (
        game_id INTEGER PRIMARY KEY AUTOINCREMENT
        , date TEXT
        , win TEXT
        , goals_for INT
        , goals_against INT
        , tournament TEXT
        , ot TEXT
        , davis_score INT
        , davis_goals INT
        , davis_assists INT
        , davis_saves INT
        , davis_shots INT
        , crank_score INT
        , crank_goals INT
        , crank_assists INT
        , crank_saves INT
        , crank_shots INT
        , mike_score INT
        , mike_goals INT
        , mike_assists INT
        , mike_saves INT
        , mike_shots INT
        , notes TEXT
        )
        ;"""
    return cursor.execute(create_table_query)