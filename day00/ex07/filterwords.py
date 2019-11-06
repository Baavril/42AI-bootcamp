#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 15:37:02 by baavril           #+#    #+#              #
#    Updated: 2019/11/05 15:37:02 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

if __name__ == '__main__':

    try:
        nb = int(sys.argv[2])
        lw = re.sub('\b[a-zA-Zi]\s', '', sys.argv[1])
        lw = re.split(' +', lw)
        print([w for w in lw if len(w) > int(sys.argv[2])])
    except:
        print("ERROR", end='\n')
