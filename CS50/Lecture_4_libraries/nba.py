from nba_api.live.nba.endpoints import scoreboard
import json

# Today's Score Board
games = scoreboard.ScoreBoard()

# json
# print(json.dumps(games.get_json(), indent = 2))

# dictionary
# print(games.get_dict()["scoreboard"]["games"][1])
print("")
print("ScoreBoard:")
print("")
for i in games.get_dict()["scoreboard"]["games"]:
    print(i["homeTeam"]["teamCity"], " ", i["homeTeam"]["teamName"],
          " vs ", i["awayTeam"]["teamCity"], " ", i["awayTeam"]["teamName"], sep="")
    print("     Current Score: ", i["homeTeam"]
          ["score"], "-", i["awayTeam"]["score"], sep="")
    print("")
