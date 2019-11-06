#!/bin/bash

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    install.sh                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 10:47:36 by baavril           #+#    #+#              #
#    Updated: 2019/11/04 10:47:36 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

function install_python()
{
	curl -o /goinfre/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
	if [ $? -ne 0 ]
	then
		printf "Failure: could not download miniconda.\n"
	fi
	bash /goinfre/miniconda.sh -b -p /goinfre/miniconda
	if [ $? -eq 0 ]
	then
		printf "Python has been installed.\n"
	else
		printf "Failure: Python could not be installed.\n"
	fi
	if [ -d "/goinfre/miniconda" ]
	then
		env PATH="/goinfre/miniconda/bin:$PATH" bash
	else
		printf "Failure: Miniconda could not be found.\n"
	fi
}

install_python
