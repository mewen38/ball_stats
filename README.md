# ball_stats
stats for playing rocket ball, howilemus we finally got em

ball_stats_table_creator.py creates fact_games table and houses DDL, called by uploader but generally will be skipped

ball_stats_drop_script.py drops the fact_games table

ball_stats_uploader.py accepts inputs and inserts into db

ball_stats_basic_select.py runs select * where you can input a game_id for quick data validation

ball_stats_analytics_view.py view DDL for analytics

ball_stats_record_updater.py input a game_id and update an indefinite number of fields for that record
