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
    return str(rd.randint(0,999))

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
                return n 
        cont += 1
        clear_screen()

def guess_number(guess: str, number:str):
    '''
    
    '''
    win = 0
    pico = [0, 0, 0]
    ferm = [0, 0, 0]
    bage = [0, 0, 0]
    for i in range(3):
        if guess[i] == number[i]:
            bage[i] = 1
            win += 1
        elif guess[i] in number:
            ferm[i] = 1
        else:
            pico[i] = 1
    
    if win == 3:
        return 1, []
    
    


if __name__ == '__main__':
    eng_text = {
        'wrong_c':'Option not available, please type again your choice.\n',
        'title':'Bagels, a deductive logic game.\n\n',
        'rules_t':'RULES\n-----\nWhen I say:    That means:',
        'rules_1':'  Pico         One digit is correct, but in the wrong position.',
        'rules_2':'  Fermi        One digit is correct and in the right position.',
        'rules_3':'  Bagels       No digit is correct.\n',
        'play':'Play? (y/n):',
        'play_o':['y', 'n'],
        'ini':'I am thinking of a 3-digit number. Try to guess what it is.\nYou have 10 guesses to get it.',
        'end':'Bye!',
        'guess':'Guess ',
        'w_numb':'The number you guess must be between 0 and 999.\nGuess another number: '
    }
    esp_text = {
        'wrong_c':'Opción no disponible, ingrese su elección nuevamente.\n',
        'title':'Bagels, un juego de lógica deductivo.\n\n',
        'rules_t':'REGLAS\n------\nCuando digo:   Significa:',
        'rules_1':'  Pico         Un dígito es correcto, pero en la posición incorrecta.',
        'rules_2':'  Fermi        Un dígito es correcto y en la posición correcta.',
        'rules_3':'  Bagels       Ningún dígito es correcto.\n',
        'play':'Jugar? (s/n):',
        'play_o':['s', 'n'],
        'ini':'Estoy pensando un número de 3 dígitos. Intenta adivinar cuál es.\nTienes 10 Oportunidades.',
        'end':'Adiós!',
        'guess':'Oportunidad ',
        'w_numb':'El número que proporcione debe estar entre 0 y 999.\nIngrese otro número: '
    }
    text = [eng_text, esp_text]

    clear_screen()

    lang = int(get_choice(['1', '2'], 'Press 1 for english.\nPresione 2 para español.\n-> ', text[0]['wrong_c'])) - 1

    clear_screen()

    print(text[lang]['title'])
    print(text[lang]['rules_t'])
    print(text[lang]['rules_1'])
    print(text[lang]['rules_2'])
    print(text[lang]['rules_3'])

    ini = get_choice(text[lang]['play_o'], text[lang]['play'], text[lang]['wrong_c'])

    if ini == 'y':
        my_num = gen_number()
        print(text[lang]['ini'])
        for i in range(10):
            resp = input(text[lang]['guess'],i+1)
            ok = True
            while(ok):
                if int(resp) > 999:
                    resp = input(text[lang]['w_numb'])
                else:
                    ok = False
            


    print(text[lang]['end'])