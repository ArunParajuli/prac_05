"""
CP1404 Practical
Name: Arun Parajuli
"""

# Define a dictionary to store Australian state abbreviations and their corresponding full names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Print the dictionary containing state abbreviations and names
print(CODE_TO_NAME)


def main():
    # Ask the user to enter a state abbreviation
    state_code = input("Enter short state: ").upper()  # Convert input to uppercase
    # Continue asking for state abbreviation until the user enters a blank line
    while state_code != "":
        try:
            # Try to find the corresponding full name of the state abbreviation
            state_name = CODE_TO_NAME[state_code]
            # Print the abbreviation and full name of the state
            print(f"{state_code} is {state_name}")
        except KeyError:
            # If the abbreviation is not found in the dictionary, inform the user
            print("Invalid short state")

        # Ask the user to enter another state abbreviation
        state_code = input("Enter short state: ").upper()


if __name__ == "__main__":
    main()
