#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 10:11:14 by baavril           #+#    #+#              #
#    Updated: 2019/11/06 10:11:14 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

if __name__ == '__main__':

    obj = Recipe('glace', 3, 700, ['chocolat', 'vanille'], 'dessert', 'description')
    obj2 = Recipe('cegla', 3, 700, ['chocolat', 'vanille'], 'dessert', 'description')
    print(obj.name)
    print(obj.cooking_lvl)
    print(obj.cooking_time)
    print(obj.ingredients)
    print(obj.recipe_type)
    print(obj.description) 
    to_print = str(obj)
    str(obj)

    cookbook = Book('cookbook')
    cookbook.add_recipe(obj)
    cookbook.add_recipe(obj2)
    cookbook.get_recipe_by_type("dessert")
