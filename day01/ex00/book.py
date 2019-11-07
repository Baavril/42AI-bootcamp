#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 10:20:04 by baavril           #+#    #+#              #
#    Updated: 2019/11/06 10:20:04 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from datetime import datetime

class Book(object):
    
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipes_list = {'starter' : {}, 'lunch' : {}, 'dessert' : {}}

    def get_recipe_by_type(self, recipe_type):
        for values in self.recipes_list[recipe_type]:
            print(str(values))


    def add_recipe(self, recipe):
        recipe_lst = ['starter', 'lunch', 'dessert']
        try:
            for elt in recipe_lst:
                if recipe.recipe_type is elt:
                    self.recipes_list[elt][recipe.name] = recipe
                    self.last_update = datetime.now()
                    print(self.last_update)
        except:
            raise Exception('Not a valid type')
