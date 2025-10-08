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

    def __init__(self, name, hp, atk, inv):

        super().__init__(name, hp, atk)
        self.inv = inv

    def heal(self, amount):

        self.hp += amount


class Enemy(Character):

    def __init__(self, name, hp, atk, desc):

        super().__init__(name, hp, atk)

        self.desc = desc


class Item():

    def __init__(self, name, heal_amount):

        self.name = name
        self.heal_amount = heal_amount


def battle(player, enemy):

    print("An enemy is attacking!")
    sleep(1)
    print("")

    turn = 1

    while player.is_alive() and enemy.is_alive():

        print(f"--- Turn {turn} ---")

        print(f"Your HP: {player.hp}")
        # print(f"{enemy.name} HP: {enemy.hp}")

        print("")
        print("[z] Attack, [x] Item, [c] Inspect, [v] Run")
        print("")

        action = input("Choose an action: ")
        print("")

        if action == "z":
            dmg = random.randint(player.atk - 5, player.atk + 5)
            enemy.take_dmg(dmg)
            print(f"{player.name} attacks {enemy.name} for {dmg} damage!")
        elif action == "x":
            print("--- Inventory ---")
            for item in player.inv:
                if item.heal_amount > 0:
                    print(f"{item.name} (heal for {item.heal_amount} HP)")
                else:
                    print(item.name)
            print("")
            use = input("Use wich item? : ")
            if use in player.inv:
                if use.heal_amount > 0:
                    player.heal(use.heal_amount)
                    print(
                        f"{player.name} healed using {use.name} for {use.heal_amount} HP")
                else:
                    print("You can't use that item")
            else:
                print(f"There's no {use} in inventory")
        elif action == "c":
            print(f"You're inspecting {enemy.name}...")
            sleep(1)
            print("")
            print(f"--- {enemy.name} ---")
            print(f"{enemy.hp} HP")
            print(f"{enemy.atk} attack")
            print(enemy.desc)
            print("")
        elif action == "v":
            print(f"{player.name} trying to run")
            sleep(1)
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
            print("")

        turn += 1

        if not player.is_alive():
            print("You died.")
            sleep(1)
            break

        if not enemy.is_alive():
            print(f"{player.name} defeated {enemy.name}")
            sleep(1)
            print("You win the battle!")
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


# Items
bread = Item("Bread", 20)
bandage = Item("Bandage", 30)
stick = Item("Stick", 0)

# Player
player_name = input("Enter your name: ")
player_inventory = [bread, bandage, stick]
player = Player(player_name, 100, 25, player_inventory)

# Enemies
roco_desc = "Looks like an armadillo"
roco = Enemy("Roco", 45, 35, roco_desc)
dodo_desc = "A bird?"
dodo = Enemy("Dodo", 60, 20, dodo_desc)
fufu_desc = "I don't know what that is"
fufu = Enemy("Fufu", 50, 40, fufu_desc)

enemies = [roco, dodo, fufu]

encounter = random.choice(enemies)

# Menu
print("Escape from This Place But You Can't See Anything Game")
print("[1] Start")
print("[2] Tutorial")
print("[3] Exit")

while True:
    menu = menu_act()
    if menu == 1:
        print("You're stuck in this place")
        sleep(1)
        print("You must get out of here")
        sleep(1)
        walk = input("Press enter to continue walking")
        battle(player, encounter)
    elif menu == 2:
        print("There's no tutorial yet")
    elif menu == 3:
        break
