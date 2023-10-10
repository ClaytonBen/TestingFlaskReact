import json
import requests
from sleeper_wrapper import Stats

stats = Stats()

projections = stats.get_all_projections("regular",2023)

with open("projections.json", "w") as outfile:
    json_string = json.dump(projections, outfile)

from api_functions import api_functions

league = api_functions.ApiFunctions("930602680773357568")
rosters = league.get_rosters()
owners = league.get_owner_info()

id_to_name = {owner['owner_id']: owner['display_name'] for owner in owners}

player_lookup = league.get_player_info('players.json')

full_rosters = []
for owner in rosters['lineups']:
    starters = []
    for starter in owner['starters']:
        if starter != '0':
            starter_info = player_lookup[starter]
            if starter_info['position'] == "DEF":
                starters.append(
                        {   
                            "name" : starter_info["team"],
                            "id" : starter,
                            "projections": projections[starter]
                        }
                    )
            else:
                starters.append(
                        {
                            "name" : starter_info['full_name'],
                            "id" : starter,
                            "projections": projections[starter]
                        }
                    )
    players = []
    for player in owner['players']:
        if player != '0':
            player_info = player_lookup[player]
            if player_info['position'] == "DEF":
                players.append(
                        {   
                            "name" : player_info["team"],
                            "id" : player,
                            "projections": projections[player]
                        }
                    )
            else:
                players.append(
                        {
                            "name" : player_info['full_name'],
                            "id" : player,
                            "projections": projections[player]
                        }
                    )
    results = {
        'id': owner['owner_id'],
        'name': id_to_name[owner['owner_id']],
        'starters': starters,
        'players': players
    }
    full_rosters.append(results)

with open("lineups.json", "w") as outfile:
    json_string = json.dump(full_rosters, outfile)


