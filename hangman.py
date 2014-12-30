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


def run_game():
    pass


if __name__ == "__main__":
    #run_game()
    get_input()
