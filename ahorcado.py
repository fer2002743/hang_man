import random
list_of_words = ['FERNANDO', 'ANTONIO', 'MESA'] #aqui creo que deberiamos añadir mas palabras

word = random.choice(list_of_words)
secret_word = '_' * len(word)
word = list(word)
secret_word = list(secret_word)



def play_again():
    decision = input('Do you want to play again: 1.YES 2.NO: ').upper()
    if decision == '1' or decision == 'YES':
        return True
    else:
        return False

def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]


def run():
    lives = 6
    counter = 0
    while lives > 0:
        counter = 0
        print(display_hangman(lives))
        letter = input('introduce a letter: ').upper()
        for element in word:
            if element == letter:
                secret_word[counter] = letter
                print(' '.join(secret_word))
            counter += 1
        if secret_word == word:
            break
        elif letter not in word:
            lives -= 1
            print(f'sorry, letter not in word, you have {lives} lives left')
    if lives > 0:
        print('Congratulation you have won')
    else:
        print('Sorry you have loose, maybe next time')

        
                




if __name__ == '__main__':
    run()
   #aqui intente dar al usuario la opcion de poder seguir jugando, pero no lo consegui 
    while play_again() == True:
        word = random.choice(list_of_words)
        secret_word = '_' * len(word)
        word = list(word)
        secret_word = list(secret_word)
        run()
    










#estas son pruebas para intentar validar el input, pero no tiene importancia

# def validate_input():
#     try:
#         letter = input('please choose a letter: ').upper()
#         assert letter.isalpha(), print('only letters are admited')
#         assert len(letter > 1), print('only one letter at each time')

#     except:
#         validate_input()



        #if validate_input() == True
        #guessed = False
