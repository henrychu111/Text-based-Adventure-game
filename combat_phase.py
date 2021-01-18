"""
This file defines the combat
"""

import random


def check_for_turn():
  """
  Checks if monster or player goes first

  param:          no parameters
  precondition:   if user chose to fight
  postcondition:  caculates if monster/player goes first 
  return:         returns either player or monster

  no doctest
  """
  your_speed = random.randint(1, 20)
  monster_speed = random.randint(1, 20)
  if your_speed > monster_speed:
    return 'player'
  elif your_speed < monster_speed:
    return 'monster'
  else:
    print("Both could not land a hit")
    return check_for_turn()


def check_for_damage():
  """
  Checks for the amount of damage

  param:          no parameters
  precondition:   monster or player attacks
  postcondition:  caculates the damage 
  return:         amount of damage

  no doctest
  """
  damage = random.randint(1, 6)
  return damage


def player_turn(monster_name, monster_health):
  """
  Checks if monster or player goes first

  param:          monster_name is the name of monster
                  monster_health is the hp of the monster
  precondition:   if it is player's turn
  postcondition:  calculates the damage the monster took 
  return:         returns the monster's remaining health
  
  no doctest
  """
  monster_damage = check_for_damage()
  monster_health -= monster_damage
  print_monster_damage(monster_name, monster_damage)
  return monster_health


def combat_round(character, monster):
  """
  Checks to see if monster or player wins in the fight

  param:          monster is type of monster  
                  character is the character list
  precondition:   user chooses to fight
  postcondition:  determines if user wins or dies 
  return:         no return

  no doctest
  """
  total_monster_health = 5
  while character[1] > 0 and total_monster_health > 0:
    turn = check_for_turn()
    if turn == 'player':
      total_monster_health = player_turn(monster[0], total_monster_health)
      if total_monster_health > 0:
        player_damage = check_for_damage()
        character[1] -= player_damage
        if character[1] > 0:
          print("The %s retaliated and you took %d damage with %d health left" %(monster[0], player_damage, character[1]))
    else:
        player_damage = check_for_damage()
        character[1] -= player_damage
        if character[1] > 0:
          print("Your got hurt from the %s and took %d damage with %d health left" % (monster[0], player_damage, character[1]))
          total_monster_health = player_turn(monster[0], total_monster_health)
  if character[1] > 0:
    print("You defeated the %s and have %d health remaining." % (monster[0], character[1]))
    character[3] += 1


      


def print_monster_damage(monster_name, monster_damage):
  """
  Prints the damage you deal to the monster

  param:          monster_name is the name of the monster  
                  monster_damage is the amount of damage the monster takes
  precondition:   character damages the monster
  postcondition:  prints monster damage
  return:         no return

  >>> print_monster_damage('slime', 2)
      Your jab nicked the slime and dealt 2 damage!
  >>> print_monster_damage('warlock', 4)
      Your slash swept across the warlock and dealt 4 damage!!
  >>> print_monster_damage('kobold', 6)
      Your lunge stab pierced through the kobold's head, dealing 6 damage and killed it
  """
  if monster_damage <= 2:
    print("Your jab nicked the %s and dealt %d damage!" % (monster_name, monster_damage))
  elif monster_damage <= 4:
    print("Your slash swept across the %s and dealt %d damage!!" % (monster_name, monster_damage))
  else:
    print("Your lunge stab pierced through the %s's head, dealing %d damage and killed it"
          % (monster_name, monster_damage))






