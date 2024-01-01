from cs50 import get_string


def count_letters(text):
    return sum(c.isalpha() for c in text)


def count_words(text):
    return len(text.split())


def count_sentences(text):
    return text.count(".") + text.count("!") + text.count("?")


def coleman_liau_index(letters, words, sentences):
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)


def main():
    # Prompt user for text
    text = get_string("Text: ")

    # Count letters, words, and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate Coleman-Liau index
    index = coleman_liau_index(letters, words, sentences)

    # Determine and print the grade level
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


if __name__ == "__main__":
    main()
