#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 18:02:27 by baavril           #+#    #+#              #
#    Updated: 2019/11/04 18:02:27 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':

    languages = {
            'Python': 'Guido van Rossum',
            'Ruby': 'Yukihiro Matsumoto',
            'PHP': 'Rasmus Lerdorf',
            }
    for key in languages:
        print(key + " was created by " + languages[key])
