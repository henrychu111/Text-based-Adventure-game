"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.
Henry Chu
Spencer Loren
"""

import doctest
import movement_phase
import enter_room



def current_state(character):
  """
  Checks to see which monster appears


  param:          charcter profile
  precondition:   none
  postcondition:  determiens if character dead
  return:         whether the character is dead

  >>> character = [[2, 2], 10, "Chris", 0]
  >>> current_state(character)
  False
  >>> character = [[2, 2], 0, "Chris", 0]
  >>> current_state(character)
  True
  """
  if character[1] <= 0:
    return True
  return False


def display_ending_message(is_quit, is_dead, is_won):
  """
  Checks to see character quit, won or dead

  param:         is_quit if character quit 
                 is_dead if character is dead
                 is_won if charcter won
  precondition:   all 3 must be booleans
  postcondition: prints out the message
  return:         no return

  >>> display_ending_message(True, False, False)
  We hope you had fun, please come back and play again!

  >>> display_ending_message(False, True, False)
  Unfortunately, you became monster food, better luck next time.
  
  >>> display_ending_message(False, False, True)
  Congratulations, You Won! The End
  """
  if is_quit:
    print(f"We hope you had fun, please come back and play again!")
  if is_dead:
    print(f"Unfortunately, you became monster food, better luck next time.")
  if is_won:
    print(f"Congratulations, You Won! The End")


def main():
    """Drives the program."""
    doctest.testmod()
    print("Hello wonderer!! You have been summoned to this wretched place to duke it out with monsters of my choosing!. You must defeat ten of them if you wish to leave.")
    board = ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4))
    character_name = input("Please enter your name: ")
    print("%s, your adventure begins!!! Have fun." % character_name)
    character = [[2, 2], 10, character_name, 0]
    is_quit = False
    is_won = False
    is_dead = False



    while (not(is_quit or is_dead or is_won)):
      is_quit = movement_phase.start_movement_phase(character, board)
      if not(is_quit):
        is_quit = enter_room.check_monster_in_current_location(character) 
      is_dead = current_state(character)
      if character[3] == 10:
        is_won = True
    
    display_ending_message(is_quit, is_dead, is_won)
    doctest.testmod()
 

   


if __name__ == "__main__":
    main()
