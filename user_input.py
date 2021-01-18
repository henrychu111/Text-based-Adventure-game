"""
File conatins functions related to user inputs
"""


def get_user_input(acceptable_inputs):
  """
  Cleans and verifies the user's input
  
  A function that will keep prompting a user for an ecceptable input until one is given.

  :param acceptable_inputs: A list containing the user inputs that will be accepted
  :precondition: acceptable_inputs must be a non-empty list
  :postcondition: Displays helpful messages to guid the user to the correct inputs
  :return: The cleaned and acceptable user input

  Function takes user input, so no Doctest
  """
  is_acceptable_value = False
  quit_command = "quit"
  while not(is_acceptable_value):
    user_choice = input(f"Please input one of the keywords, {acceptable_inputs}: ").strip().lower()
    if user_choice == quit_command or user_choice in acceptable_inputs:
      is_acceptable_value = True
    else:
      print(f"Your input of was not an accepted command, please input one of the keywords {acceptable_inputs} or the command '{quit_command}' to end the game.")
  return user_choice
