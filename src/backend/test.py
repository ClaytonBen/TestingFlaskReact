import json

from api_functions import api_functions


rosters = api_functions.ApiFunctions.get_rosters("695699151924555776")
owners = api_functions.ApiFunctions.get_owner_info("695699151924555776")

id_to_name = {owner['owner_id']: owner['display_name'] for owner in owners}

player_lookup = api_functions.ApiFunctions.get_player_info('players.json')

print(rosters)
rosters = []
for owner in rosters['lineups']:
    starters = []
    for starter in owner['starters']:
        if starter != "0":
            player_lookup[starter]

    players = []
    for player in owner['players']:
        if starter != "0":
            player_lookup[starter]
    results ={
        'name': id_to_name[owner['owner_id']],
        'starters': starters,
        'players': players
    }
    rosters.append(results)

with open("sample.json", "w") as outfile:
    json.dump(players, rosters)