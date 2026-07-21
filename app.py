from flask import Flask, session, render_template, request
from dotenv import load_dotenv
from roshambeaux import play
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET")
@app.route("/", methods=["GET", "POST"])

def home():
    if request.method == "GET":
        session.clear()

    game = None
    finished = False
    win_rate = 0

    if "wins" not in session:
        session["wins"] = 0
        session["losses"] = 0
        session["ties"] = 0

    if "current_round" not in session:
        session["current_round"] = 1

    if "waiting" not in session:
        session["waiting"] = False

    if request.method == "POST":
        if "rounds" in request.form:
            session["rounds"] = int(request.form["rounds"])
            session["current_round"] = 1
            session["wins"] = 0
            session["losses"] = 0
            session["ties"] = 0
            session["waiting"] = False

        elif "choice" in request.form:
            user_choice = request.form["choice"]
            game = play(user_choice)

            if game["result"] == "You Win":
                session["wins"] += 1
            elif game["result"] == "You Lose":
                session["losses"] += 1
            else:
                session["ties"] += 1

            session["waiting"] = True

        elif "next" in request.form:
            session["current_round"] += 1
            session["waiting"] = False

        elif "final" in request.form:
            finished = True

    if session.get("rounds"):
        win_rate = (session["wins"]/session["rounds"])*100

    passed = win_rate >= 65

    return render_template(
        "Website.html",
        game=game,
        wins=session.get("wins", 0),
        losses=session.get("losses", 0),
        ties=session.get("ties", 0),
        round=session.get("current_round", 1),
        rounds=session.get("rounds", 0),
        waiting=session.get("waiting", False),
        finished=finished,
        win_rate=win_rate,
        passed=passed
    )

if __name__ == "__main__":
    app.run(debug=True)