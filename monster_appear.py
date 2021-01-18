"""
This file defines if and what monster appears
"""


import random

def check_for_monster():
  """
  Checks if the monster appears


  param:          no parameter
  precondition:   user moves to different place
  postcondition:  determines if character encounters a monster 
  return:         returns True if there is a monster and False if no monsters

  no doctest
  """
  monster_chance = random.randint(1, 100)
  if monster_chance <= 25:
    return True
  else:
    return False

    

def which_monster():
  """
  Checks to see which monster appears


  param:          no parameter
  precondition:   if monster appears
  postcondition:  determines the monster's name 
  return:         monster

  no doctest
  """
  type_of_monsters = (
    ["slime", "is slowly oozing towards you and wants to lick your feet"], 
    ["bat", "is flying around your head wanting to suck your blood"],
    ["hound", "is barking voraciously at you"],
    ["goblin", "with an ugly face is sneering at you"],
    ["wolf", "in front of you howls AWWWWWOOOOOOO!!!"],
    ["kobold", "is menacingly looking in your direction"],
    ["saber-tooth tiger", "stalks toward you with drool dripping from its massive teeth"],
    ["dark knight", "in black armour with a piercing aura unsheathes his sword"],
    ["warlock", "with suffocating magic swirling around walks toward you"])
  monster = random.choice(type_of_monsters)
  return monster

