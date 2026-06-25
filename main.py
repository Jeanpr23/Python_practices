import json
import datetime

# --------- MEMORY ---------

try:
    with open("memory.json", "r") as file:
        memory = json.load(file)

except:
    memory = {}

# --------- ----------

if "adress" not in memory:
    memory["adress"] = ""

elif "city" not in memory:
    memory["city"] = ""

elif "state" not in memory:
    memory["state"] = ""

elif "country" not in memory:
    memory["country"] = ""

elif "favorite_game" not in memory:
    memory["favorite_game"] =[]

elif "name" not in memory or memory["name"] == "":
    name = input("What is your name? ")
    memory["name"] = name

elif "birth_country" not in memory:
    memory["birth_country"] = ""

elif "birthday" not in memory:
    memory["birthday"] = ""

def save_memory():
    with open("memory.json", "w") as file:
        json.dump(memory, file)
# --------------------------

current_year = datetime.datetime.now().year

birthday = memory["birthday"]
birth_year = int(birthday.split("-")[0])

age = current_year - birth_year


while True:

    question = input("You: ")
    question = question.lower()


# EXIT CHECK --------

    if question == "bye":
        save_memory()
        break

# ------------
    elif question == "hello":
        print("Computer Friend: Hi", memory["name"])

    elif "my favorite game is" in question:
        favorite_game = question.replace("my favorite game is", "").strip()
        memory["favorite_game"].append(favorite_game)
        print("Computer Friend: got it, I will remember", favorite_game)

    elif question == "my favorite games?":
        print("Computer Friend:", ", ".join(memory["favorite_game"]))

    elif "my adress is" in question:
        adress = question.replace("my adress is", "").strip()
        memory["adress"] = (adress)
        print("Computer Friend: got it, I will remember", adress)

    elif question == "my adress is?":
        print("Computer Friend: Your adress is", memory["adress"])

    elif "my city is" in question:
        city = question.replace("my city is", "").strip()
        memory["city"] = (city)
        print("Computer Friend: got it, I will remember", city)

    elif question == "my city?":
        print("Computer Friend: Your city is", memory["city"])

    elif "my state is" in question:
        state = question.replace("my state is", "").strip()
        memory["state"] = (state)
        print("Computer Friend: got it, I will remember", state)

    elif question == "my state?":
        print("Computer Friend: Your state is", memory["state"])

    elif "my country is" in question:
        country = question.replace("my country is", "").strip()
        memory["country"] = (country)
        print("Computer Friend: got it, I will remember", country)

    elif question == "my country?":
        print("Computer Friend: Your country is", memory["country"])

    elif "im from" in question:
        birth_country = question.replace("im from", "")
        memory["birth_country"] = (birth_country)
        print("Computer Friend: got it, I will remember", birth_country)

    elif question == "my birth country?":
        print("Computer Friend: You are from", memory["birth_country"])

    elif question == "how do you know that?":
        print("Computer Friend: because you teach me that :)")

    elif question == "my age?":
        print("Computer Friend: You are", age)

    elif question == "in what year i was born?":
        print("Computer Friend: You where born in", birth_year)