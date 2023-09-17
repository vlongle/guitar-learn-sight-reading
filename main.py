from flask import Flask, render_template, jsonify, url_for
import random
from sheet import generate_sheet_music
from guitar import display_notes
from constants import NATURAL_NOTES
import os

app = Flask(__name__)

@app.route('/')
def index():
  # always start with a sheet with one-note
  # generate_sheet_music(["C"])
  # # always start with a blank guitar
  # display_notes([])
  return render_template('index.html')

@app.route('/random_note')
def random_note():
    note = random.choice(NATURAL_NOTES)
    print("random note:", note)
    with open("selected_note.txt", "w") as file:
        file.write(note)
    generate_sheet_music([note])
    display_notes([])
    return jsonify(note=note)

@app.route('/reveal_note')
def reveal_note():
    if not os.path.exists("selected_note.txt"):
        return jsonify(note="no note selected")
    with open("selected_note.txt", "r") as file:
        note = file.read()
    print("revealed note:", note)
    display_notes([note])
    return jsonify(note=note)


@app.route('/show_all')
def show_all():
    generate_sheet_music(NATURAL_NOTES)
    display_notes(NATURAL_NOTES)
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)
