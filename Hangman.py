import random, os # importing libraries...
os.system ("color") # now text can be printed in colors!
def welcome_screen():
    """
    this function prints the welcome screen in random color
    """
    HANGMAN_ASCII_ART = """Welcome to my game!
      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/

    """
    color = random.randint(31,37) #Random color that the welcome screen is printed in.
    print(f"\033[{color};1;1m" , HANGMAN_ASCII_ART, "6", "\033[0m") #Print the welcome screen


def choose_word(file_path, index):
    """this function choose the secret word according to the params file_path and index
    : param file_path : words file
    : param index : the place of the wanted word in the file
    : type file_path : file
    : type index : integer
    : return: secret_word
    : Note: the file must be a text file and between every two words there must be a space
    """
    file_path = file_path.encode("ascii", "ignore")
    file_path = file_path.decode()
    file_path = open(file_path) #Open the words file
    read_file = file_path.read()
    read_file = read_file.split() #List of all the words in the file
    index = abs(int(index)) - 1 #Index in python language (starts with 0, not 1)
    index = index - ((index//len(read_file))*len(read_file)) #To make index smaller / equal to the file length
    secret_word = read_file[index].strip(",") #Finally, choose the secret word!
    return secret_word #Return the secret word to be used in the rest of the game
    file_path.close() #Close the file (important!)


HANGMAN_PHOTOS = { #Will be used in print_hangman function
    0 :
    """    x-------x"""
    ,
    1:
    """    x-------x
     |
     |
     |
     |
     |

    """
    ,
    2 :
    """    x-------x
     |       |
     |       0
     |
     |
     |

    """
    ,
    3:
    """    x-------x
     |       |
     |       0
     |       |
     |
     |
        """
    ,
    4:
    """    x-------x
     |       |
     |       0
     |      /|\\
     |
     |

"""
,
    5:
    """    x-------x
     |       |
     |       0
     |      /|\\
     |      /
     |

    """
    ,
    6:
    """    x-------x
     |       |
     |       0
     |      /|\\
     |      / \\
     |
    """
    }
def print_hangman(num_of_tries):
    """this function prints the current hangman according to the wrong guesses that the user made in random color
    : param num_of_tries : number of wrong guesses
    : type num_of_tries : integer
    : return: None
    """
    color = random.randint(31,37) #Random color that the poor hangman will be printed in.
    try:
        print(f"\033[{color};1;1m" , HANGMAN_PHOTOS[int(num_of_tries)], "\033[0m") #Print the hangman
    except:
        lose = True #This will make the game stop


def show_hidden_word(secret_word, old_letters_guessed):
    """
    this function print the word in letters and '_' like in hangman games,
    and that's according to the word and the letters that the user already guessed
    : param secret_word : the secret word (that the user have to guess)
    : param old_letters_guessed : all letters that the user guessed before
    : type secret_word : string
    : type old_letters_guessed : list
    : return: None
    """
    show_word = [] #In the near future it will be filled with letters and underscores!
    for letter in secret_word: #This loop is that one who will fill the show_word list!
        if letter in old_letters_guessed:
            for character in old_letters_guessed:
                if character == letter:
                    show_word += [letter]
        else:
             show_word += "_"
    show_word = " ".join(show_word) #Casting show_word to string
    print(show_word)

def check_win(secret_word, old_letters_guessed):
    """
    this function checks if the user win the game (guessed the secret word)
    : param secret_word : the secret word (that the user have to guess)
    : param old_letters_guessed : all letters that the user guessed before
    : type secret_word : string
    : type old_letters_guessed : list
    : return: True if the user win the game, False otherwise
    """
    guessed_letters = 0
    checked_letters = [] #It will make sure no letters are repeated
    for letter in old_letters_guessed: #Will count the correct letters that the user guessed and in the right amount
        if letter in secret_word and not letter in checked_letters:
            guessed_letters = guessed_letters + secret_word.count(letter)
            checked_letters += [letter]
    return guessed_letters == len(secret_word)


def is_valid_input(letter_guessed, old_letters_guessed):
    """this function checks if the user's input is one English letter.
    : param letter_guessed : the letter that the user guessed
    : param old_letters_guessed : all letters that the user guessed before
    : type letter_guessed : string
    : type old_letters_guessed : list
    : return: if the user's input is an English letter, if the guessed letter isn't a letter that the user already guessed
    """
    letter_guessed = letter_guessed.lower() #No difference between capital and small letters
    letter_guessed = letter_guessed.replace(" ","") #Ignore spaces
    return len(letter_guessed) == 1 and letter_guessed.isalpha(), not(letter_guessed in old_letters_guessed)


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """this function adds the letters (only English letters) that the user guessed to the letters that the user guessed before
       prints feedback according to if the user's guess is an english letter and that it isn't guessed before
    : param letter_guessed : the letter that the user guessed
    : param old_letters_guessed : all letters that the user guessed before
    : type letter_guessed : string
    : type old_letters_guessed : list
    : return: old_letters_guessed, letter_guessed, check
    """
    check = False #For now the letter don't need to be checked if it's in the secret word
    letter_guessed = letter_guessed.lower()
    if is_valid_input(letter_guessed, old_letters_guessed)[0]: #Check if user's guess is one English letter
        if not(is_valid_input(letter_guessed, old_letters_guessed)[1]): #Check if it have been guessed before
            #If yes, print X and the letters that the user already guessed
            print("X")
            print(" -> ".join(sorted(old_letters_guessed)))
        else:
            #Finally! it's one English letter that haven't been guessed before!
            #It will be checked if it's correct in the hangman function...
            check = True
    else:
        #User's guess isn't one English letter, so X will be printed
        print("X")
    return sorted(old_letters_guessed), letter_guessed, check

def hangman(secret_word):
    """
    this function uses all the other functions to create an enjoyable and interactive hangman game!
    : param secret_word: the word that the user have to guess
    : type secret_word: string
    : return None
    """
    secret_word = secret_word.lower() #No difference between capital and small letters
    print("") #Blank line
    #Letters that the user guessed before, max number of tries, number of tries ,and if the user lost the game
    old_letters_guessed, MAX_TRIES, num_of_tries, lose = [], 6, 0, False
    print_hangman(num_of_tries)
    print("")
    show_hidden_word(secret_word, old_letters_guessed)
    while not lose: #This loop will end if the user lost or...
        if check_win(secret_word, old_letters_guessed) or num_of_tries >= MAX_TRIES:
            #if the user won or if the number of wrong guesses that the user guessed is bigger than the max number
            break
        #Update letters that the user guessed, the letter that they guesses, and if the letter should be checked
        old_letters_guessed, letter_guessed, to_check = try_update_letter_guessed(input("Guess a letter: "), old_letters_guessed)
        if to_check: #If the letter is one English letter and that it haven't been guessed before
            old_letters_guessed += letter_guessed #Add the letter to the letters that the user guessed before
            if not letter_guessed in secret_word: #Only if the letter isn't in the secret word
                num_of_tries += 1 #Add 1 to the number of the user's wrong guesses
                print(":(")
                print_hangman(num_of_tries)
            show_hidden_word(secret_word, old_letters_guessed)
    if check_win(secret_word, old_letters_guessed): # Check if the user won
        print("Win!") #They did :)
    else:
        print("Lose!")
        print("the word is", secret_word)

def main():
    welcome_screen() #Print the welcome screen
    secret_word = choose_word(input("Enter the words file path: ").strip('"'), input("Enter the place of the word: "))
    hangman(secret_word) #And start the game!

if __name__ == "__main__":
    main()
