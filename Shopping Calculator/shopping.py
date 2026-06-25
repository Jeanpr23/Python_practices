prices = {
    "molde": 2.17,

    "jamon": 5.44,

    "hotdogs": 5.44,

    "limon": 0.20,

    "jugo de fruitpunch": 2.50,

    "jugo de china": 2.29,

    "7up": 2.49,

    "m&m": 1.99,

    "kinder bueno": 1.99,

    "aguacate": 2.50,

    "leche mediana": 3.49


}

total = 0

while True:

 item = input("Enter item (or type done): ")

 if item == "done":
  break

 total = total + prices[item]

 print("Added:", item)

 print("Total: $", total)