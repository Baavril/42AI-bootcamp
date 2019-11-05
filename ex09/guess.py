#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 18:05:04 by baavril           #+#    #+#              #
#    Updated: 2019/11/05 18:05:04 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def check_numbers(nb1, nb2, count):
    if (nb2 == "exit"):
        quit()
    try:
        nb2 = int(nb2)
        if nb1 is nb2:
            print("Congratulations, you've got it!\nYou won in {0} attempts!".format(count))
            if nb1 is 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            quit()
        elif nb1 > nb2:
            print("Too low!")
        elif nb1 < nb2:
            print("Too high!")
    except ValueError:
        print("That's not a number.")

if __name__ == '__main__':
    nb1 = random.randint(1, 99)
    count = 0
    print('This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType \'exit\' to end the game.\nGood luck!')
    while(42):
        nb2 = input("What's your guess between 1 and 99?\n>> ")
        count += 1
        check_numbers(nb1, nb2, count)
