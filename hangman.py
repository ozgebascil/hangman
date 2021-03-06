import string
import random

E = '_'


def read_words():
    with open('words.txt', 'r') as content_file:
        content = content_file.read()
        content = content.split()
        return content


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
    c_list = char_list[:]
    w_char_list = wrong_char_list[:]

    char = char.upper()
    word = word.upper()

    if char not in word:
        if char not in w_char_list:
            w_char_list.append(char)
        else:
            raise ValueError
    else:
        if char not in c_list:
            for index, c in enumerate(word):
                if c == char:
                    c_list[index] = char
        else:
            raise ValueError

    return c_list, w_char_list


def print_table(char_list, wrong_char_list, lives_left):
    print " ".join(char_list)
    if wrong_char_list:
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
            if len(w_char_list) != len(wrong_char_list):
                lives_left -= 1
            return run_game(word, c_list, w_char_list, lives_left)


if __name__ == "__main__":
    word = random.choice(read_words())
    run_game(word, [E for i in range(len(word))], [], 6)
