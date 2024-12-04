import re

# only 14 blue cubes, 13 green cubes, and 12 red cubes
with open('puzzle-input.txt', 'r') as file:
    total_points = 0
    for card_line in file:
        winning_numbers = card_line[10:40].strip().split()
        my_numbers = card_line[41:].strip().split()
        pass
        card_points = 0
        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                card_points += 1
                print(f"{winning_number} ", end="")
        if card_points > 0:
            total_card_points = 2 ** (card_points - 1)
            total_points += total_card_points
            print(f"- {card_points} / {total_card_points} ({total_points})")
        print()
        pass
