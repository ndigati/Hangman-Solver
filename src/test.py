import random


def makedict(filename):
    """
    Makes the given txt file of english words into a dictionary for easy
    use in python.
    Sorted by their lengths.
    :param filename: .txt file of english words
    :return: dictionary, d, of all words grouped by length.
    """
    d = {}
    with open(filename, 'r') as file:
        for line in file:
            l = line.rstrip()
            if len(l) not in d:
                d[len(l)] = [l]
            else:
                d[len(l)].append(l)
    return d


def find_word(letters, length, dictionary):
    """
    Return a list of possible solution words given the letters and length
    
    :param letters: tupules of already known letters
    :param length: length of solution word
    :param dictionary:  dictionary of possible words
    :return: possible_words: list of possible solution words
    """
    
    possible_words = []
    same_length_words = dictionary[length]
    for pair in letters:
        if len(possible_words) == 0:
            for word in same_length_words:
                if word[int(pair[1]) - 1].count(pair[0]):
                    possible_words.append(word)
                elif word in possible_words:
                    possible_words.remove(word)
        else:
            possible_words = [word for word in possible_words
                              if word[int(pair[1]) - 1].count(pair[0])]

    return possible_words


def ask_for_word():
    """
    Function to ask the user for the information they know about the work.

    Asks for letters and their position in the solution word.

    Makes these pairs into tuples (letter, position) for easy access to
    needed information.
    :return: list of tuples and the length of the solution word
    """
    word = input("What letters do you have? Separate pairs by spaces "
                 "(EX: a2 {LetterPosition}): ")
    tuples = []
    word = word.split(sep=' ')
    for pair in word:
        # if the position was a 2 digit number using just pair[0] and pair[1]
        # wouldn't get the whole number so have to use pair[1:]
        # if the position is only 1 digit (1-9) just make the pair a tupule
        if len(pair) >= 3:
            tup = (pair[0], pair[1:])
            tuples.append(tup)
        else:
            tuples.append(tuple(pair))
    length = int(input("How long is the word you are looking for: "))
    return tuples, length


def main():
    # used to print information to the user with 0 being the default case of
    # printing all possible options to the user.
    choice = 0

    # makes the list of english words a dictionary sorted by length.
    # used for easy filtering by length of the solution word.
    dictionary = makedict('wordsEn.txt')

    letters, length = ask_for_word()
    possibles = find_word(letters, length, dictionary)

    # print possible solution(s) to the user depending on how many are found.
    if len(possibles) == 1:
        print("The word is: ", possibles[0])
        choice = 3
    else:
        print("A possible word is: ", random.choice(possibles))
    while choice != 3:
        if choice == 0:
            print("If you would like another guess type 1.\n"
                  "If you would like the full list type 2 (May be long list).\n"
                  "If you would like to quit type 3.\n")
        elif choice == 1:
            print("Another possible word is: ", random.choice(possibles))
        elif choice == 2:
            print("Here you go: \n", possibles)

        choice = int(input())

    print("Thank you! :D")

    """Used to make the dictionary into a JSON file, to make sure all
    words were in the dictionary before moving on and sorting by length.
    May be used later on for other things.
    Only used for debugging and ensuring the output lists had all possible
    length words.
    Produced jsonDictionary.txt file.

    with open('jsonDictionary.txt', 'w') as file:
         file.write(json.JSONEncoder(indent=2).encode(dictionary))
    """

if __name__ == '__main__':
    main()
