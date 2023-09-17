import fretboard
from constants import NATURAL_NOTES
import os


PATH = os.path.join("static", "guitar")

COLORS = {
    "E": "#FAD02E",  # Sunflower Yellow
    "F": "#F28D35",  # Tangerine
    "G": "#D83367",  # Crimson
    "A": "#635DFF",  # Ultramarine
    "B": "#508BF9",  # Blue Jeans
    "C": "#1AB39F",  # Turquoise
    "D": "#2EC4B6"   # Mint
}

NOTE_TO_STRING_AND_FRET = {
    "E-2": (0, 0),  # Low E string, Open
    "F-2": (0, 1),
    "G-2": (0, 3),
    "A-2": (1, 0),  # A string, Open
    "B-2": (1, 2),
    "C-3": (1, 3),
    "D-3": (2, 0),  # D string, Open
    "E-3": (2, 2),
    "F-3": (2, 3),
    "G-3": (3, 0),  # G string, Open
    "A-3": (3, 2),
    "B-3": (4, 0),  # B string, Open
    "C-4": (4, 1),
    "D-4": (4, 3),
    "E-4": (5, 0),  # High E string, Open
    "F-4": (5, 1),
    "G-4": (5, 3)
}



def display_notes(notes):
    fb = fretboard.Fretboard(frets=(0, 3))
    for note in notes:
        string, fret = NOTE_TO_STRING_AND_FRET[note]
        note_name = note.split("-")[0] # remove octave, so E-2 -> E
        color = COLORS[note_name]
        fb.add_marker(string=string, fret=fret, label=note, color=color)
    fb.save(os.path.join(PATH, 'guitar.svg'))

if __name__ == "__main__":
    display_notes(NATURAL_NOTES)