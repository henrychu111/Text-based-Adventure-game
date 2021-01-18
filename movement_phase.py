"""
This file defines the movement phase for the character
"""

import doctest
import user_input
import random


def display_map(character, board):
  """
  Display dungeon map.
  
  A simple function that will output the map of the dungeon to the screen.

  :param character: A list containing the character's current state 
  :param board: A list of lists representing the dungeon area and coordinates. The main lists represents dungeon rows and the nested lists represent the dungeon columns for coordinates.
  :precondition: character must have their coordinates within the scope of the board
  :precondition: board must be a non-empty list containing equal length, non-empty nested lists, with each nested list starting at 0 and incrementing by 1 for each element.
  :postcondition: Prints a diagram of the dungeon map to the user screen.
  
  >>> character = [[2, 2], 10, "Chris"]
  >>> board = ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4))
  >>> display_map(character, board)
  ---------
  | OOOOO |
  | OOOOO |
  | OOXOO |
  | OOOOO |
  | OOOOO |
  ---------
  <BLANKLINE>
  """
  display_text = f"---------\n"
  for each_line_index in range(len(board)):
    line_string =""
    for each_column_index in range(len(board[each_line_index])):
      character_row_position = character[0][0]
      character_column_position = character[0][1]
      if each_line_index == character_row_position and each_column_index == character_column_position:
        line_string += "X"
      else:
        line_string += "O"
    display_text += f"| {line_string} |\n"
  display_text += f"---------\n"
  print(display_text)


def get_available_movement_options(character, board):
  """
  Get the directions that the character can move
  
  A simple function that will output a list of directions that the chracter can move

  :param character: A list containing the character's current state 
  :param board: A list of lists representing the dungeon area and coordinates. The main lists represents dungeon rows and the nested lists represent the dungeon columns for coordinates.
  :precondition: character must have their coordinates within the scope of the board
  :precondition: board must be a 5 by 5 board
  :postcondition: Will determine which directions the character can move
  :return: A list of directions the character can move
  
  >>> character = [[0, 0], 10, "Chris"]
  >>> board = ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4))
  >>> get_available_movement_options(character, board):
  ['s', 'e']

  >>> character = [[0, 4], 10, "Chris"]
  >>> board = ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4))
  >>> get_available_movement_options(character, board):
  ['s', 'w']

  >>> character = [[4, 0], 10, "Chris"]
  >>> board = ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4))
  >>> get_available_movement_options(character, board):
  ['n', 'e']

  >>> character = [[4, 4], 10, "Chris"]
  >>> board = ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4))
  >>> get_available_movement_options(character, board):
  ['n', 'w']

  >>> character = [[2, 2], 10, "Chris"]
  >>> board = ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4))
  >>> get_available_movement_options(character, board):
  ['n', 's', 'e', 'w']
  """
  available_directions = []
  character_row_position = character[0][0]
  character_column_position = character[0][1]
  if character_row_position > 0:
    available_directions.append('n')
  if character_row_position < 4:
    available_directions.append('s')
  if character_column_position > 0:
    available_directions.append('w')
  if character_column_position < 4:
    available_directions.append('e')
  return available_directions


def display_available_moves(acceptable_moves):
  """
  Displays the available moves open to the user
  
  A simple function that will output the available character moves in an rpg aesthetic

  :param acceptable_moves: A list of the first letters of the coardinal directions that the user may move
  :precondition: acceptable_moves must be a non-empty list
  :postcondition: Prints the available character moves in an rpg aesthetic to the user's screen
  
  >>> acceptable_moves = ['n', 's', 'e', 'w']
  >>> display_available_moves(acceptable_moves)
  You look around and see an exit to your North (n), East (e), South (s), West (w). What direction would you like to travel?
  <BLANKLINE>
  """
  output_string = "You look around and see an exit to your "
  if 'n' in acceptable_moves:
    output_string += "North (n), "
  if 'e' in acceptable_moves:
    output_string += "East (e), "
  if 's' in acceptable_moves:
    output_string += "South (s), "
  if 'w' in acceptable_moves:
    output_string += "West (w), "
  output_string = output_string[:-2]
  output_string += ". What direction would you like to travel?\n"
  print(f"{output_string}")


def move_character(character, user_move):
  """
  Move character
  
  A simple function that updates the characters coordinates based on the direction moved

  :param character: A list containing the character's current state 
  :param user_move: The first, lowercase, letter of the cardinal direction that the character is moving to
  :precondition: character must have their coordinates within the scope of the board
  :precondition: user_move must be a string of length 1, containing the first, lowercase, letter of a cardinal direction that would break a 5 by 5 board
  :postcondition: Updates the chracter's coordinates, within the constrictions of a 5 by 5 board
  
  >>> character = [[2, 2], 10, "Chris"]
  >>> user_move = 'n'
  >>> move_character(character, user_move)
  >>> print(character)
  [[1, 2], 10, 'Chris']

  >>> character = [[2, 2], 10, "Chris"]
  >>> user_move = 'e'
  >>> move_character(character, user_move)
  >>> print(character)
  [[2, 3], 10, 'Chris']

  >>> character = [[2, 2], 10, "Chris"]
  >>> user_move = 's'
  >>> move_character(character, user_move)
  >>> print(character)
  [[3, 2], 10, 'Chris']

  >>> character = [[2, 2], 10, "Chris"]
  >>> user_move = 'w'
  >>> move_character(character, user_move)
  >>> print(character)
  [[2, 1], 10, 'Chris']
  """
  character_row_position = character[0][0]
  character_column_position = character[0][1]
  if user_move == 'n':
    character_row_position -= 1
    character[0][0] = character_row_position
  elif user_move == 's':
    character_row_position += 1
    character[0][0] = character_row_position
  elif user_move == 'e':
    character_column_position += 1
    character[0][1] = character_column_position
  elif user_move == 'w':
    character_column_position -= 1
    character[0][1] = character_column_position


def get_random_room_description():
  """
  Get a random dungeon room description.
  
  A simple function that will randomly pick a dungeon room description from a list of possible descriptions.

  :postcondition: Randomly picks and returns a room description
  :return: The room description string
  
  No doctest, utilizes random numbers
  """
  # Further descriptions will be added if there is sufficient time leftover
  reference_list_room_descriptions = [
    f"The room is plain, with stone walls and illuminated by torches. There were no special landmarks or distinguishing features around the room."
  ]
  room_description_index = random.randint(0, len(reference_list_room_descriptions) - 1)
  return reference_list_room_descriptions[room_description_index]


def display_new_room_message(user_move):
  """
  Display the room entry message.
  
  A simple function that will output the new room message to the screen.

  :param user_move: A string identifying if the user moved, north, south, east, or west
  :precondition: user_move must be the lowercase first character of the cardinal direction that the user moved 
  :postcondition: Prints the room entry message to the user's screen
  
  No doctest, the room description is randomly generated
  """
  if user_move == 'n':
    direction_of_entry = "South"
  elif user_move == 's':
    direction_of_entry = "North"
  elif user_move == 'e':
    direction_of_entry = "West"
  elif user_move == 'w':
    direction_of_entry = "East"
  print(f"\nYou enter from the {direction_of_entry} passage into a room. {get_random_room_description()}\n")



def start_movement_phase(character, board):
  """
  Takes user through the movement portion of the game
  
  A fucntion that will display the navigation information, get the user input, and move the character.

  :param character: A list containing the character's current state
  :param board: A list of lists representing the dungeon area and coordinates. The main lists represents dungeon rows and the nested lists represent the dungeon columns for coordinates.
  :precondition: character must be the list containing the character information, with their coordinates within the scope of the baord
  :precondition: board must be a non-empty list containing equal length, non-empty nested lists, with each nested list starting at 0 and incrementing by 1 for each element.
  :postcondition: Moves the character to the next room they wat to visit
  :return: Whether the user quit the game

  Function takes user input, so no Doctest
  """
  display_map(character, board)
  acceptable_moves = get_available_movement_options(character, board)
  display_available_moves(acceptable_moves)
  user_move = user_input.get_user_input(acceptable_moves)
  if user_move == 'quit':
    return True
  move_character(character, user_move)
  display_new_room_message(user_move)
  return False