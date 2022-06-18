import os
import string
import random
# import tkinter as tk
# from tkinter import E, S, W, N, ttk


# window = tk.Tk()


settings = {
    'upper' : True,
    'lower' : True,
    'number' : True,
    'symbol' : True,
    'space' : False,
    'lenght' : 8
}


def clear_screen():
    os.system('cls')


def intro():
    print('<<<<welcome to pasword generator>>>>')
    print('in first place you have to set settings')
    print('at the end the generated password is shown')
    print('-' * 70)


def get_lenght(settings):
    
    while True:
        user_choice = input(f'please enter the lenght of the password (enter = {settings["lenght"]}) :  ')
        
        if user_choice == '' or user_choice.isdigit():
            if user_choice != '':
                return int(user_choice)
            return settings['lenght']
        
        print('please enter a number!')


def get_settings(settings):
    
    for option, value in settings.items():
        if option != 'lenght':

            if value == True:
                default = 'yes'
            else:
                default = 'no'

            while True:
                user_choice = input(f'do you want {option} in your password? (y = yes , n = no , enter = {default}):  ')

                if user_choice in ['y', 'n', '']:
                    if user_choice == 'y':
                        settings[option] = True
                    elif user_choice == 'n':
                        settings[option] = False
                    break
                else:
                    print('please enter "y" or "n" or press "enter"')
        else:
            settings[option] = get_lenght(settings)


def make_random_upper():
    return random.choice(string.ascii_uppercase)


def make_random_lower():
    return random.choice(string.ascii_lowercase)


def make_random_num():
    return random.choice(string.digits)


def make_random_symbol():
    return random.choice(string.punctuation)


def make_random_letter(settings):
        user_option = []

        for option, value in settings.items():
            if option != 'lenght':
                if value:
                    user_option.append(option)
        
        random_option = random.choice(user_option)

        if random_option == 'upper':
            return make_random_upper()

        elif random_option == 'lower':
            return make_random_lower()

        elif random_option == 'number':
            return make_random_num()

        elif random_option == 'symbol':
            return make_random_symbol()
        
        else:
            return ' '


def password_generator(setting):
    
    while True:

        generated_password = ''
        
        for i in range(setting['lenght']):
            generated_password += make_random_letter(settings)

        print('-' * 70)
        print(f'your generated password is: {generated_password}')
        print('-' * 70)

        repeat = input('do you want another password with current settings ("y" = yes, "n" = no, enter = yes)  ')

        if repeat in ['y', 'n', '']:
            if repeat == 'n':
                break
        
        else:
            print('plese enter "y" or "n" or press enter')


def change_settings():
    
    while True:  
        
        print('-' * 70)
        want_change = input('do you want to change setting and get another password? ("y" = yes, "n" = no, enter = yes):  ')

        if want_change in ['y', 'n', '']:

            if want_change == 'n':

                print('-' * 70)
                print('\t\t<<<thank you for choosing us!!>>>')
                print('-' * 70)

                return
            
            print('-' * 70)
            get_settings(settings)
            password_generator(settings)
        
        else:
            print('plese enter "y" or "n" or press enter')


def run():
    clear_screen()
    intro()
    get_settings(settings)
    password_generator(settings)
    change_settings()




# lbl_settings = ttk.Label(
#     master= window,
#     text='set your settings:'
# )

# lbl_settings.grid(row=0, column=0)

# cbtn_upper = ttk.Checkbutton(
#     master=window,
#     text='Upper case letters',
# )

# cbtn_upper.grid(row=0, column=1)

# cbtn_lower = ttk.Checkbutton(
#     master=window,
#     text='Lower case letters',
# )

# cbtn_lower.grid(row=0, column=2)

# cbtn_num = ttk.Checkbutton(
#     master=window,
#     text='Numbers',
# )

# cbtn_num.grid(row=1, column=1)

# cbtn_symbol = ttk.Checkbutton(
#     master=window,
#     text='Symbols',
# )

# cbtn_symbol.grid(row=1, column=2)

# cbtn_space = ttk.Checkbutton(
#     master=window,
#     text='Spaces',
# )

# cbtn_space.grid(row=2, column=1)
# btn_generate = ttk.Button(
#     master=window,
#     text='Generate Password',
# )

# btn_generate.grid(row=0, column=3)

# lbl_pass = ttk.Label(
#     master=window,
#     text='Your Generated Password is:',
# )

# lbl_pass.grid(row=3, column=0)

# lbl_gen_pass = ttk.Label(
#     master=window,
#     text='Your password will be shown here.....',
# )

# lbl_gen_pass.grid(row=3, column=1)

# window.title('Password Generator')
# window.mainloop()

run()


