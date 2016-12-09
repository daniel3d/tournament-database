# -*- coding: utf-8 -*-
# Test cases for tournament.py
# These tests are not exhaustive, but they should cover the majority of cases.
#
# If you do add any of the extra credit options, be sure to add/modify these
# test cases as appropriate to account for your module's added functionality.

from tournament import *
from textwrap import dedent


class style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def formatString(message):
    return dedent(message).replace("\n", "")


def error(message):
    raise ValueError(style.FAIL + formatString(message) + style.ENDC)


def warning(message):
    print style.WARNING + formatString(message) + style.ENDC


def succes(message):
    print style.OKGREEN + formatString(message) + style.ENDC


def info(message, header=False):
    if header:
        print style.HEADER + message + style.ENDC
    else:
        print style.OKBLUE + message + style.ENDC

info("                                                                                               ")
info("                                                                                               ")
info("▄▄▄█████▓ ▒█████   █    ██  ██▀███   ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████  ███▄    █ ▄▄▄█████▓")
info("▓  ██▒ ▓▒▒██▒  ██▒ ██  ▓██▒▓██ ▒ ██▒ ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒")
info("▒ ▓██░ ▒░▒██░  ██▒▓██  ▒██░▓██ ░▄█ ▒▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░")
info("░ ▓██▓ ░ ▒██   ██░▓▓█  ░██░▒██▀▀█▄  ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ")
info("  ▒██▒ ░ ░ ████▓▒░▒▒█████▓ ░██▓ ▒██▒▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██░   ▓██░  ▒██▒ ░ ")
info("  ▒ ░░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ")
info("    ░      ░ ▒ ▒░ ░░▒░ ░ ░   ░▒ ░ ▒░░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░░   ░ ▒░    ░    ")
info("  ░      ░ ░ ░ ▒   ░░░ ░ ░   ░░   ░    ░   ░ ░   ░   ▒   ░      ░      ░      ░   ░ ░   ░      ")
info("             ░ ░     ░        ░              ░       ░  ░       ░      ░  ░         ░          ")
info("                                                                                               ")
info("Udacity Full Stack Web Developer Nanodegree", header=True)
info("Test cases for tournament.py created by Daniel Yovchev 2016", header=True)
info("These tests are not exhaustive, but they should cover the majority of cases", header=True)
info("                                                                                               ")


def testCount():
    """
    Test for initial player count,
             player count after 1 and 2 players registered,
             player count after players deleted.
    """
    deleteMatches()
    deletePlayers()
    count = countPlayers()
    if count == '0':
        error("""
        ! countPlayers should return numeric zero, not string '0'.""")
    if count != 0:
        error("""
        ! After deletion, countPlayers should return zero.""")
    succes("""
    1. countPlayers() returns 0 after initial deletePlayers() execution.""")
    registerPlayer("Chandra Nalaar")
    count = countPlayers()
    if count != 1:
        error("""
        ! After one player registers, countPlayers() should be 1. Got {count}
        """.format(count=count))
    succes("""
    2. countPlayers() returns 1 after one player is registered.""")
    registerPlayer("Jace Beleren")
    count = countPlayers()
    if count != 2:
        error("""
        ! After two players register, countPlayers() should be 2. Got {count}
        """.format(count=count))
    succes("""
    3. countPlayers() returns 2 after two players are registered.""")
    deletePlayers()
    count = countPlayers()
    if count != 0:
        error("""
        ! After deletion, countPlayers should return zero.""")
    succes("""
    4. countPlayers() returns zero after registered players are deleted.""")
    succes("""
    5. Player records successfully deleted.""")


def testStandingsBeforeMatches():
    """
    Test to ensure players are properly represented in standings prior
    to any matches being reported.
    """
    deleteMatches()
    deletePlayers()
    registerPlayer("Melpomene Murray")
    registerPlayer("Randy Schwartz")
    standings = playerStandings()
    if len(standings) < 2:
        error("""
        ! Players should appear in playerStandings even before, 
        they have played any matches.""")
    elif len(standings) > 2:
        error("""
        ! Only registered players should appear in standings.""")
    if len(standings[0]) != 7:
        error("""
        ! Each playerStandings row should have seven columns.""")
    [   # i, n, m, w, l, d, s
        (id1, name1, matches1, wins1, loses1, draws1, score1),
        (id2, name2, matches2, wins2, loses2, draws2, score2)
    ] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        error("""
        ! Newly registered players should have no matches or wins.""")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        error("""
        ! Registered players' names should appear in standings,
        even if they have no matches played.""")
    succes("""
    6. Newly registered players appear in the standings with no matches.""")


def testReportMatches():
    """
    Test that matches are reported properly.
    Test to confirm matches are deleted properly.
    """
    deleteMatches()
    deletePlayers()
    registerPlayer("Bruno Walton")
    registerPlayer("Boots O'Neal")
    registerPlayer("Cathy Burton")
    registerPlayer("Diane Grant")
    registerPlayer("Daniel Yovchev")
    registerPlayer("Randy Schwartz")
    standings = playerStandings()
    [id1, id2, id3, id4, id5, id6] = [row[0] for row in standings]
    reportMatch(id1, id2, 0)
    reportMatch(id3, id4, id3)
    reportMatch(id5, id6, id6)
    standings = playerStandings()
    for (i, n, m, w, l, d, s) in standings:
        if m != 1:
            error("! Each player should have one match recorded.")
        if i in (id1, id2) and w != 0 and l != 0 and s != 0.5:
            error("! Each draw should give 0.5 score to the player.")
        if i in (id3, id6) and w != 1 and l != 0 and score != 1.0:
            error("! Each match winner should have one win recorded.")
        if i in (id4, id5) and w != 0 and l != 1 and score != 0.0:
            error("! Each match loser should have zero wins recorded.")
    succes("""
    7. After a match, players have updated standings.""")
    deleteMatches()
    standings = playerStandings()
    if len(standings) != 6:
        error("""
        ! Match deletion should not change number of players in standings.""")
    for (i, n, m, w, l, d, s) in standings:
        if m != 0:
            error("""
            ! After deleting matches, players should have zero 
            matches recorded.""")
        if w != 0:
            error("""
            ! After deleting matches, players should have zero 
            wins recorded.""")
    succes("""
    8. After match deletion, player standings are properly reset.""")
    succes("""
    9. Matches are properly deleted.""")


def testPairings():
    """
    Test that pairings are generated properly 
    both before and after match reporting.
    """
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Fluttershy")
    registerPlayer("Applejack")
    registerPlayer("Pinkie Pie")
    registerPlayer("Rarity")
    registerPlayer("Rainbow Dash")
    registerPlayer("Princess Celestia")
    registerPlayer("Princess Luna")
    standings = playerStandings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    pairings = swissPairings()
    if len(pairings) != 4:
        error("""
        ! For eight players, swissPairings should return 4 pairs. Got {pairs}.
        """.format(pairs=len(pairings)))
    reportMatch(id1, id2, id1)
    reportMatch(id3, id4, id3)
    reportMatch(id5, id6, id5)
    reportMatch(id7, id8, id7)
    pairings = swissPairings()
    if len(pairings) != 4:
        error("""
        ! For eight players, swissPairings should return 4 pairs. 
        Got {pairs}.""".format(pairs=len(pairings)))
    [
        (pid1, pname1, pid2, pname2),
        (pid3, pname3, pid4, pname4),
        (pid5, pname5, pid6, pname6),
        (pid7, pname7, pid8, pname8)
    ] = pairings
    possible_pairs = set([frozenset([id1, id3]), frozenset([id1, id5]),
                          frozenset([id1, id7]), frozenset([id3, id5]),
                          frozenset([id3, id7]), frozenset([id5, id7]),
                          frozenset([id2, id4]), frozenset([id2, id6]),
                          frozenset([id2, id8]), frozenset([id4, id6]),
                          frozenset([id4, id8]), frozenset([id6, id8])
                          ])
    actual_pairs = set([frozenset([pid1, pid2]),
                        frozenset([pid3, pid4]),
                        frozenset([pid5, pid6]),
                        frozenset([pid7, pid8])])
    for pair in actual_pairs:
        if pair not in possible_pairs:
            error("""
            ! After one match, players with one win should be paired.""")
    succes("""
    10. After one match, players with one win are properly paired.""")


if __name__ == '__main__':
    warning("""-- Running testCount()""")
    testCount()
    warning("""-- Running testStandingsBeforeMatches()""")
    testStandingsBeforeMatches()
    warning("""-- Running testReportMatches()""")
    testReportMatches()
    warning("""-- Running testPairings()""")
    testPairings()
    warning("""Thank you for reviwing this code ;)""")
    succes("""Success!  All tests pass!""")
