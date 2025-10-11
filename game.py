import random
from time import sleep
from sys import exit


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

    def take_item(self, new_item):

        if new_item:
            self.inv.append(new_item)

    def theres_item(self, item):
        print(f"There's a {item.name} on the floor.")
        sleep(1)
        print("")
        print("[z] Take, [Enter] Leave.")
        print("")
        act = input("Choose an action: ")
        print("")
        if act == "z":
            player.take_item(item)
            print(
                f"You took the {item.name}.")
            sleep(1)
            print(f"{item.name} added to inventory.")
        else:
            print(f"You leave the {item.name}.")

    def theres_item_enemy(self, item):
        print(f"{self.name} drops a {item.name} on the floor.")
        sleep(1)
        print("")
        print("[z] Take, [Enter] Leave.")
        print("")
        act = input("Choose an action: ")
        if act == "z":
            player.take_item(item)
            print("")
            print(
                f"You took the {item.name}.")
            sleep(1)
            print(f"{item.name} added to inventory.")
        else:
            print("")
            print(f"You leave the {item.name}.")
        sleep(1)


class Enemy(Character):

    def __init__(self, name, hp, atk, desc):

        super().__init__(name, hp, atk)
        self.desc = desc

    def drop_item(self):

        chance = random.random()

        if chance < 0.2:
            template = random.choice(common_items)
            drop = Item(template.name, template.heal_amount, template.atk)
            player.theres_item_enemy(drop)
        elif chance > 0.15 and chance <= 0.22:
            template = random.choice(rare_items)
            drop = Item(template.name, template.heal_amount, template.atk)
            player.theres_item_enemy(drop)
        elif chance > 0.22 and chance < 0.25:
            template = random.choice(super_rare_items)
            drop = Item(template.name, template.heal_amount, template.atk)
            player.theres_item_enemy(drop)
        else:
            pass


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
    exit("Exited. Player died.")


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
        print("[z] Attack, [x] Inspect, [c] Inventory, [v] Run.")
        print("")

        action = input("Choose an action: ")
        print("")

        if action == "z":
            dmg = random.randint(player.atk - 5, player.atk + 5)
            enemy.take_dmg(dmg)
            print(f"{player.name} attacks {enemy.name} for {dmg} damage!")
        elif action == "c":
            print("--- Stats ---")
            print(f"HP: {player.hp}")
            print(f"ATK: {player.atk} ({player.weapon.name})")
            print("--- Inventory ---")
            for item in player.inv:
                if item.heal_amount > 0:
                    print(f"- {item.name} (heal for {item.heal_amount} HP)")
                elif item.atk > 0:
                    print(f"- {item.name} (deal {item.atk} damage)")
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
                elif used.atk > 0:
                    print("You can't switch weapon mid battle!")
                else:
                    print("You can't use that item.")
            elif use == "":
                print("For some reason you decided to not use any item.")
            else:
                print(f"There's no {use} in your inventory.")
        elif action == "x":
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
            enemy.drop_item()
            print("You win the battle!")
            return

        turn += 1


def menu_act():

    while True:
        print("")
        value = input("Choose an action: ")
        print("")
        if value == "":
            print("Invalid action.")
        else:
            try:
                return int(value)
            except ValueError:
                print("Invalid action.")


def game():

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
                template = random.choice(enemies_lv1)
                encounter = Enemy(template.name, template.hp,
                                  template.atk, template.desc)
                battle(player, encounter)
            elif floor_encounter > 0.5 and floor_encounter <= 0.65:
                template = random.choice(common_items)
                encounter = Item(
                    template.name, template.heal_amount, template.atk)
                player.theres_item(encounter)
            elif floor_encounter > 0.65 and floor_encounter <= 0.72:
                template = random.choice(rare_items)
                encounter = Item(
                    template.name, template.heal_amount, template.atk)
                player.theres_item(encounter)
            elif floor_encounter > 0.72 and floor_encounter <= 0.75:
                template = random.choice(super_rare_items)
                encounter = Item(
                    template.name, template.heal_amount, template.atk)
                player.theres_item(encounter)
            else:
                print("Nothing.")
        elif act == "c":
            print("--- Stats ---")
            print(f"HP: {player.hp}")
            print(f"ATK: {player.atk} ({player.weapon.name})")
            print("--- Inventory ---")
            for item in player.inv:
                if item.heal_amount > 0:
                    print(f"- {item.name} (heal for {item.heal_amount} HP)")
                elif item.atk > 0:
                    print(f"- {item.name} (deal {item.atk} damage)")
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
            elif use == "":
                print("Inventory closed.")
            else:
                print(f"There's no {use} in your inventory.")
        else:
            print("Invalid action.")

        sleep(1)


# --- Items ---

# *item* = Item("*item_name*", *item_heal_amount*, *item_atk*)

# Common
bread = Item("Bread", 20, 0)
bandage = Item("Bandage", 30, 0)

stick = Item("Stick", 0, 10)
wooden_sword = Item("Wooden Sword", 0, 20)

phone = Item("Phone", 0, 0)
rock = Item("Piece of rock", 0, 0)

# Rare
sword = Item("Normal Sword", 0, 30)

# Super rare
good_sword = Item("Good Sword", 0, 40)

common_items = [
    bread,
    bandage,
    wooden_sword,
    rock
]

rare_items = [
    sword
]

super_rare_items = [
    good_sword
]

# --- Player ---
player_name = input("Enter your name: ")
player_inventory = [
    bread
]
player = Player(player_name, 100, stick.atk, player_inventory, 0, 0)
player.weapon = stick

# --- Enemies ---
roco_desc = "Looks like an armadillo."
roco = Enemy("Roco", 30, 15, roco_desc)
dodo_desc = "A bird? Definately a bird."
dodo = Enemy("Dodo", 40, 10, dodo_desc)
fufu_desc = "I don't know what that is."
fufu = Enemy("Fufu", 25, 20, fufu_desc)

enemies_lv1 = [
    roco, dodo, fufu
]

# --- Menu ---
print("")
print("--- Tower 100 ---")
print("[1] Start")
print("[2] Tutorial")
print("[3] Exit")

while True:
    menu = menu_act()
    if menu == 1:
        game()
    elif menu == 2:
        print("There's no tutorial yet.")
    elif menu == 3:
        exit("Exited.")
    else:
        print("Invalid action.")
