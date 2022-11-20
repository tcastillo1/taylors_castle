from nba_api.live.nba.endpoints import scoreboard
import json

# Today's Score Board
games = scoreboard.ScoreBoard()

file = open("scoreboard.txt", "w")

file.write("Scoreboard\n")

for i in games.get_dict()["scoreboard"]["games"]:
    teams = (i["homeTeam"]["teamCity"] + " " + i["homeTeam"]["teamName"] + " vs " + i["awayTeam"]["teamCity"] + " " +
             i["awayTeam"]["teamName"] + "\n")
    score = ("     Current Score: " +
             str(i["homeTeam"]["score"]) + "-" + str(i["awayTeam"]["score"]) + "\n")
    home_leader = "     " + i["gameLeaders"]["homeLeaders"]["name"] + " " + \
        str(i["gameLeaders"]["homeLeaders"]["points"]) + " points\n"
    away_leader = "     " + i["gameLeaders"]["awayLeaders"]["name"] + " " + \
        str(i["gameLeaders"]["awayLeaders"]["points"]) + " points\n"
    file.write(teams)
    file.write(score)
    file.write(home_leader)
    file.write(away_leader)


file.close()
