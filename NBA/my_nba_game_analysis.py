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
        print('currActn: ', current_action)
        print('data1: ', data[1])
        print('data0: ', data[0])
        # if is_away_team(away_team, current_team):
        #     result["away_team"]["players_data"][player_name]['3P'] += 1
        # else:
        #     result["home_team"]["players_data"][player_name]['3P'] += 1

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

'''