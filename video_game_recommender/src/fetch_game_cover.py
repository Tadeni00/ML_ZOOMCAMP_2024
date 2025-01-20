import requests

RAWG_API_KEY = "8318ac06f229417b8fb269f759fba502"

def fetch_game_cover(game_name):
    url = f"https://api.rawg.io/api/games?key={RAWG_API_KEY}&search={game_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            game = data["results"][0]
            return {
                "name": game.get("name", "Unknown"),
                "release_date": game.get("released", "Unknown"),
                "cover_url": game.get("background_image", None)
            }
        else:
            print(f"No results found for game: {game_name}")
            return None
    else:
        print(f"Failed to fetch data for '{game_name}'. Status Code: {response.status_code}")
        return None
