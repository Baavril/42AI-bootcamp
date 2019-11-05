#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 19:34:57 by baavril           #+#    #+#              #
#    Updated: 2019/11/05 19:35:00 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep, time
import sys

start = time()

def ft_progress(listy):
    for i in listy:
        eta = float(time() - start)
        prct = i / len(listy)
        load = round(prct * 10) * "=" + ">"
        print("\x1b[6;31;40mETA: {0:4.2f}s [{2:12}[{1:.0%}] ]\x1b[0m".format(eta, prct, load), end='\r')
        yield i

if __name__ == '__main__':
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.0005)
    print()
    print(ret)
