#These are Maple Oaks'
#characterstics
strength = -1
intelligence = 1
wisdom = 1
dexterity = 2
constitution = 1
charisma = 2
proficiencies = ['Dexterity', 'Charisma']
proficient_bonus = 2

def check_proficiency(traits, current_score):
    for i, prof in enumerate(proficiencies):
        if traits == prof:
            print('Luckily youre proficient in {trait}!'.format(trait=trait))
            return current_score + proficient_bonus
    return current_score    
    
trait = input('What trait are you rolling?\nStrength, Intelligence, Dexterity,\nWisdom, Constitution, or Charisma?\n')
check_or_save = input('Is this a check or save?\n')

trait = trait.lower()
check_or_save = check_or_save.lower()


#Roll a d20
from random import randint
dice_roll = randint(1,20) 

if trait == "strength": 
    if check_or_save == "save": strength = check_proficiency("Strength", strength)
    score = dice_roll + strength
    print("Dice Roll... {dice_roll} + {trait} = {score}".format(dice_roll=dice_roll,trait=strength,score=score))
if trait == "intelligence":
    if check_or_save == "save": intelligence = check_proficiency("Intelligence", intelligence)
    score = dice_roll + intelligence
    print("Dice Roll... {dice_roll} + {trait} = {score}".format(dice_roll=dice_roll,trait=intelligence, score=score))
if trait == "dexterity":
    if check_or_save == "save": dexterity = check_proficiency("Dexterity", dexterity)
    score = dice_roll + dexterity
    print("Dice Roll... {dice_roll} + {trait} = {score}".format(dice_roll=dice_roll,trait=dexterity,score=score))
if trait == "constitution":
    if check_or_save == "save": constitution = check_proficiency("Constitution", constitution)
    score = dice_roll + constitution
    print("Dice Roll... {dice_roll} + {trait} = {score}".format(dice_roll=dice_roll,trait=constitution,score=score))
if trait == "charisma":
    if check_or_save == "save": charisma = check_proficiency("Charisma", charisma)
    score = dice_roll + charisma
    print("Dice Roll... {dice_roll} + {trait} = {score}".format(dice_roll=dice_roll,trait=charisma,score=score))
if trait == "wisdom": 
    if check_or_save == "save": strength = check_proficiency("Wisdom", strength)
    score = dice_roll + strength
    print("Dice Roll... {dice_roll} + {trait} = {score}".format(dice_roll=dice_roll,trait=wisdom,score=score))





