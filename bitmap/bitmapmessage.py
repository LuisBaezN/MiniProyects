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
        'title':'Birthday paradox.\n\nThe Birthday Pradox shows us that in agroup of N people, the odds that two of them have matching birthdays is surprisingly large.\n\n(It is not actually a paradox, it is just a surprising result)',
        'input':'How many birthdays shall I generate? (Max 100) \n > ',
    }
    esp_text = {
        'wrong_c':'Opción no disponible, ingrese su elección nuevamente.\n',
        'title':'Paradoja del cumpleaños.\n\nLa paradoja del cumpleaños muestra que dentro de un grupo de N personas, las probabilidades de que dos de ellas cumplan años el mismo día es sorpresivamente alta.\n\n(Actualmente no es una paradoja, solo un resultado sorprendente)',
        'input':'Cuántos cumpleaños debería generar? (Max 100) \n > ',
    }
    text = [eng_text, esp_text]

    clear_screen()

if __name__ == '__main__':
    main()