import string

WORD = 'refrigerator'

WORD_LIST = ['' for i in range(len(WORD))]
#print WORD_LIST


def get_input():
    let = raw_input("Please guess a letter: ")
    let = let.upper()
    if len(let) > 1:
        print "This is not letter!"
        return get_input()
    elif let not in string.ascii_letters:
        print "Please enter a letter!"
        return get_input()
    return let


def update_char(char, word, char_list, wrong_char_list):

    if char not in word:
        if char not in wrong_char_list:
            wrong_char_list.append(char)
        else:
            raise ValueError
    else:
        if char not in char_list:
            for index, c in enumerate(word):
                if c == char:
                    char_list[index] = char
        else:
            raise ValueError

    return char_list, wrong_char_list


def run_game():
    pass


if __name__ == "__main__":
    #run_game()
    #get_input()
    print update_char('r', 'tree', ['', '', 'e', ''], [''])
