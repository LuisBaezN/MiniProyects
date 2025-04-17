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
    eng_text = {
        'wrong_c':'Option not available, please type again your choice.\n',
        'title':'Birthday paradox.\n\nExplore the surprising probabilities of this paradox.',
        'input':'How many birthdays shall I generate? (Max 100) \n > ',
        'show_1':'Here are the bithdays: ',
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
        'ini':'\nInitianing 100,000 instances...',
        'sim':' simulations run.'
    }
    esp_text = {
        'wrong_c':'Opción no disponible, ingrese su elección nuevamente.\n',
        'title':'Paradoja del cumpleaños.\n\nExplore las sorprendentes de esta paradoja.',
        'input':'Cuántos cumpleaños debería generar? (Max 100) \n > ',
        'show_1':'Aquí están los cumpleaños: ',
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
        'ini':'\nIniciando 100,000 instancias...',
        'sim':' simulaciones ejecutadas.'
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

    print(text[lang]['show_1'])
    
    birthday = []
    mat = 0
    for i in range(resp):
        birthday.append(text[lang]['months'][months[i]] + ' ' + str(days[i]))
        print(birthday[i], end=' ')
        if mat == 0 and i > 0 and birthday[i] in birthday:
            mat += 1

    print(text[lang]['first_r'] + str(mat))
    '''
    print(text[lang]['ini'])

    instances = 100_000
    total_mat = 0

    for t in range(instances):
        if (instances + 1) % (t+1) == 0:
            print(str(t + 1) + text[lang]['sim'])
        months, days = generate_birthdays(resp)
        
        birthday = []
        mat = 0
        for i in range(resp):
            birthday.append(text[lang]['months'][months[i]] + ' ' + str(days[i]))
            if mat == 0 and i > 0 and birthday[i] in birthday:
                mat += 1
                break
        if mat > 0:
            total_mat += 1

    percent = (total_mat / instances) * 100

    print(percent)
    '''

if __name__ == "__main__":
    main()