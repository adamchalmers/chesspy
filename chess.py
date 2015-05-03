from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
games = {}

class Game():

	def __init__(self, game_id, color, pw):
		assert color == "white" or color == "black"
		self.game_id = game_id
		self.pw = {color: pw}
		self.board = [[None for i in range(8)] for i in range(8)]

	def board_str(self):
		s = ""
		for x in range(8):
			for y in range(8):
				piece = self.board[x][y]
				if piece:
					s += piece + " "
				else:
					s += ".. "
			s += str(x) + "\n"
		return s

@app.route("/game/<game_id>")
def game(game_id):
	if game_id in games:
		return render_template("game.html", game_id=game_id)
	else:
		return render_template("no_game.html", games=games)

@app.route("/new.html")
def new_game():
    return render_template("new.html")

@app.route("/")
def index():
	return render_template("index.html", games=games)

@app.route("/init_new", methods=["POST"])
def init_new():
	game_id = request.form["id"] 
	pw = request.form["pw"]
	color = request.form["color"]
	
	if game_id in games:
		return "Game already exists."
	else:
		games[game_id] = Game(game_id, color, pw)
		return redirect(url_for("game", game_id=game_id))




if __name__ == "__main__":
    app.run(debug=True)
