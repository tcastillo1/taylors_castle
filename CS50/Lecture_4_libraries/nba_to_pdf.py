from fpdf import FPDF
from nba_api.live.nba.endpoints import scoreboard
import json

# Today's Score Board
games = scoreboard.ScoreBoard()


# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)

# create a cell
pdf.cell(200, 10, txt="Scoreboard",
         ln=1, align='C')

x = 2

for i in games.get_dict()["scoreboard"]["games"]:
    text_to_write = (i["homeTeam"]["teamCity"] + " " + i["homeTeam"]["teamName"] +
                     " vs " + i["awayTeam"]["teamCity"] + " " + i["awayTeam"]["teamName"])
    pdf.cell(200, 10, txt=text_to_write, ln=x, align='C')
    text_to_write = ("Current Score: " +
                     str(i["homeTeam"]["score"]) + "-" + str(i["awayTeam"]["score"]))
    pdf.cell(200, 10, txt=text_to_write, ln=x + 1, align='C')
    x = x + 2

pdf.cell(200, 10, txt="kings got robbed fuck the lakers", ln=x + 3, align='C')
pdf.output("scoreboard.pdf")
