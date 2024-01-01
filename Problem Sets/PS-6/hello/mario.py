def get_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if 1 <= user_input <= 8:
                return user_input
            else:
                print("Please enter a positive integer between 1 and 8, inclusive.")
        except ValueError:
            print("Please enter a valid integer.")


def print_half_pyramids(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        hashes_left = "#" * i
        gap = " " * 2
        hashes_right = "#" * i
        print(f"{spaces}{hashes_left}{gap}{hashes_right}")


# Prompt user for the half-pyramid's height
height = get_int("Enter the height of the half-pyramids (1-8): ")

# Generate and print the half-pyramids
print_half_pyramids(height)
