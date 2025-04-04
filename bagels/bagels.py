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

if __name__ == '__main__':
    available_lang = 2
    eng_text = {
        'wrong_c':'Option not available, please type again your choice.\n',
        'title':'Bagels, a deductive logic game.\n\n',
        'rules_t':'Rules:\nWhen I say:    That means:',
        'rules_1':'  Pico         One digit is correct, but in the wrong position.',
        'rules_2':'  Fermi        One digit is correct and in the right position.',
        'rules_3':'  Bagels       No digit is correct.\n',
        'play':'Play? (y/n):',
        'ini':'I am thinking of a 3-digit number. Try to guess what it is'
    }
    esp_text = {
        'wrong_c':'Opción no disponible, ingrese su elección nuevamente.\n',
        'title':'Bagels, un juego de lógica deductivo.\n\n',
        'rules_t':'Reglas:\nCuando digo:   Significa:',
        'rules_1':'  Pico         Un dígito es correcto, pero en la posición incorrecta.',
        'rules_2':'  Fermi        Un dígito es correcto y en la posición correcta.',
        'rules_3':'  Bagels       Ningún dígito es correcto.\n',
        'play':'Jugar? (y/n):',
        'ini':'Estoy pensando un número de 3 dígitos. Intenta adivinar cuál es'
    }
    text = [eng_text, esp_text]

    clear_screen()

    cont = 0
    lang = 0
    while(True):
        if cont > 0:
            for i in range(available_lang):
                print(text[i]['wrong_c'])
        print(17*'-')
        resp = input('Press 1 for english.\nPresione 2 para español.\n-> ')
        if resp.strip() == '1' or resp.strip() == '2':
            lang = int(resp) - 1
            cont = 0
            break
        cont += 1
        clear_screen()

    clear_screen()

    print(text[lang]['title'])
    print(text[lang]['rules_t'])
    print(text[lang]['rules_1'])
    print(text[lang]['rules_2'])
    print(text[lang]['rules_3'])

    while(True):
        resp = input(text[lang]['play'])
        if resp.lower().strip() == 'y' or resp.lower().strip() == 'n':
            pass
    #print(gen_number())