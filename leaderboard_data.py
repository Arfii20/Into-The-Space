"""
Handles the leaderboard data using sqlite3 library.
Contains 3 functions which creates, saves and provides values for the leaderboard.
"""

import sqlite3


def create_database_table():
    """
    This function runs when the program is run and if there is no database table,
    it creates a table with the selected name.
    If the table exists, the function has no effect.
    """
    # Connects to the database
    conn = sqlite3.connect("leaderboard_database.db")

    # Creates cursor and attempts to create a table if it does not already exist.
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS leaderboard (Name text, Score integer)")

    # Commits and closes the file after finishing all tasks.
    conn.commit()
    conn.close()


def save_leaderboard(player_name, total_score):
    """
    Takes player's name and score and stores them to the database.
    Player's name will be a string and score will be an integer.
    """
    # Connects to the database.
    conn = sqlite3.connect("leaderboard_database.db")

    # create cursor
    curs = conn.cursor()

    # Inserts the name and score to a new row on the leaderboard table.
    curs.execute("INSERT INTO leaderboard VALUES (:Name, :Score)",
                 {
                     "Name": player_name,
                     "Score": total_score
                 })

    # Commits and closes the database.
    conn.commit()
    conn.close()


def get_leaderboard_values():
    """Gets top 10 scores from the database and returns to the caller of the function."""
    # Connects to the database.
    conn = sqlite3.connect("leaderboard_database.db")

    # creates the cursor.
    curse = conn.cursor()

    # Selects all the columns and orders the table by descending score.
    curse.execute("SELECT *, oid FROM leaderboard ORDER BY Score DESC")

    # Fetches top 10 scores.
    leaders = curse.fetchmany(10)

    conn.commit()
    conn.close()

    # Returns the list of tuples to the caller.
    return leaders
