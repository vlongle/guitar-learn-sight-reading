import xml.etree.ElementTree as ET
import os

PATH = os.path.join("static", "sheet")

def trim_svg_whitespace(svg_path):
    # Parse the SVG file
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Retrieve width and height of the SVG
    width = float(root.attrib["width"].replace("pt", ""))
    height = float(root.attrib["height"].replace("pt", ""))

    # Update the width, height, and viewBox attributes
    trimmed_width = width * 0.7  # these multipliers can be adjusted as needed
    trimmed_height = height * 0.7

    root.attrib["width"] = f"{trimmed_width}pt"
    root.attrib["height"] = f"{trimmed_height}pt"
    root.attrib["viewBox"] = f"0 0 {trimmed_width} {trimmed_height}"

    # Write the changes back to the SVG file
    tree.write(svg_path)

if __name__ == "__main__":
    # Call after converting PDF to SVG
    trim_svg_whitespace(os.path.join(PATH, "sheet.svg"))
