import random

guess_num = []

diff = 0
tries = 0

print("Hello! What is your name?: ")
userName = input()

play = True

while play:
    print(
    """Three levels of difficulty:
    Level 1 => easy (e)
    Level 2 => medium (m)
    Level 3 => hard (h)
    """)
    level = input("Welcome {}, What level of difficulty do you want to play?[e/m/h]: " .format(userName))

    if level == "e":
        diff = 10
        tries = 6
        break
    elif level == "m":
        diff = 20
        tries = 4
        break
    else:
        if level == "h":
            diff = 50
            tries = 3
    break
rand_num = random.randint(1, diff)
print("You are entitled to {} guess" .format(tries))
while len(guess_num) < tries:
    guess = input("Guess a number between 1 and {}: ".format(diff))

    try:
        player_num = int(guess)
    except:
        print("I dont understand that! an invalid input.")
        continue

    if not player_num > 0 or not player_num <= diff:
        print("Please guess a number between 1 and {}: ".format(diff))
        continue

    guess_num.append(player_num)
    tries_left = tries - len(guess_num)
    if player_num == rand_num:
        print("You are right! The number was {}: " .format(rand_num))
        print("It took you {} tries." .format(len(guess_num)))
        break
    else:
        if rand_num > player_num:
            print("That was wrong. The number is higher than {}. Guess #{}. You have {} guesses left" .format(player_num, len(guess_num), tries_left))
        else:
            print("That was wrong. The number is lower than {}. Guess #{}. You have {} guesses left" .format(player_num, len(guess_num), tries_left))
        continue
if not rand_num in guess_num:
    print("Game Over! The number I was thinking is {}." .format(rand_num))
