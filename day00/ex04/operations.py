#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 16:18:05 by baavril           #+#    #+#              #
#    Updated: 2019/11/04 16:18:05 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

def operations(a, b):
    print('Sum: {0}'.format(a + b))
    print('Difference: {0}'.format(a - b))
    print('Product: {0}'.format(a * b))
    try:
        print('Quotient: {0}'.format(a / b))
    except:
        print('Quotient: ERROR (div by zero)')
    try:    
        print('Remainder: {0}'.format(a % b))
    except:
        print('Remainder: ERROR (modulo by zero)')

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 3:
        try:
            operations(int(sys.argv[1]), int(sys.argv[2]))
        except:
            print("InputError: only numbers \nUsage: python operations.py\nExample:\npython operations.py 10 3")
    elif argc <= 3:
        print("Usage: python operations.py\nExample:\n  python operations.py 10 3")
    elif argc > 3:
        print("InputError: too many arguments\nUsage: python operations.py\nExample:\npython operations.py 10 3")
