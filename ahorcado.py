import random
from words import words_list

def get_word():
    word = random.choice(words_list)
    return word.upper()

def print_ahorcado_foo(hidden_word, hits, mistakes, not_guessed_letters):
    print('Palabra a adivinar: ', hidden_word, 'Aciertos:', hits, 'Desaciertos:', mistakes, '-'.join(not_guessed_letters))
    print('\n') 

def should_user_keep_playing(is_guessed, tries):
    return is_guessed and tries > 0

def check_if_word_is_allowed(word):
    return len(word) == 1 and word.isalpha()

def play(word):
    hidden_word = '?' * len(word)
    is_guessed = False
    guessed_letters = []
    not_guessed_letters = []
    hits = 0
    mistakes = 0
    tries = 7

    print_ahorcado_foo(hidden_word, hits, mistakes, not_guessed_letters)

    while not should_user_keep_playing(is_guessed, tries):
        guess = input('Ingrese letra: ').upper()

        if check_if_word_is_allowed(guess):
            check_user_guess_already_exist = guess in guessed_letters or guess in not_guessed_letters
            check_user_guess_is_not_in_word = guess not in word
            check_hidden_word_is_complete = '?' not in hidden_word

            if check_user_guess_already_exist:
                print('La letra ', guess, 'ya ha sido ingresada anteriormente.')
            elif check_user_guess_is_not_in_word:
                print('La letra ', guess, 'no se encuentra dentro de la palabra.')
                tries -= 1
                mistakes += 1
                not_guessed_letters.append(guess)
            else:
                print('Eres un capo! La letra ', guess, 'está dentro de la palabra')
                hits += 1
                guessed_letters.append(guess)
                word_as_list = [letter if letter in guessed_letters else '?' for letter in word]
                hidden_word = ''.join(word_as_list)

                if check_hidden_word_is_complete:
                    is_guessed = True

        else:
            print('El valor ingresado no es válido')
            tries -= 1
            mistakes += 1


        print_ahorcado_foo(hidden_word, hits, mistakes, not_guessed_letters)

    if is_guessed:
        print('Felicitaciones! Has adivinado la palabra :D.')
    else:
        print('Lo lamento, te has quedado sin intentos. La palabra era ' + word + ' :(.')
    

def main():
    word = get_word()

    print('Bienvenido al Juego del Ahorcado!')

    play(word)
    while input('Quieres jugar de nuevo? (Y/N)').upper() == 'Y':
        word = get_word()
        play(word)
    

if __name__ == '__main__':
    main()