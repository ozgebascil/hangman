import string

WORD = 'refrigerator'

WORD_LIST = ['' for i in range(len(WORD))]
#print WORD_LIST
E = '_'


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

    if char not in word.upper():
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


def print_table(char_list, wrong_char_list, lives_left):
    print " ".join(char_list)
    print "You have guessed these letters incorrectly: %s " % ", ".join(wrong_char_list)
    print "You have %s lives left" % lives_left


def run_game(word, char_list, wrong_char_list, lives_left):
    print_table(char_list, wrong_char_list, lives_left)
    if not lives_left:
        print "You ran out of lives"
    elif word.upper() == ''.join(char_list):
        print "You win!"
    else:
        char = get_input()
        try:
            c_list, w_char_list = update_char(char, word, char_list, wrong_char_list)
        except ValueError:
            print "You have already guessed this letter! %s" % char
            return run_game(word, char_list, wrong_char_list, lives_left)
        else:
            if len(c_list) == len(char_list):
                lives_left -= 1

            return run_game(word, char_list, wrong_char_list, lives_left)







if __name__ == "__main__":
    #run_game()
    #get_input()
    #print update_char('r', 'tree', ['', '', 'e', ''], [''])
    #print_table([E, E, 'e', 'e'], ['f', 'g'], 5)
    run_game('tree', [E, E, E, E], [], 6)
