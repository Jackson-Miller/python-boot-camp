import pandas

# Import CSV and create a dictionary with dictionary comprehension
csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}


# Create a list with the phonetic name using list comprehension
def main():
    word = input("Enter a word: ").upper()
    try:
        phonetic_name = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Please enter a word, numbers are not accepted.")
        main()
    else:
        print(phonetic_name)


main()
