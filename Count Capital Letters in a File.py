import string

with open("text.txt") as file:
    total_count = 0
    upper_count = 0
    lower_count = 0
    digit_count = 0
    punctuation_count = 0
    text = file.read()

    for char in text:
        total_count += 1
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in string.punctuation:
            punctuation_count += 1

    print(f"Total characters: {total_count}")
    print(f"Uppercase characters: {upper_count}")
    print(f"Lowercase characters: {lower_count}")
    print(f"Digits: {digit_count}")
    print(f"Punctuation: {punctuation_count}")