import random

part_1 = [
    "生麦",
    "赤猫",
    "白砂",
    "青空",
    "小鳥"
]


part_2 = [
    "生米",
    "黒猫",
    "白猫",
    "早口",
    "新鮮"
]


part_3 = [
    "生卵",
    "走る猫",
    "飛ぶ鳥",
    "笑う人",
    "歌う子"
]

def generate_japanese_twister():

    a = random.choice(part_1)
    b  = random.choice(part_2)
    c = random.choice(part_3)

    sentence = f"{a}{b}{c}。"

    return sentence


for i in range(10):
    print(generate_japanese_twister())