#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cookbook.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 09:24:33 by baavril           #+#    #+#              #
#    Updated: 2019/11/05 09:24:33 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cookbook = {
        'sandwich': { 'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': '10'},
        'cake' : { 'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': '60'},
        'salad' : { 'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': '15'} }

def exit_program():
    raise SystemExit

def delete_recipes():
    menu()
    name = input("Type the recipe you would like to delete :\n")
    del cookbook[name]

def add_recipes():
    print('{0:-^50s}\n'.format("Add function", end='\n'))
    name = input("Write a name recipe\n")
    ingredients = input("Which ingredients composes your recipe ?\n")
    meal = input("What type of meal is it ?\n")
    prep_time = input("how much time does your recipe take ?\n")
    cookbook[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time' : prep_time}

def menu():
    print('{0:-^50s}\n'.format("Recipes names"), end='\n')
    for key in cookbook:
        print(key, end='\n')
    print('\n')

def user():
    print("Wrong Keywords' menu")
    namesec = input("Do you want to select a new keyword menu ? Enter yes or the program will exit\n")
    if namesec == "yes":
        prt_cookbook(cookbook)

def recipes():
    menu()
    lim = len(cookbook) - 1
    name = input("{0:^30s}".format("Which cookbook do you want ? Enter a keyword just above please\n"))
    try:
        print('{0:-^50s}\n'.format("ingredients", end='\n'))
        print("Le type de repas : {0}".format(cookbook[name]['meal']), end='\n')
        print("Le temps de preparation : {0}".format(cookbook[name]['prep_time']), end='\n')
        print("Ingredients : ", end='')
        for igt in range(len(cookbook[name]['ingredients']) - 1):
            print(cookbook[name]['ingredients'][igt], end='')
            print(', ', end='')
        print("{0}\n".format(cookbook[name]['ingredients'][igt + 1]), end='')
    except:
        user()

selection = {
        '1' : ('print the menu', menu),
        '2' : ('chose a recipe', print_a_recipe),
        '3' : ('add a recipe', add_recipes),
        '4' : ('delete a recipe', delete_recipes),
        '5' : ('exit program', exit_program)
        }

if __name__ == '__main__':

    while(42):
        print("\nPlease select a function by typing the corresponding number\n")
        for i in selection:
            print(i, selection[i][0])
        print("\n")
        selected = input(">>   ")
        try:
            selection[selected][1]()
        except KeyError:
            print('This option does not exist, please type the\
 corresponding number.\nTo exit, enter 5.', end='\n')
