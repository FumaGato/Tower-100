from time import sleep
import random
import sys


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

    def __init__(self, name, hp, atk, inv, floor, enemy_defeated):

        super().__init__(name, hp, atk)
        self.inv = inv
        self.floor = floor
        self.enemy_defeated = enemy_defeated
        self.weapon = None

    def heal(self, amount):

        self.hp += amount

    def update_hp(self):

        if self.hp > 100:
            self.hp = 100

    def equip(self, new_weapon):

        if new_weapon == self.weapon:
            print(f"{new_weapon.name} is already equipped.")
            return

        if self.weapon:
            self.inv.append(self.weapon)

        self.weapon = new_weapon
        self.atk = new_weapon.atk

        if new_weapon in self.inv:
            self.inv.remove(new_weapon)

        print(f"{self.name} equipped {new_weapon.name}! ATK is now {self.atk}.")


class Enemy(Character):

    def __init__(self, name, hp, atk, desc):

        super().__init__(name, hp, atk)
        self.desc = desc


class Item():

    def __init__(self, name, heal_amount, atk):

        self.name = name
        self.heal_amount = heal_amount
        self.atk = atk


def result():

    print("")
    print("--- Result ---")
    print(f"Enemy defeated: {player.enemy_defeated}")
    print(f"Floor: {player.floor}")
    print("")

    done = input("Press [Enter] to quit.")

    print("")
    sys.exit("Exited. Player died.")


def battle(player, enemy):

    print("An enemy is approaching!")
    sleep(1)
    print("")

    turn = 1

    while player.is_alive() and enemy.is_alive():

        print(f"--- Turn {turn} ---")

        print(f"Your HP: {player.hp}")
        print(f"{enemy.name} HP: {enemy.hp}")

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
            use = input("Use wich item? : ").lower()
            print("")
            used = None
            for item in player.inv:
                if item.name.lower() == use:
                    used = item
            if used:
                if used.heal_amount > 0:
                    if player.hp < 100:
                        player.heal(used.heal_amount)
                        print(
                            f"{player.name} healed using {used.name} for {used.heal_amount} HP.")
                        player.inv.remove(used)
                        sleep(1)
                        player.update_hp()
                        print(f"{player.name} HP is now {player.hp}.")
                    else:
                        print("Your HP is full!")
                elif used.aTK > 0:
                    PRINT("You can't use that right now.")
                else:
                    print("You can't use that item.")
            else:
                print(f"There's no {use} in your inventory.")
        elif action == "c":
            print(f"You're inspecting {enemy.name}...")
            sleep(1)
            print("")
            print(f"--- {enemy.name} ---")
            print(f"{enemy.hp} HP")
            print(f"{enemy.atk} attack")
            sleep(1)
            print("")
            print(enemy.desc)
        elif action == "v":
            print(f"{player.name} trying to run.")
            sleep(1)
            if random.random() < 0.66:
                print(f"{player.name} escaped!")
                break
            else:
                print(f"{player.name} failed to escape!")
        else:
            print("Invalid action, you lost your turn.")

        sleep(1)

        if enemy.is_alive():
            print("")
            print(f"{enemy.name} is attacking!")
            sleep(1)
            dmg = random.randint(enemy.atk - 5, enemy.atk + 5)
            player.take_dmg(dmg)
            print(f"{enemy.name} hit {player.name} for {dmg} damage!")
            sleep(1)
            print("")

        if not player.is_alive():
            print("You died.")
            sleep(1)
            result()

        if not enemy.is_alive():
            player.enemy_defeated += 1
            print(f"{player.name} defeated {enemy.name}.")
            sleep(1)
            print("You win the battle!")
            return

        turn += 1


def menu_act():

    while True:
        value = input("Choose an action: ")
        if value == "":
            print("Invalid action.")
        else:
            try:
                return int(value)
            except ValueError:
                print("Invalid action.")


def game():

    print("")
    print("So bassicaly you decided to climb this tower...")
    sleep(1)
    print("And...")
    sleep(1)
    print("Yeah...")
    sleep(1)

    while True:
        print("")
        print("[Enter] Next floor, [c] Inventory.")
        print("")
        act = input("Choose an action: ")
        print("")
        if act == "":
            player.floor += 1
            print(f"--- Floor {player.floor} ---")
            floor_encounter = random.random()
            if floor_encounter < 0.5:
                template = random.choice(enemies)
                encounter = Enemy(template.name, template.hp,
                                  template.atk, template.desc)
                battle(player, encounter)
            else:
                print("There's no one.")
        elif act == "c":
            print("--- Stats ---")
            print(f"HP: {player.hp}")
            print(f"ATK: {player.atk} ({player.weapon.name})")
            print("--- Inventory ---")
            for item in player.inv:
                if item.heal_amount > 0:
                    print(f"- {item.name} (Heal for {item.heal_amount} HP)")
                elif item.atk > 0:
                    print(f"- {item.name} (Deal {item.atk} damage)")
                else:
                    print(f"- {item.name}")
            print("")
            use = input("Use wich item? : ").lower()
            print("")
            used = None
            for item in player.inv:
                if item.name.lower() == use:
                    used = item
            if used:
                # Healing
                if used.heal_amount > 0:
                    if player.hp < 100:
                        player.heal(used.heal_amount)
                        print(
                            f"{player.name} healed using {used.name} for {used.heal_amount} HP.")
                        player.inv.remove(used)
                        sleep(1)
                        player.update_hp()
                        print(f"{player.name} HP is now {player.hp}.")
                    else:
                        print("Your HP is full!")

                # Switch weapon
                elif used.atk > 0:
                    player.equip(used)

                # Non-usable item
                else:
                    print("You can't use that item.")
            else:
                print(f"There's no {use} in your inventory.")

        sleep(1)


# Items

# *item* = Item("*item_name*", *item_heal_amount*, *item_atk*)

bread = Item("Bread", 40, 0)
bandage = Item("Bandage", 55, 0)

stick = Item("Stick", 0, 25)
wooden_sword = Item("Wooden Sword", 0, 35)

phone = Item("Phone", 0, 0)

# Player
player_name = input("Enter your name: ")
player_inventory = [
    bread,
    bandage,
    wooden_sword,
    phone
]
player = Player(player_name, 100, stick.atk, player_inventory, 0, 0)
player.weapon = stick

# Enemies
roco_desc = "Looks like an armadillo."
roco = Enemy("Roco", 45, 35, roco_desc)
dodo_desc = "A bird?"
dodo = Enemy("Dodo", 60, 20, dodo_desc)
fufu_desc = "I don't know what that is."
fufu = Enemy("Fufu", 40, 40, fufu_desc)

enemies = [roco, dodo, fufu]

# Menu
print("")
print("--- Tower 100 ---")
print("[1] Start")
print("[2] Tutorial")
print("[3] Exit")
print("")

while True:
    menu = menu_act()
    if menu == 1:
        game()
    elif menu == 2:
        print("")
        print("There's no tutorial yet")
        print("")
    elif menu == 3:
        print("")
        sys.exit("Exited.")
