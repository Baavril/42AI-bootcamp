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

class Recipe:

    nbrecipe = 0
    
    def check(self):
        if (isinstance(name, str)):
           self._name = p
        else:
            print("Error")

    def __init__(self, name=""):
        try:
            if (isinstance(name, str)):
                self._name = name                # name of recipe
        except:
            print("Error3")
      #  self.name = name                # name of recipe
       # self._cooking_lvl = 0            # range 1 - 5
       #self._cooking_time = 0           # n minutess (no '-' values)
       # self._ingredients = ingredients  # list of ingredients
       # self._description = description  # description can be empty
       # self._recipe_type = 0           
        #self._cooking_lvl = cooking_lvl 
        #nbrecipe += 1


  #  def _get_name(self):
   #     return self._name
    #def _set_name(self, p):
     #   self._name = p

   # name = property(_get_name, _set_name)
    
    @property 
    def name(self):
        try:
            print(name)
            if (isinstance(name, str)):
                return(self._name)
        except:
            print("Error1")
    
    @name.setter
    def name(self, p):
        try:
            if (isinstance(name, str)):
                self._name = p
        except:
            print("Error2")
