import csv
import re

def load_data(filename):
    result = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')

        
        for row in csvreader:
            result.append(row)

    return result

def is_away_team(away_team, current_team):
    return away_team == current_team

def analyse_nba_game(play_by_play_moves):
    result = {"home_team": {"name": "", "players_data": []}, "away_team": {"name": "otherteam", "players_data": []}}

    for play in play_by_play_moves:
        current_team = play[2]
        home_team = play[3]
        away_team = play[4]
        current_action = play[7]

        three_pts_regexp = re.compile(r'(.*) makes 3-pt jump shot from')
        data = three_pts_regexp.search(current_action)
        player_name = data[1]
        print(current_action)
        print(data[1])
        if is_away_team(away_team, current_team):
            result["away_team"]["players_data"][player_name]['3P'] += 1
        else:
            result["home_team"]["players_data"][player_name]['3P'] += 1

        # print(current_team)
        # print(current_action)
        break

def _main():
    play_by_play_moves = load_data("data_light.txt")
    analyse_nba_game(play_by_play_moves)

_main()




    



'''
1. Parse each play
2. Update player stats
3. Calc percentage for field goals, three-pointers, free-throws
4. Structure the data in the right format
Create a function analyse_nba_game(play_by_play_moves) which receives an array of play and will return a dictionary summary of the game.

Each play follow this format:

PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
They are ordered by time.

The return dictionary (hash) will have this format:

{"home_team": {"name": TEAM_NAME, "players_data": DATA}, "away_team": {"name": TEAM_NAME, "players_data": DATA}}
DATA will be an array of hashes with this format:
{"player_name": XXX, "FG": XXX, "FGA": XXX, "FG%": XXX, "3P": XXX, "3PA": XXX, "3P%": XXX, "FT": XXX, "FTA": XXX, "FT%": XXX, "ORB": XXX, "DRB": XXX, "TRB": XXX, "AST": XXX, "STL": XXX, "BLK": XXX, "TOV": XXX, "PF": XXX, "PTS": XXX}
Percent are on 100.
Player is a string everything else are integers.

Example00

1|708.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by K. Thompson (bad pass; steal by S. Adams)
1|703.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by P. George (bad pass)
1|691.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Curry makes 3-pt jump shot from 24 ft (assist by K. Durant)
1|673.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Adams misses 2-pt jump shot from 12 ft
1|671.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|Offensive rebound by D. Schröder
1|667.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|P. George misses 3-pt jump shot from 26 ft
1|665.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|Defensive rebound by K. Durant
1|657.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|K. Durant makes 2-pt layup from 2 ft
1|638.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|D. Schröder misses 2-pt jump shot from 14 ft
1|636.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Offensive rebound by D. Schröder
1|623.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|S. Adams misses 2-pt layup from 3 ft (block by K. Durant)
1|621.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Defensive rebound by D. Green
1|618.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Turnover by D. Green (out of bounds lost ball)
1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|2|5|P. Patterson makes 2-pt layup from 2 ft (assist by S. Adams)
1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|2|5|Shooting foul by D. Green (drawn by P. Patterson)
1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|5|P. Patterson makes free throw 1 of 1
1|598.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|D. Jones makes 2-pt dunk from 1 ft (assist by D. Green)
1|581.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|P. Patterson misses 2-pt hook shot from 8 ft
1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|Offensive rebound by P. Patterson
1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|Shooting foul by K. Thompson (drawn by P. Patterson)
1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson makes free throw 1 of 2
1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson misses free throw 2 of 2
1|580.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by D. Green
1|569.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|D. Green misses 3-pt jump shot from 28 ft
1|567.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by D. Schröder
1|552.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson misses 2-pt jump shot from 16 ft
1|551.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by S. Curry
1|547.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Turnover by S. Curry (bad pass; steal by P. George)
1|542.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Turnover by S. Adams (bad pass; steal by K. Durant)
1|533.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|10|K. Thompson makes 3-pt jump shot from 26 ft (assist by D. Green)
'''