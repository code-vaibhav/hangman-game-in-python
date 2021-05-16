import random
import string

WORDLIST_FILENAME = "words.txt"

def add_word(trie, word):
    curr = trie
    for l in word:
        if l not in curr:
          curr[l] = dict()
        curr = curr[l]


def create_trie(word_list):
    trie = dict()
    for word in word_list:
      curr = trie
      for l in word:
        if l not in curr:
          curr[l] = dict()
        curr = curr[l]

    return trie

def in_trie(trie, word):
    curr = trie
    for l in word:
      if l in curr:
        curr = curr[l]
      else:
        return False
    if(bool(curr)):
      return False
    return True 

def list_matches(trie, prefix):
    curr = trie
    for l in prefix:
      if l in curr:
        curr = curr[l]
      else: 
        return []
    
    words = []


def load_words():
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):

    for l in secret_word:
      if l not in letters_guessed:
        return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    
    word = secret_word[:]
    for l in secret_word:
      if l not in letters_guessed:
        word = word.replace(l, '_ ', 1)
    return word


def get_available_letters(letters_guessed):
    
    available_letters = string.ascii_lowercase
    for l in letters_guessed:
      available_letters = available_letters.replace(l, '')
    return available_letters


def hangman(secret_word):
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have 3 warnings left.')

    guess = 6
    warning = 3
    letters_guessed = []
    
    while guess:
      print('-----------------------------------')
      if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        print('Your total score for this game is', guess*len(set(secret_word)))
        return
      print('You have', guess, 'guesses left.')
      print('Availbale letters:', get_available_letters(letters_guessed))
      letter = input('Please guess a letter: ').lower()
      if letter.isalpha():
        if letter in letters_guessed:
          if warning:
            warning -= 1
            print('Oops! You\'ve already guessed that letter. You now have', warning ,'warnings :', get_guessed_word(secret_word, letters_guessed))
          else:
            guess -= 1
            print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose a guess:', get_guessed_word(secret_word, letters_guessed))
        else:
          letters_guessed.append(letter)
          if letter in secret_word:
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
          else:
            if letter in ['a', 'e', 'i', 'o', 'u']:
              guess -= 2
            else:
              guess -= 1 
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
      else:
        if warning:
          warning -= 1
          print('Oops! That is not a valid letter. You now have', warning ,'warnings left:', get_guessed_word(secret_word, letters_guessed))
        else:
          guess -= 1
          print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:', get_guessed_word(secret_word, letters_guessed))

    print('-----------------------------------')
    print('Sorry, you ran out of guesses. The word was', secret_word,'.')
    return


def match_with_gaps(my_word, other_word):
    
    word = my_word[:]
    word = "".join(word.split())
    if len(word) == len(other_word):
      pos = 0
      for l in word:
        if l != '_' and other_word.find(l, pos) != word.find(l, pos):
          return False
        pos += 1
      return True
    else:
      return False


def show_possible_matches(my_word):
    
    found_words = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        found_words.append(word)
    
    if len(found_words):
      for word in found_words:
        print(word, end='\t')
    else:
      print('No matches found')
    
    print('\n')


def hangman_with_hints(secret_word):
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have 3 warnings left.')

    guess = 6
    warning = 3
    letters_guessed = []
    
    while guess:
      print('-----------------------------------')
      if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        print('Your total score for this game is', guess*len(set(secret_word)))
        return
      print('You have', guess, 'guesses left.')
      print('Availbale letters:', get_available_letters(letters_guessed))
      letter = input('Please guess a letter: ').lower()
      if letter.isalpha():
        if letter in letters_guessed:
          if warning:
            warning -= 1
            print('Oops! You\'ve already guessed that letter. You now have', warning ,'warnings :', get_guessed_word(secret_word, letters_guessed))
          else:
            guess -= 1
            print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose a guess:', get_guessed_word(secret_word, letters_guessed))
        else:
          letters_guessed.append(letter)
          if letter in secret_word:
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
          else:
            if letter in ['a', 'e', 'i', 'o', 'u']:
              guess -= 2
            else:
              guess -= 1 
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
      elif letter == '*':
        print('Possible word matches are:')
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      else:
        if warning:
          warning -= 1
          print('Oops! That is not a valid letter. You now have', warning ,'warnings left:', get_guessed_word(secret_word, letters_guessed))
        else:
          guess -= 1
          print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:', get_guessed_word(secret_word, letters_guessed))

    print('-----------------------------------')
    print('Sorry, you ran out of guesses. The word was', secret_word,'.')
    return


if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    # hangman(secret_word)
    
    hangman_with_hints(secret_word)