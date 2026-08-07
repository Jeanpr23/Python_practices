import random


word_group_1 = [
    "Шесть",
    "Шустрых",
    "Шумных",
    "Шальных",
    "Шёлковых"

]


word_group_2 = [
    "шмелей",
    "шершней",
    "шутников",
    "шофёров",
    "шариков"

]


word_group_3 = [
    "шумно шуршат",
    "шепчут шёпотом",
    "быстро шагают",
    "шустро шевелятся",
    "сильно шумят"
]


word_group_4 = [
    "в шелковице",
    "в широком шкафу",
    "в старом шалаше",
    "на шумной улице",
    "около школы"
]


def generate_russian_twister():

    part1 = random.choice(word_group_1)
    part2 = random.choice(word_group_2)
    part3 = random.choice(word_group_3)
    part4 = random.choice(word_group_4)

    sentence = f"{part1} {part2} {part3} {part4}."


    return sentence

for i in range(10):
    print(generate_russian_twister())
