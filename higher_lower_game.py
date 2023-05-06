import os
from random import choice

from art import logo, vs
from game_data import data

print(logo)
score = 0
game_should_continue = True

player_a = choice(data)
player_b = choice(data)


# Format random player into printable format
def format_data(player):
    player_name = player["name"]
    player_description = player["description"]
    player_country = player["country"]
    return f"{player_name}, a {player_description}, from {player_country}"


# Checking user guess
def check(guess, player_a, player_b):
    if player_a_followers > player_b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Make a game repeatable:
while game_should_continue:
    # Player b in the next round is player a
    player_a = player_b
    player_b = choice(data)
    while player_a == player_b:
        player_b = choice(data)

    print(f"Compare A: {format_data(player=player_a)}")
    print(vs)
    print(f"Compare B: {format_data(player=player_b)}")
    guess = input("Who has more followers? A or B ").lower()
    # Counting followers for each player:
    player_a_followers = player_a["follower_count"]
    player_b_followers = player_b["follower_count"]

    check(guess, player_a, player_b)

    os.system("clear")
    print(logo)
    # Counting score
    if check(guess, player_a, player_b):
        score += 1
        print(f"You are right! Current score: {score}")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
