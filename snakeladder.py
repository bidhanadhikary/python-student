import random
from termcolor import colored

dice_face = [1,2,3,4,5,6]
snakes = {16: 6, 46: 25, 49: 11, 62: 19, 64: 60,
          74: 53, 89: 68, 92: 88, 95: 75, 99: 80}
ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42,
           28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}

num_players = int(input("Enter the number of players: "))
players = []

# How many players will join the game?
for i in range(num_players):
    name = input(f"Enter player {i+1} name: ")
    player = {
        'name': name,
        'score': 0,
        'state': 0,
        'history': []
    }
    players.append(player)

print(players)

# Game Starts
game_over = False
while not game_over:
    for p in players:
        value = random.choice(dice_face)

        # Rolling for 1 to gain entry qualification
        if p['state'] == 0:
            while value == 6:
                print(f"{p['name']} rolled a 6 and gets a free additional roll.")
                value = random.choice(dice_face)
            if value == 1:
                # Player rolled a 1 and can start playing
                p['state'] = 1
                p['score'] = 1
                print(f"{p['name']} rolled a {value}. New score: {p['score']}. GAME ON!")

                # Code to repeat turn
                while value in [1, 6]:
                    print(f"{p['name']} gets to continue play due to a die roll of {value}.")
                    value = random.choice(dice_face)
                    p['score'] += value
                    print(f"{p['name']} rolled a {value}. New score: {p['score']}.")
                    pass

            else:
                print(f"{p['name']} rolled a {value}. NEEDS TO ROLL A 1 TO START!")

        # Player is on field and progressing across the board
        elif p['state'] == 1:
            next_value = p['score'] + value

            if next_value <= 100:
                p['score'] += value
                print(f"{p['name']} rolled a {value}. New score: {p['score']}")

                # Check if player landed on a snake or ladder
                for head, tail in snakes.items():
                    if p['score'] == head:
                        p['score'] = tail
                        print(f"Oh no! There was a snake at block {head}. {p['name']} ran back to {tail} to escape!")
                for base, top in ladders.items():
                    if p['score'] == base:
                        p['score'] = top
                        print(f"{p['name']} found a ladder at block {base} and climbed to {top}. Noice!")

                # Check if one player has ejected another player
                for r in players:
                    if r['name'] != p['name'] and r['score'] == next_value:
                        r['score'] = 0
                        r['state'] = 0
                        print(f"OH NOES!!! {p['name']} HAS EJECTED {r['name']}!!!")

                # Code to repeat turn
                while value in [1, 6]:
                    print(f"{p['name']} gets to continue play due to a die roll of {value}.")
                    value = random.choice(dice_face)
                    p['score'] += value
                    print(f"{p['name']} rolled a {value}. New score: {p['score']}.")

                    # Did score exceed 100?
                    if p['score'] > 100:
                        p['score'] -= value
                        print(f"Score exceeded 100! Invalid! Score: {p['score']}")

                    # Win Condition. Someone scored 100!
                    if p['score'] == 100:
                        p['state'] = 2
                        game_over = True

                        print(colored(f"{p['name']} WON!", "red", "on_green"))
                        print("Final Scores")
                        print(players)
                        break

                    # Check if player landed on a snake or ladder
                    for head, tail in snakes.items():
                        if p['score'] == head:
                            p['score'] = tail
                            print(
                                f"Oh no! There was a snake at block {head}. {p['name']} ran back to {tail} to escape!")
                    for base, top in ladders.items():
                        if p['score'] == base:
                            p['score'] = top
                            print(f"{p['name']} found a ladder at block {base} and climbed to {top}. Noice!")

                    # Check if one player has ejected another player
                    for r in players:
                        if r['name'] != p['name'] and r['score'] == next_value:
                            r['score'] = 0
                            r['state'] = 0
                            print(f"OH NOES!!! {p['name']} HAS EJECTED {r['name']}!!!")
                    pass


            # Score exceeds 100 and score is invalidated
            else:
                print(f"{p['name']} rolled a {value}. Score exceeded 100! Invalid! Score: {p['score']}")

                # Code to repeat turn
                if value in [1, 6]:
                    print(f"{p['name']} gets to continue play due to a die roll of {value}.")
                    value = random.choice(dice_face)
                    p['score'] += value
                    print(f"{p['name']} rolled a {value}. New score: {p['score']}.")
                    pass

        # Win Condition. Someone scored 100!
        if p['score'] == 100:
            p['state'] = 2
            game_over = True

            print(colored(f"{p['name']} WON!", "red", "on_green"))
            print("Final Scores")
            print(players)
            break


