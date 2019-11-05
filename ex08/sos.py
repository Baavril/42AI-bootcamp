#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 16:55:34 by baavril           #+#    #+#              #
#    Updated: 2019/11/05 16:55:34 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse_code = {
        'a' : '.-',
        'b' : '-...',
        'c' : '-.-.',
        'd' : '-..',
        'e' : '.',
        'f' : '..-.',
        'g' : '--.',
        'h' : '....',
        'i' : '..',
        'j' : '.---',
        'k' : '-.-',
        'l' : '.-..',
        'm' : '--',
        'n' : '-.',
        'o' : '---',
        'p' : '.--.',
        'q' : '--.-',
        'r' : '.-.',
        's' : '...',
        't' : '-',
        'u' : '..-',
        'v' : '...-',
        'w' : '.--',
        'x' : '-..-',
        'y' : '-.--',
        'z' : '--..',
        '0' : '-----',
        '1' : '.----',
        '2' : '..---',
        '3' : '...--',
        '4' : '....-',
        '5' : '.....',
        '6' : '-....',
        '7' : '--...',
        '8' : '---..',
        '9' : '----.',
        ' ' : '/'
        }

def check_errors():
    try:
        for word in sys.argv[1:]:
            word = word.lower()
            for char in word:
                test = morse_code[char]
    except KeyError:
        print("ERROR", end='\n')
        quit()

if __name__ == '__main__':
    check_errors()
    if (len(sys.argv) > 1):
        nb = 0
        for word in sys.argv[1:]:
            if nb >= 1:
                print('/ ', end='')
            nb += 1
            word = word.lower()
            for i in range(len(word) - 1):
                print(morse_code[word[i]], end=' ')
        print(morse_code[word[i + 1]])
