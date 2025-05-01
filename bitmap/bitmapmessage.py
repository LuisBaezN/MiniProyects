import sys
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

def main():
    bitmap = '''
    .........................................
    
                     ***
                     *****
                      ****
                       ***
                       ***
                       ***
                       ***
                       ***
                       ***
                       ***
                       ***
                       ***
                       ***
                       ***
                      *****
                    *********
                  ***  ***  ***
                ***    ***    ***
              ***      ***      ***
                ***    ***    ***
                  ***  ***   ***
                    *  ***   *
                        *
                       ***
                        *

    .........................................
    '''
    eng_text = {
        'wrong_c':'Option not available, please type again your choice.\n',
        'title':'Bitmap Message.\n\n',
        'input':'Enter the message to display with the bitmap.\n > ',
    }
    esp_text = {
        'wrong_c':'Opción no disponible, ingrese su elección nuevamente.\n',
        'title':'Mensaje Bitmap.\n\n',
        'input':'Ingrese el mensaje a desplegar con el bitmap.\n > ',
    }
    text = [eng_text, esp_text]

    clear_screen()

    lang = int(get_choice(['1', '2'], 'Press 1 for english.\nPresione 2 para español.\n-> ', text[0]['wrong_c'])) - 1

    clear_screen()

    print(text[lang]['title'])
    message = input(text[lang]['input'])

    if message == '':
        sys.exit()

    len_mess = len(message)
    for line in bitmap.splitlines():
        for i, bit in enumerate(line):
            if bit == ' ':
                print(' ', end='')
            else:
                print(message[i % len_mess], end='')
        print()

if __name__ == '__main__':
    main()