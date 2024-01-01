def get_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid integer.")

def is_valid(card_number):
    # Check if the card number is valid using Luhn's Algorithm
    digits = [int(digit) for digit in card_number]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        digits[i] = sum(divmod(digits[i], 10))
    return sum(digits) % 10 == 0

def card_type(card_number):
    if is_valid(card_number):
        length = len(card_number)
        start_digit = int(card_number[0])

        if (length == 13 or length == 16) and start_digit == 4:
            return "VISA"
        elif length == 15 and (start_digit == 3 and (int(card_number[1]) == 4 or int(card_number[1]) == 7)):
            return "AMEX"
        elif length == 16 and start_digit == 5 and 1 <= int(card_number[1]) <= 5:
            return "MASTERCARD"

    return "INVALID"

# Prompt user for the credit card number
card_number = str(get_int("Enter your credit card number: "))

# Check the card type and print the result
card_type_result = card_type(card_number)
print(card_type_result)
