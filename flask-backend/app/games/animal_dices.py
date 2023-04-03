from random import choice
import time

dice1_results = ["Gourd", "Crab", "Shrimp", "Fish", "Chicken", "Deer"]
dice2_results = ["Gourd", "Crab", "Shrimp", "Fish", "Chicken", "Deer"]
dice3_results = ["Gourd", "Crab", "Shrimp", "Fish", "Chicken", "Deer"]

animal_emojis = {
    "Gourd": "🎃",
    "Crab": "🦀",
    "Shrimp": "🦐",
    "Fish": "🐟",
    "Chicken": "🐔",
    "Deer": "🦌",
}

def play_animal_dices(emoji_mode=False, roll=True):
    if not roll:
        return

    dice1 = choice(dice1_results)
    dice2 = choice(dice2_results)
    dice3 = choice(dice3_results)
    
    results = [dice1, dice2, dice3]
    animal_counts = {animal: results.count(animal) for animal in set(results)}

    if emoji_mode:
        result_str = ", ".join([f"{count} {animal_emojis[animal]}" for animal, count in animal_counts.items()])
    else:
        result_str = ", ".join([f"{count} {animal}" for animal, count in animal_counts.items()])

    return result_str
