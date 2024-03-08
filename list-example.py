import random

fruit = ["apple", "banana", "cherry"]
fruit.append("date")
fruit.extend(["elderberry", "fig", "grape"])
fruit += ["honeydew", "kiwi", "lemons"]

print(fruit)

random_fruits = random.choice(fruit)
while True:
    fruit = random.choice(fruit)
    like = input(f"Do you like the {fruit}? (yes/no/stop) ")
    if like.lower() == "yes":
        new_fruit = input(f"Name another fruit to add: ")
        fruit.append(new_fruit)
    elif like.lower() == "no":
        print(f"Removing {fruit} from the list")
        fruit.remove(fruit)
    elif like.lower() == "stop":
        break
with open("fruits.txt", "w") as fd:
    for fruit in fruits:
        fd.write(fruit +"\n")