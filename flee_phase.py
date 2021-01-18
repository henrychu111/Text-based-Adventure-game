"""
This file defines the flee phase
"""


import random


def flee_result(character):
  """
  Checks to see if character successfully flees or takes damage


  param:          character is the character list
  precondition:   user chooses to flee
  postcondition:  determines user successfully flees or takes damage when fleeing 
  return:         no return

  no doctest
  """
  damage_chance = random.randint(1,10)
  if damage_chance == 1:
    flee_damage = random.randint(1, 4)
    character[1] -= flee_damage
    print("Oh no! You got hit when you were fleeing and took %d damage leaving %d health left" % (flee_damage, character[1]))
  else:
    print("You have successfully escaped!")
