import json

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
                starters.append(starter_info["team"])
            else:
                starters.append(starter_info['full_name'])
    players = []
    for player in owner['players']:
        if player != '0':
            player_info = player_lookup[player]
            if player_info['position'] == "DEF":
                players.append(player_info["team"])
            else:
                players.append(player_info['full_name'])
    results ={
        'name': id_to_name[owner['owner_id']],
        'starters': starters,
        'players': players
    }
    full_rosters.append(results)

with open("lineups.json", "w") as outfile:
    json_string = json.dump(full_rosters, outfile)
