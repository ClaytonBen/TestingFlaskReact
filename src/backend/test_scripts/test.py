import os
print(os.getcwd())

from src.backend.api_functions.api_functions import ApiFunctions

rosters = ApiFunctions.get_rosters("695699151924555776")
owners = ApiFunctions.get_owner_info("695699151924555776")

id_to_name = {owner['owner_id']: owner['display_name'] for owner in owners}

player_lookup = ApiFunctions.get_player_info('players.json')

player_lookup['BUF']

output = [
    {
        'name': id_to_name[owner['owner_id']],
        'starters': [ player_lookup[player] for player in owner['starters']],
        'players': owner['players']
    }
    for owner in rosters['lineups']
]

for owner in rosters['lineups']:
    [ player_lookup[player] for player in owner['starters']]