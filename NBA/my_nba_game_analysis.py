import csv
import re
import json

def load_data(filename):
    result = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            result.append(row)
    return result

def is_away_team(away_team, current_team):
    return away_team == current_team

def update_stats(player_stats, description):
    if "makes" in description:
        if "3-pt" in description:
            player_stats["3P"] += 1
            player_stats["3PA"] += 1
            player_stats["PTS"] += 3
        elif "2-pt" in description:
            player_stats["FG"] += 1
            player_stats["FGA"] += 1
            player_stats["PTS"] += 2
        elif "free throw" in description:
            player_stats["FT"] += 1
            player_stats["FTA"] += 1
            player_stats["PTS"] += 1
    elif "misses" in description:
        if "3-pt" in description:
            player_stats["3PA"] += 1
        elif "2-pt" in description:
            player_stats["FGA"] += 1
        elif "free throw" in description:
            player_stats["FTA"] += 1
    elif "rebound" in description:
        if "Offensive" in description:
            player_stats["ORB"] += 1
        else:
            player_stats["DRB"] += 1
        player_stats["TRB"] += 1
    elif "assist" in description:
        player_stats["AST"] += 1
        assisting_player = re.search(r'assist by (.*)\)', description)
        if assisting_player:
            player_stats["AST_PLAYER"] = assisting_player.group(1).strip()
    elif "steal" in description:
        player_stats["STL"] += 1
    elif "block" in description:
        player_stats["BLK"] += 1
    elif "Turnover" in description:
        player_stats["TOV"] += 1
    elif "foul" in description:
        player_stats["PF"] += 1
    # print(player_stats)

def calculate_percentages(player_stats):
    player_stats["FG%"] = round((player_stats["FG"] / player_stats["FGA"] * 100) if player_stats["FGA"] > 0 else 0, 1)
    player_stats["3P%"] = round((player_stats["3P"] / player_stats["3PA"] * 100) if player_stats["3PA"] > 0 else 0, 1)
    player_stats["FT%"] = round((player_stats["FT"] / player_stats["FTA"] * 100) if player_stats["FTA"] > 0 else 0, 1)

def initialize_player_stats(player_name):
    return {
                "player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, 
        "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0
    }

def analyse_nba_game(play_by_play_moves):
    result = {"home_team": {"name": "", "players_data": {}}, "away_team": {"name": "", "players_data": {}}}

    # Regular expressions for extracting player names
    patterns = {
        "makes_3pt": re.compile(r'^(.*) makes 3-pt'),
        "makes_2pt": re.compile(r'^(.*) makes 2-pt'),
        "makes_ft": re.compile(r'^(.*) makes free throw'),
        "misses_3pt": re.compile(r'^(.*) misses 3-pt'),
        "misses_2pt": re.compile(r'^(.*) misses 2-pt'),
        "misses_ft": re.compile(r'^(.*) misses free throw'),
        "off_rebound": re.compile(r'Offensive rebound by (.*)'),
        "def_rebound": re.compile(r'Defensive rebound by (.*)'),
        "assist": re.compile(r'\(assist by (.*)\)'),
        
        "steal": re.compile(r'steal by (.*)\)'),
        "block": re.compile(r'\(block by (.*)\)'),
        
        "turnover": re.compile(r'Turnover by (.*?) \(bad pass; steal by (.*?)\)'),
        "simple_turnover": re.compile(r'Turnover by (.*?) \('),
        
        "foul": re.compile(r'Shooting foul by (.*)'),
        "drawn_foul": re.compile(r'\(drawn by (.*)\)')
    }

    for play in play_by_play_moves:
        period, remaining_sec, current_team, away_team, home_team, away_score, home_score, current_action = play

        if not result["home_team"]["name"]:
            result["home_team"]["name"] = home_team
        if not result["away_team"]["name"]:
            result["away_team"]["name"] = away_team

        team_key = "home_team" if current_team == home_team else "away_team"

        # Special case for turnovers involving steals
        turnover_match = patterns["turnover"].search(current_action)
        if turnover_match:
            turnover_player_name = turnover_match.group(1).strip()
            steal_player_name = turnover_match.group(2).strip()
        
            #Update turnover player stats
            if turnover_player_name not in result[team_key]["players_data"]:
                result[team_key]["players_data"][turnover_player_name] = initialize_player_stats(turnover_player_name)
            result[team_key]["players_data"][turnover_player_name]["TOV"] += 1

            # Determine the correct team key for the steal player
            steal_team_key = "away_team" if team_key == "home_team" else "home_team"

            # Update steal player stats
            steal_player_name = steal_player_name.strip().split(" (")[0].strip()
            if steal_player_name not in result[steal_team_key]["players_data"]:
                result[steal_team_key]["players_data"][steal_player_name] = initialize_player_stats(steal_player_name)
            result[steal_team_key]["players_data"][steal_player_name]["STL"] += 1
            continue # Skip to the next play
        
        # Simple turnover
        simple_turnover_match = patterns["simple_turnover"].search(current_action)
        if simple_turnover_match:
            turnover_player_name = simple_turnover_match.group(1).strip()
            if turnover_player_name not in result[team_key]["players_data"]:
                result[team_key]["players_data"][turnover_player_name] = initialize_player_stats(turnover_player_name)
            result[team_key]["players_data"][turnover_player_name]["TOV"] += 1


        # Regular player action parsting    
        player_name = None
        for key, pattern in patterns.items():
            match = pattern.search(current_action)
            if match:
                player_name = match.group(1).split(" (")[0].strip() # Extract only player name
                break
        if not player_name:
            continue
        # player_name = player_name.split(" (")[0].strip()
        if player_name not in result[team_key]["players_data"]:
            result[team_key]["players_data"][player_name] = initialize_player_stats(player_name)
        update_stats(result[team_key]["players_data"][player_name], current_action)

        # Assist handling
        assist_match = patterns["assist"].search(current_action)
        if assist_match:
            assisting_player = assist_match.group(1).strip()
            if assisting_player not in result[team_key]["players_data"]:
                result[team_key]["players_data"][assisting_player] = initialize_player_stats(assisting_player)
            result[team_key]["players_data"][assisting_player]["AST"] += 1
        
        # Blocked shot
        missed_shot_match = patterns["misses_2pt"].search(current_action) 
        if missed_shot_match:
            missed_shot_player = missed_shot_match.group(1).strip()
            if missed_shot_player not in result[team_key]["players_data"]:
                result[team_key]["players_data"][missed_shot_player] = initialize_player_stats(missed_shot_player)
            result[team_key]["players_data"][missed_shot_player]["FGA"] += 1

            # Block handling after the blocked shot
            block_match = patterns["block"].search(current_action)
            if block_match:
                blocking_player = block_match.group(1).strip()
                # Assign blocking_player to the opposite team of the missed_shot_player
                blocking_team_key = "away_team" if team_key == "home_team" else "home_team"
                
                if blocking_player not in result[blocking_team_key]["players_data"]:
                    result[blocking_team_key]["players_data"][blocking_player] = initialize_player_stats(blocking_player)
                result[blocking_team_key]["players_data"][blocking_player]["BLK"] += 1
            
        # Drawn by foul
        if "drawn by" in current_action:
            match = patterns["drawn_foul"].search(current_action)
            if match:
                drawn_player_name = match.group(1).strip()
                if drawn_player_name not in result[team_key]["players_data"]:
                    result[team_key]["players_data"][drawn_player_name] = initialize_player_stats(drawn_player_name)
                

                # Determine the team key of player who committed the foul
                committing_team_key = "away_team" if current_team == home_team else "home_team"
                committing_player_name_match = patterns["foul"].search(current_action)
                if committing_player_name_match:
                    committing_player_name = committing_player_name_match.group(1).strip().split(" (")[0].strip()
                    # committing_player_name = committing_player_name.strip().split(" (")[0].strip()
                     
                    if committing_player_name not in result[committing_team_key]["players_data"]:
                        result[committing_team_key]["players_data"][committing_player_name] = initialize_player_stats(committing_player_name)
                    result[committing_team_key]["players_data"][committing_player_name]["PF"] += 1

    for team in ["home_team", "away_team"]:
        for player_stats in result[team]["players_data"].values():
            calculate_percentages(player_stats)
        result[team]["players_data"] = list(result[team]["players_data"].values())
    return result



def _main():
    play_by_play_moves = load_data("sample.txt")
    game_summary = analyse_nba_game(play_by_play_moves)
    print("Game Summ: ", game_summary)

_main()




    


