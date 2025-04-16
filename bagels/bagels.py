import random as rd
import os
import platform

def clear_screen() -> None:
    '''
    Clears the terminal screen.
    '''
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  

def gen_number() -> str:
    '''
    Generates a random number between 0 and 999 and then transforms it to string

    Input:
    ------
    None.

    Output:
    -------
    A random number as string.
    '''
    numb = rd.randint(0,999)

    # make a function of this with a size of n 0
    if numb < 10:
        numb = '00' + str(numb)
    elif numb < 100:
        numb = '0' + str(numb)

    return numb

def get_choice(option: list, input_legend: str = 'Give me your choice: ', error_info: str='Choice not available.') -> str:
    '''
    Returns the choice user. It can be n options.
    
    Input:
    ------
    The option argument must be a list of strings. The input legend is the message delivered to the user to understand the available choices. 

    Output:
    -------
    Returns the option that the user choose as a string.
    '''
    n = len(option)
    cont = 0
    while(True):
        if cont > 0:
            print(error_info)
        print(17*'-')
        resp = input(input_legend).lower().strip()
        for i in range(n):
            if resp == option[i]:
                return resp
        cont += 1
        clear_screen()

def guess_number(guess: str, number:str):
    '''
    Verify if a string number matches a random number. It get hints if any number match or is in the string.
    
    Input:
    ------
    Recives two numbers of the same size.

    Output:
    -------
    Returns the type of guess and a list of hints. If the response is 1, then the number has been guessed, if is -1, non of the number is in the random number, 
    and if is zero, there are some matches.
    '''
    str_length = len(guess)
    if str_length != len(number):
        raise ValueError('Guess number must be the same length as hiden number')
    hints = []
    ferm_c = 0
    pico_c = 0
    for i in range(str_length):
        if guess[i] == number[i]:
            ferm_c += 1
        elif guess[i] in number:
            pico_c += 1
    
    if ferm_c == str_length:
        return 1, hints
    elif pico_c == 0 and ferm_c == 0:
        hints.append('Bagels')
        return -1, hints
    else:
        while(True):
            numb = rd.randint(0,1)
            if numb == 1 and pico_c > 0:
                hints.append('Pico')
                pico_c -= 1
            elif ferm_c > 0:
                hints.append('Fermi')
                ferm_c -= 1 
            elif ferm_c == 0 and pico_c == 0:
                break
        return 0, hints
    
if __name__ == '__main__':
    eng_text = {
        'wrong_c':'Option not available, please type again your choice.\n',
        'title':'Bagels, a deductive logic game.\n\n',
        'rules_t':'RULES\n-----\nWhen I say:    That means:',
        'rules_1':'  Pico         One digit is correct, but in the wrong position.',
        'rules_2':'  Fermi        One digit is correct and in the right position.',
        'rules_3':'  Bagels       No digit is correct.\n',
        'play':'Play? (y/n): ',
        'play_o':['y', 'n'],
        'ini':'I am thinking of a 3-digit number. Try to guess what it is.\nYou have 10 guesses to get it.',
        'end':'\nBye!',
        'guess':'Guess',
        'w_numb':'The number you guess must be between 0 and 999.\nGuess another number: ',
        'win':'You got it!',
        'play_a':'\nDo you want to play again? (y/n): ',
        'game_o':'\nGAME OVER :(',
        'numb':'The number I thought was '
    }
    esp_text = {
        'wrong_c':'Opción no disponible, ingrese su elección nuevamente.\n',
        'title':'Bagels, un juego de lógica deductivo.\n\n',
        'rules_t':'REGLAS\n------\nCuando digo:   Significa:',
        'rules_1':'  Pico         Un dígito es correcto, pero en la posición incorrecta.',
        'rules_2':'  Fermi        Un dígito es correcto y en la posición correcta.',
        'rules_3':'  Bagels       Ningún dígito es correcto.\n',
        'play':'Jugar? (s/n): ',
        'play_o':['s', 'n'],
        'ini':'Estoy pensando un número de 3 dígitos. Intenta adivinar cuál es.\nTienes 10 Oportunidades.',
        'end':'\nAdiós!',
        'guess':'Oportunidad',
        'w_numb':'El número que proporcione debe estar entre 0 y 999.\nIngrese otro número: ',
        'win':'Has encontrado el número!',
        'play_a':'\nQuieres jugar de nuevo? (s/n): ',
        'game_o':'\nPerdiste el juego :(',
        'numb':'El número que pensé fue el '
    }
    text = [eng_text, esp_text]
    rounds = 10

    clear_screen()

    lang = int(get_choice(['1', '2'], 'Press 1 for english.\nPresione 2 para español.\n-> ', text[0]['wrong_c'])) - 1

    clear_screen()

    print(text[lang]['title'])
    print(text[lang]['rules_t'])
    print(text[lang]['rules_1'])
    print(text[lang]['rules_2'])
    print(text[lang]['rules_3'])

    ini = get_choice(text[lang]['play_o'], text[lang]['play'], text[lang]['wrong_c'])

    if ini == text[lang]['play_o'][0]:
        matchs = 1
        while(matchs>0):
            matchs += 1
            if matchs > 2:
                resp = input(text[lang]['play_a'])
                if resp == text[lang]['play_o'][1]:
                    matchs = 0
                    break
                else:
                    clear_screen()
                    print(text[lang]['title'])
                    print(text[lang]['rules_t'])
                    print(text[lang]['rules_1'])
                    print(text[lang]['rules_2'])
                    print(text[lang]['rules_3'])
            my_numb = gen_number()
            print(text[lang]['ini'])
            for i in range(rounds):
                print(17*'-')
                print('>' + str(my_numb))
                msg = text[lang]['guess'] + " #" + str(i+1) + ": "
                resp = input(msg)
                ok = True
                while(ok):
                    if int(resp) > 999:
                        resp = input(text[lang]['w_numb'])
                    else:
                        ok = False

                if int(resp) < 10:
                    resp = '00' + str(int(resp))
                elif int(resp) < 100:
                    resp = '0' + str(int(resp))

                result, hints = guess_number(resp, str(my_numb))

                if result == 1:
                    print(text[lang]['win'])
                    break
                elif result == -1:
                    print('- ' + hints[0] + ' -')
                else:
                    print(hints)
                    print(end='- ')
                    for h in hints:
                        print(h, end=' - ')
            
            if i == rounds - 1:
                print(text[lang]['game_o'])
                print(text[lang]['numb'] + str(my_numb))


    print(text[lang]['end'])