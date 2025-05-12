import random
import string

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = letters + digits + symbols

    # Make sure the password contains at least one character from each set
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(16))
