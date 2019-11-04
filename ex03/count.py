#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 14:38:26 by baavril           #+#    #+#              #
#    Updated: 2019/11/04 14:38:26 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(txt = ""):
    nu = 0;
    nl = 0;
    np = 0;
    ns = 0;
    if not txt:
       txt = input("What is your input ?\n")
    nb_chars = len(txt)
    for c in txt:
        if (c.isupper()):
            nu += 1
        if (c.islower()):
            nl += 1
        if c in string.punctuation:
            np += 1
        if (c.isspace()):
            ns += 1
    print("The text contains {0} characters:".format(nb_chars))
    print("- {0} upper letters".format(nu))
    print("- {0} lower letters".format(nl))
    print("- {0} punctuation marks".format(np))
    print("- {0} spaces".format(ns))

if __name__ == '__main__':
    text_analyzer()
