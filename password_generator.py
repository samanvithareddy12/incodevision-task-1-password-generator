import secrets
import string


def display_title():
    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)
    print("Generate a strong random password!\n")


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))

            if length <= 0:
                print("Password length must be greater than zero.")
            else:
                return length

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def generate_password(length):
    # Collect letters, numbers, and symbols
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # Combine all available characters
    all_characters = letters + numbers + symbols

    # Ensure the password includes a letter, a number,
    # and a symbol whenever the requested length permits
    password_characters = []

    if length >= 3:
        password_characters.append(secrets.choice(letters))
        password_characters.append(secrets.choice(numbers))
        password_characters.append(secrets.choice(symbols))

        # Generate the remaining characters using a loop
        for _ in range(length - 3):
            character = secrets.choice(all_characters)
            password_characters.append(character)

    else:
        # For lengths below 3, select from all character types
        for _ in range(length):
            character = secrets.choice(all_characters)
            password_characters.append(character)

    # Randomize the positions of the selected characters
    secrets.SystemRandom().shuffle(password_characters)

    # Convert the character list into a string
    password = "".join(password_characters)

    return password


def main():
    display_title()

    length = get_password_length()

    password = generate_password(length)

    print("\n" + "-" * 40)
    print("Your generated password is:")
    print(password)
    print("-" * 40)
    print("Password length:", len(password))


# Start the program
if __name__ == "__main__":
    main()