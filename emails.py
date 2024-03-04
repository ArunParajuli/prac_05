"""
CP1404 Practical
Name: Arun Parajuli
"""
def extract_name(email):
    # Splitting the email address at the '@' symbol and taking the part before it as the name
    name = email.split('@')[0]
    # Capitalizing the first letter of each word in the name
    name = name.title()
    return name


def main():
    # Dictionary to store email-name pairs
    user_info = {}

    # Keep asking the user for email addresses until they enter a blank one
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        # Extract the name from the email address
        name = extract_name(email)
        # Ask the user to confirm if the extracted name is correct
        confirm_name = input(f"Is your name {name}? (Y/n) ").strip().lower()
        # If the user confirms or presses Enter, continue; otherwise, ask for the correct name
        if confirm_name == '' or confirm_name == 'y':
            pass
        else:
            name = input("Name: ").strip()
        # Store the email and name in the dictionary
        user_info[email] = name

    # Print the collected email-name pairs
    print("\nName - Email")
    for email, name in user_info.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
