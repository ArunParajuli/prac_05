"""
CP1404 Practical
Name: Arun Parajuli
"""
# Define constants for file name and indices of country and champion columns
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    """Reads the data file and prints details about Wimbledon champions and countries."""
    # Get records from the data file
    records = get_records(FILENAME)
    # Process records to extract champions and countries
    champion_to_count, countries = process_records(records)
    # Display results of champions and countries
    display_results(champion_to_count, countries)

def process_records(records):
    """Creates a dictionary of champions and a set of countries from records (a list of lists)."""
    # Initialize an empty dictionary to store champions and their win counts
    champion_to_count = {}
    # Initialize an empty set to store unique countries
    countries = set()
    # Iterate over each record in the list of records
    for record in records:
        # Add the country to the set of countries
        countries.add(record[INDEX_COUNTRY])
        # Try to increment the win count for the champion in the dictionary
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        # If the champion is not found in the dictionary, create a new entry with win count 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    # Return the dictionary of champions and their win counts, and the set of countries
    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Displays champions and countries."""
    # Print the champions and their win counts
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    # Print the countries in alphabetical order
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))

def get_records(filename):
    """Gets records from a file and returns them as a list of lists."""
    # Initialize an empty list to store records
    records = []
    # Open the file and read its contents
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        # Iterate over each line in the file
        for line in in_file:
            # Split the line into parts using comma as delimiter and append to records
            parts = line.strip().split(",")
            records.append(parts)
    # Return the list of records
    return records

# Call the main function to start the program
main()
