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

def generate_birthdays(num: int) -> list:
    '''
    Generate a n number of birthdays.

    Input:
    ------
    An integer that indicates the number of birthdays to generate.
    
    Output:
    -------
    Returns 2 list of days and months.
    '''
    months = []
    days = []
    for _ in range(num):
        month = rd.randint(1,12)
        if month == 2:
            day = rd.randint(1,28)
        elif month == 4 or 6 or 9 or 11:
            day = rd.randint(1,30)
        else:
            day = rd.randint(1,31)
        months.append(month)
        days.append(day)
    
    return months, days

def main():
    # With 70 people, there is a 99%
    eng_text = {
        'wrong_c':'Option not available, please type again your choice.\n',
        'title':'Birthday paradox.\n\nThe Birthday Pradox shows us that in agroup of N people, the odds that two of them have matching birthdays is surprisingly large.\n\n(It is not actually a paradox, it is just a surprising result)',
        'input':'How many birthdays shall I generate? (Max 100) \n > ',
        'show_1':'\nHere are the bithdays:\n',
        'first_r':'\n\nMatching birthdays in this simulation: ',
        'months':{
            1:'Jan',
            2:'Feb',
            3:'Mar',
            4:'Apr',
            5:'May',
            6:'Jun',
            7:'Jul',
            8:'Aug',
            9:'Sep',
            10:'Oct',
            11:'Nov',
            12:'Dec'
        },
        'ini':'\nInitianing 100,000 instances...\n',
        'sim':' simulations run.',
        'results':'\nOut of {:,} simulations of {} people, there was a matching birthday in that group {:,} times. This means that {} people have a {:.2f}% chance of having a matching birthday in their group.'
    }
    esp_text = {
        'wrong_c':'Opción no disponible, ingrese su elección nuevamente.\n',
        'title':'Paradoja del cumpleaños.\n\nLa paradoja del cumpleaños muestra que dentro de un grupo de N personas, las probabilidades de que dos de ellas cumplan años el mismo día es sorpresivamente alta.\n\n(Actualmente no es una paradoja, solo un resultado sorprendente)',
        'input':'Cuántos cumpleaños debería generar? (Max 100) \n > ',
        'show_1':'\nAquí están los cumpleaños:\n',
        'first_r':'\n\nNúmero de cumpleaños que coinciden: ',
        'months':{
            1:'Ene',
            2:'Feb',
            3:'Mar',
            4:'Abr',
            5:'May',
            6:'Jun',
            7:'Jul',
            8:'Ago',
            9:'Sep',
            10:'Oct',
            11:'Nov',
            12:'Dic'
        },
        'ini':'\nIniciando 100,000 instancias...\n',
        'sim':' simulaciones ejecutadas.',
        'results':'\nDe las {:,} simulaciones de {} personas, hubo una coincidencia en ese grupo {:,} veces. Esto significa que {} personas tienen {:.2f}% de probabilidad de tener una coincidencia en su grupo.'
    }
    text = [eng_text, esp_text]

    clear_screen()

    lang = int(get_choice(['1', '2'], 'Press 1 for english.\nPresione 2 para español.\n-> ', text[0]['wrong_c'])) - 1

    clear_screen()

    print(text[lang]['title'])
    resp = input(text[lang]['input'])

    try:
        resp = int(resp)
    except:
        raise ValueError('Must insert an integer')

    months, days = generate_birthdays(resp)

    print(37*'-')
    print(text[lang]['show_1'])
    
    birthday = []
    mat = 0
    for i in range(resp):
        current_bd = text[lang]['months'][months[i]] + ' ' + str(days[i])
        if mat == 0 and i > 0 and current_bd in birthday:
            mat += 1
        birthday.append(current_bd)
        print(birthday[i], end=' ')

    print(text[lang]['first_r'] + str(mat))
    
    print(text[lang]['ini'])

    instances = 100_000
    total_mat = 0

    for t in range(instances):
        if (t + 1) % 10_000 == 0:
            print(f'{t + 1:,}' + text[lang]['sim'])
        months, days = generate_birthdays(resp)
        
        birthday = []
        mat = 0
        for i in range(resp):
            current_bd = text[lang]['months'][months[i]] + ' ' + str(days[i])
            if mat == 0 and i > 0 and current_bd in birthday:
                mat += 1
                break
            birthday.append(current_bd)
        if mat > 0:
            total_mat += 1

    percent = (total_mat / instances) * 100

    print(text[lang]['results'].format(instances, resp, total_mat, resp, percent))

if __name__ == "__main__":
    main()