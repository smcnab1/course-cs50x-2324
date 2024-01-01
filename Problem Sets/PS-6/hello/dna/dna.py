import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    database_filename = sys.argv[1]
    database = read_database(database_filename)

    # Read DNA sequence file into a variable
    sequence_filename = sys.argv[2]
    dna_sequence = read_dna_sequence(sequence_filename)

    # Find longest match of each STR in DNA sequence
    match_counts = find_str_counts(dna_sequence, database)

    # Check database for matching profiles
    match = find_matching_profile(match_counts, database)

    if match:
        print(match)
    else:
        print("No match")


def read_database(filename):
    """Reads the CSV database file and returns it as a list of dictionaries."""
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_dna_sequence(filename):
    """Reads the DNA sequence file and returns it as a string."""
    with open(filename) as file:
        return file.read().strip()


def find_str_counts(sequence, database):
    """Finds the longest match of each STR in the DNA sequence."""
    str_counts = {}
    for header in database[0].keys():
        if header != "name":
            str_counts[header] = longest_match(sequence, header)
    return str_counts


def find_matching_profile(match_counts, database):
    """Checks the database for matching profiles."""
    for profile in database:
        if all(
            int(profile[str_name]) == int(str_count)
            for str_name, str_count in match_counts.items()
        ):
            return profile["name"]
    return None


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to the next potential match in the sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in the sequence, return the longest run found
    return longest_run


if __name__ == "__main__":
    main()
