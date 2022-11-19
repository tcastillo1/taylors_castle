from nba_api.live.nba.endpoints import scoreboard
import json

# Today's Score Board
games = scoreboard.ScoreBoard()

file = open("scoreboard.txt", "w")

file.write("Scoreboard\n")

for i in games.get_dict()["scoreboard"]["games"]:
    text_to_write = (i["homeTeam"]["teamCity"] + " " + i["homeTeam"]["teamName"] + " vs " + i["awayTeam"]["teamCity"] + " " +
                     i["awayTeam"]["teamName"] + "\n" + "     Current Score: " +
                     str(i["homeTeam"]["score"]) + "-" +
                     str(i["awayTeam"]["score"])
                     + "\n")
    file.write(text_to_write)

file.close()
