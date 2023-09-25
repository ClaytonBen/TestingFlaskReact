import json
import requests

class ApiFunctions:
    @staticmethod
    def get_rosters(league_id):
        url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
        response = requests.request("GET", url)
        owner_lineups = response.json()
        lineups = []
        for lineup in owner_lineups:
            user_lineup = {
                "owner_id": lineup['owner_id'],
                "starters": lineup['starters'],
                "players": lineup['players']
            }
            lineups.append(user_lineup)
        return {'lineups': lineups}
    @staticmethod
    def get_owner_info(league_id):
        url = f"https://api.sleeper.app/v1/league/{league_id}/users"
        response = requests.request("GET", url)
        data = response.json()
        owners = []
        for id in data:
            user_info = {
                "display_name": id['display_name'],
                "owner_id": id['user_id']
            }
            owners.append(user_info)
        return owners
    @staticmethod
    def save_player_info():
        url = "https://api.sleeper.app/v1/players/nfl"
        response = requests.request("GET", url)
        player_info = response.json()
        with open('players.json', 'w') as outfile:
            json.dump(player_info, outfile)
    @staticmethod
    def get_player_info(file):
        with open(file) as json_file:
            player_info = json.load(json_file)
        return player_info
    