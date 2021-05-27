#This program will generate a random password of 8 characters everytime it runs

import random

def random_pass():
    '''
        This function generates a random password satisfying the following conditions

        1. 2 uppercase letters from A to Z,
        2. 2 lowercase letters from a to z,
        3. 2 digits from 0 to 9,
        4. 2 punctuation signs such as !, ?, “, # etc.

        Return : password(string)
    '''
    uppercase1 = chr(random.randint(65,90))
    uppercase2 = chr(random.randint(65,90))
    lowercase1 = chr(random.randint(97,122))
    lowercase2 = chr(random.randint(97,122))
    digit1 = random.randint(0,9)
    digit2 = random.randint(0,9)
    punctutation1 = random.choice(['!', '#', '$', '%', '&', '?', '@'])
    punctutation2 = random.choice(['!', '#', '$', '%', '&', '?', '@'])

    password = uppercase1 + uppercase2 + lowercase1 + lowercase2 + str(digit1) + str(digit2) + punctutation1 + punctutation2
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

print("********* Random Password Generator ******\n")
print('''
        This program generates a random password satisfying the following conditions

        1. 2 uppercase letters from A to Z,
        2. 2 lowercase letters from a to z,
        3. 2 digits from 0 to 9,
        4. 2 punctuation signs such as !, ?, “, # etc.
    ''')
print(f"Password Generated ==> {random_pass()}")