#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import random


def connect(database_name="tournament"):
    """Connect to given PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={dbname}".format(dbname=database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception, error:
        print(error)


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor.execute("""DELETE FROM matches""")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute("""DELETE FROM players""")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    cursor.execute("""SELECT COUNT(*) FROM players""")
    result = cursor.fetchone()
    db.close()
    return result[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    cursor.execute("""
        INSERT INTO players (name) VALUES (%s)
    """, (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    cursor.execute("""SELECT * FROM standings ORDER BY score DESC""")
    result = cursor.fetchall()
    db.close()
    return result


def reportMatch(player, opponent, result):
    """Records the outcome of a single match between two players.

    Args:
      player:  the id number of the frist player
      opponent:  the id number of the second player
      result:  the id of the player who won or 0 for a draw
    """
    db, cursor = connect()
    cursor.execute("""
        INSERT INTO matches (player, opponent, result) VALUES(%s,%s,%s)
    """, (player, opponent, result))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()

    pairings = []
    for i in range(0, len(standings) / 2):
        player = standings[2 * i]
        opponent = standings[(2 * i) + 1]
        pairings.append((player[0], player[1], opponent[0], opponent[1]))

    return pairings


def playGame(players):
    """Simulate a game.

    Args:
        players: list of the players ids

    Returns:
        id of the player who win the game or 0 for a draw
    """
    result = random.randrange(-1, 2)
    return 0 if result == -1 else players[result]
