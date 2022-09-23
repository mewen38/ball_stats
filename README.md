# ball_stats
stats for playing rocket ball, howilemus we finally got em

ball_stats_table_creator.py creates fact_games table and houses DDL, called by uploader but generally will be skipped

ball_stats_drop_script.py drops the fact_games table

ball_stats_uploader.py accepts inputs and inserts into db

ball_stats_basic_select.py retrieves entire row for a given game_id

ball_stats_open_query.py executes a full SQL statement

ball_stats_analytics_view.py view DDL for analytics

ball_stats_record_updater.py input a game_id and update an indefinite number of fields for that record
