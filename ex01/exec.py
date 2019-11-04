#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 11:10:34 by baavril           #+#    #+#              #
#    Updated: 2019/11/04 11:47:07 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def reverse_alpha():
    if len(sys.argv) > 1:
        list = []
        for args in sys.argv[:0:-1]:
            list.append(args[::-1].swapcase())
        print(' '.join(list), end='\n')

if __name__ == '__main__':
    reverse_alpha()
