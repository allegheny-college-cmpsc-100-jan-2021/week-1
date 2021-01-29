#!/usr/bin/env python

# TODO: import the random module

# This function parses both the player 
# and monster files
def parse_file(filename):
    members = {}
    file = open(filename,"r")
    lines = file.readlines()
    for line in lines:
        name, diff = line.split(";")
        members[name] = {"str": int(diff)}
    return members

# MONSTER FIGHT!
def fight_monster(diff, roll):
    if diff > roll:
        return -1
    return 1

# Performs rolls for groups
def do_roll(entities):
    roll = 0
    
    for entity in entities:
        e_name = entity
        e_str = entities[entity]["str"]
        e_roll = roll_dice(e_str)
        roll += e_roll
        print(f"{entity} rolls a {e_roll}!")
        
    return roll

# Roll an individual die
def roll_dice(sides):
    return random.randint(1, sides)

# Initialze points
points = 0

# TODO: Load files to parse for player and
#       monster data

# Create loop to move from challenge to challenge
for monster in monsters:
    
    # TODO: "Appear" the monster and do the monster's
    #       die roll
    
    # TODO: Get players' team roll
    
    print(f"The group rolled a total of: {group_roll}!")
    
    # TODO: Get the result of this single fight
    
    if result > 0: 
        print(f"The players beat the {m_name}!\n")
    else:
        print(f"The players failed to beat the {m_name}!\n")

# TODO: if statement to report the final outcome of all
#       battles!