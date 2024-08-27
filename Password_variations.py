import random

# Function to substitute letters with numbers
def substitute_letters_with_numbers(word):
    substitutions = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
    for letter, number in substitutions.items():
        word = word.replace(letter, number)
    return word

# Function to generate password variations with substitutions
def generate_password_variations_with_substitution(word):
    variations = []

    # Original word
    variations.append(word)

    # All uppercase
    variations.append(word.upper())

    # All lowercase
    variations.append(word.lower())

    # Capitalize first letter
    variations.append(word.capitalize())

    # Reverse word
    variations.append(word[::-1])

    # Substitute letters with numbers
    variations.append(substitute_letters_with_numbers(word))

    # Add a random number at the end
    variations.append(word + str(random.randint(0, 9)))

    # Combine all transformations with substitution
    all_transformations_with_substitution = [
        word.upper(),
        word.lower(),
        word.capitalize(),
        word[::-1],
        substitute_letters_with_numbers(word),
        word + str(random.randint(0, 9))
    ]
    variations.append(','.join(all_transformations_with_substitution))

    return variations

# Main program
if __name__ == "__main__":
    input_word = input("Enter a word: ")

    password_variations = generate_password_variations_with_substitution(input_word)

    print("\nPassword Variations:")
    for variation in password_variations:
        print(variation)
