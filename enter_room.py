import monster_appear
import combat_phase
import user_input
import flee_phase

def check_monster_in_current_location(character):
  """
  Determines character choice if monster appears, combat or flee

  If no monster appears, then the player heals 2 health


  param:          character is the character list
  precondition:   character moves to a different place
  postcondition:  if monster appears, does combat or flee depending on the choice
  return:         returns True if character quits
                  returns False if character fights or flees successfully

  no doctest
  """
  if monster_appear.check_for_monster():
    monster = monster_appear.which_monster()
    print ("A %s %s." % (monster[0], monster[1]))
    acceptable_user_choices = ('flee', 'fight')
    user_choice = user_input.get_user_input(acceptable_user_choices)
    if user_choice == 'fight':
      combat_phase.combat_round(character, monster)
    elif user_choice == 'flee':
      flee_phase.flee_result(character)
    else:
      return True
  else:
    print("There are no monsters here!")
    prev_health = character[1]
    character[1] += 2
    if character[1] > 10:
      character[1] = 10
    print("Your current health is %d, healed by %d" % (character[1], character[1] - prev_health))
  return False