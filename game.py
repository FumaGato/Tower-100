from time import sleep
import random


class Character:

    def __init__(self, name, hp, atk):

        self.name = name
        self.hp = hp
        self.atk = atk

    def take_dmg(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0


class Player(Character):

    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)


class Enemy(Character):

    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)


def battle(player, enemy):
    print("An enemy is attacking!")
    print("")

    turn = 1

    while player.is_alive() and enemy.is_alive():

        print(f"--- Turn {turn} ---")

        print(f"Your HP: {player.hp}")
        print(f"{enemy.name} HP: {enemy.hp}")

        print("")
        print("[z] Attack, [x] Skill, [c] Item, [v] Run")
        print("")

        action = input("Choose an action: ")

        if action == "z":
            dmg = random.randint(player.atk - 5, player.atk + 5)
            enemy.take_dmg(dmg)
            print(f"{player.name} attacks {enemy.name} for {dmg} damage!")
        elif action == "x":
            pass
        elif action == "c":
            pass
        elif action == "v":
            print(f"{player.name} trying to run")
            if random.random() < 0.66:
                print(f"{player.name} escaped!")
                break
            else:
                print(f"{player.name} failed to escape!")
        else:
            print("Invalid action, you lost your turn")

        sleep(1)

        if enemy.is_alive():
            print(f"{enemy.name} is attacking!")

            sleep(1)

            dmg = random.randint(enemy.atk - 5, enemy.atk + 5)
            player.take_dmg(dmg)
            print(f"{enemy.name} hit {player.name} for {dmg} damage!")

            sleep(1)

        turn += 1

        if not player.is_alive():
            print("You lost")
            break

        if not enemy.is_alive():
            print(f"You defeated {enemy.name}")
            sleep(1)
            print("You win")
            break


def menu_act():
    while True:
        value = input(">")
        if value == "":
            print("Choose an action: ")
        else:
            try:
                return int(value)
            except ValueError:
                print("That's not a number")


# Player
player_name = input("Enter your name: ")
player = Player(player_name, 100, 25)

# Enemies
roco = Enemy("Roco", 40, 20)
dodo = Enemy("Dodo", 60, 10)
fufu = Enemy("Fufu", 20, 50)

# Menu
print("Escape from This Place But You Can't See Anything Game")
print("(1) Start")
print("(2) Tutorial")
print("(3) Exit")

menu = menu_act()

if menu == 1:
    battle(player, roco)
elif menu == 2:
    print(player.atk)
elif menu == 3:
    exit
