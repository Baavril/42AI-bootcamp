#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 12:56:24 by baavril           #+#    #+#              #
#    Updated: 2019/11/04 12:56:24 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def     whois():
        if len(sys.argv) > 1:
            integer = int(sys.argv[1])
            if integer % 2:
                print("{0} is Odd number".format(integer));
            else:
                print("{0} is Even number".format(integer));

if __name__ == '__main__':
    whois()
