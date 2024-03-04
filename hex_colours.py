"""
CP1404 Practical
Name: Arun Parajuli
"""
# Define a list of color names and their hexadecimal codes
COLOR_CODES = {
    "ALICEBLUE": "#F0F8FF",        # Light blue color
    "ANTIQUEWHITE": "#FAEBD7",     # Off-white color
    "AQUA": "#00FFFF",             # Bright cyan color
    "AZURE": "#F0FFFF",            # Pale blue color
    "BEIGE": "#F5F5DC",            # Creamy yellow-brown color
    "BISQUE": "#FFE4C4",           # Pale orange color
    "BLACK": "#000000",            # Pure black color
    "BLANCHEDALMOND": "#FFEBCD",   # Pale yellow color
    "BLUE": "#0000FF",             # Pure blue color
    "BLUEVIOLET": "#8A2BE2"        # Purple color
}

# Function to find the hexadecimal code of a color name
def lookup_color(color_name):
    # Check if the color name is in the list
    # If found, return its hexadecimal code
    # If not found, return "Unknown color"
    return COLOR_CODES.get(color_name.upper(), "Unknown color")

# Main function to interact with the user
def main():
    # Keep asking the user for a color name until they enter a blank line
    while True:
        # Get a color name input from the user
        color_name = input("Enter a color name (or blank to quit): ").strip()
        # If the input is blank, stop the loop
        if not color_name:
            break
        # Look up the hexadecimal code for the entered color name
        color_code = lookup_color(color_name)
        # Print the color name and its hexadecimal code
        print(f"{color_name.capitalize()}: {color_code}")

# Check if this script is run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to start the program
    main()
