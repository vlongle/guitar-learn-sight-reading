from mingus.containers import Bar
from mingus.extra import lilypond as LilyPond
import os
from constants import NATURAL_NOTES, ALL_NOTES
from utils import trim_svg_whitespace
import subprocess




PATH = os.path.join("static", "sheet")


def bars_to_lilypond(bars):
    lily_data = ["{ \\clef \"treble_8\" \\time 4/4"]
    for bar in bars:
        bar_content = LilyPond.from_Bar(bar).replace("{", "").replace("}", "")
        # Remove subsequent time signatures, keeping only the first one
        bar_content = bar_content.replace("\\time 4/4", "")
        lily_data.append(bar_content)
    lily_data.append("}")
    return "\n".join(lily_data)

def make_guitar_sheet(bars):
    # Convert the list of bars to LilyPond notation with guitar clef.
    lilypond_data = bars_to_lilypond(bars)

    insertion_index = lilypond_data.find("{") + 1
    lilypond_data = lilypond_data[:insertion_index] + "\\clef \"treble_8\" " + lilypond_data[insertion_index:]
    return lilypond_data

def generate_bar_with_notes(notes):
    b = Bar()
    for note in notes:
        b + note
    return b

def save_to_ly_file(lilypond_data):
    filename = os.path.join(PATH, "sheet.ly")
    with open(filename, 'w') as file:
        file.write(lilypond_data)
    return lilypond_data, os.path.abspath(filename)

def generate_sheet_music(notes, generate_pdf=True):
    bars = []
    bar_notes = []
    for note in notes:
        bar_notes.append(note)
        if len(bar_notes) == 4:
            bars.append(generate_bar_with_notes(bar_notes))
            bar_notes = []

    # Handle any remaining notes
    if bar_notes:
        bars.append(generate_bar_with_notes(bar_notes))
        
    lilypond_data = make_guitar_sheet(bars)
    print("Lilypond data:", lilypond_data)
    if generate_pdf:
        print("Generating PDF...")
        LilyPond.to_pdf(lilypond_data, os.path.join(PATH, "sheet.pdf"))

        pdf_path = os.path.join(PATH, "sheet.pdf")
        svg_path = os.path.join(PATH, "sheet.svg")
        svg_path = os.path.join(PATH, "sheet.svg")
        subprocess.run(["pdf2svg", pdf_path, svg_path])
        trim_svg_whitespace(os.path.join(PATH, "sheet.svg"))

    return save_to_ly_file(lilypond_data)

if __name__ == "__main__":
    print(len(ALL_NOTES), len(NATURAL_NOTES))
    generate_sheet_music(NATURAL_NOTES)