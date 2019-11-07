#!/usr/local/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baavril <baavril@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 12:36:28 by baavril           #+#    #+#              #
#    Updated: 2019/11/06 12:36:28 by baavril          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Recipe(object):
    ''' Recipe class
    Init name, cooking_lvl, cooking_time, ingredients, description
    , ingredients, recipe_type'''

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        self._name = self.only_str(name)
        self._cooking_lvl = self.int_range(cooking_lvl)
        self._cooking_time = self.only_int(cooking_time)
        self._ingredients = self.only_list(ingredients)
        self._recipe_type = self.check_recipe_lst(recipe_type)
        self._description = self.only_str(description)

    def __str__(self):
        s = "The name of the recipe is " + self._name + ". The ingredients are :"
        #c = len(self.ingredients)
        for elt in self.ingredients:
            s += ' ' + elt
        s += ". The recipe type is " + self.recipe_type + ". The description can be empty.\nDescription : " + self.description
        print(s)
        return s

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = self.only_str(name)

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        self.cooking_lvl = self.int_range(cooking_lvl)

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, cooking_time):
        self.cooking_time = self.int_range(cooking_time)

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self.ingredients = self.only_list(ingredients)

    @property
    def recipe_type(self):
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, recipe_type):
        self.recipe_type = self.check_recipe_lst(recipe_type)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self.description = self.only_str(description)

    @staticmethod
    def only_str(s):
        if isinstance(s, str):
            return (s)
        else:
            raise Exception('Not a valid type')

    @staticmethod
    def int_range(s):
        if isinstance(s, int) and s > 0 and s <= 5:
            return (s)
        else:
            raise Exception('Not a valid type')

    @staticmethod
    def only_int(s):
        if isinstance(s, int):
            return (s)
        else:
            raise Exception('Not a valid type')

    @staticmethod
    def only_list(s):
        if isinstance(s, list):
            return (s)
        else:
            raise Exception('Not a valid type')

    @staticmethod
    def check_recipe_lst(s):
        recipe_lst = ['starter', 'lunch', 'dessert']
        if isinstance(s, str):
            for i in recipe_lst:
                if s is i:
                    return (s)
            else:
                raise Exception('Not a valid type')
        else:
            raise Exception('Not a valid type')
