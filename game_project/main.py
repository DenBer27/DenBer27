from heroes import get_attack_power
from heroes import Human, Dwarf, Elf

import random
from warriors import Knight, Archer, Spy
import time


def main():
    global race1, race2
player1_name = input("Игрок 1 введите ваше имя: ")
player2_name = input("Игрок 2 введите ваше имя: ")
print("""Выберите расу героя:
    Человек (Human) - цифра 1
    Гном (Dwarf) - цифра 2
    Эльф (Elf) - цифра 3
    """)


def create_hero1():
    global player1_hero, player1_hero_name
    race1 = int(input(f"Игрок {player1_name} введите номер расы: "))
    if race1 == 1:
        race = "Human"
        player1_hero_name = "Human"
        player1_hero = Human(race, player1_hero_name)
    elif race1 == 2:
        race = "Dwarf"
        player1_hero_name = "Dwarf"
        player1_hero = Dwarf(race, player1_hero_name)
    elif race1 == 3:
        race = "Elf"
        player1_hero_name = "Elf"
        player1_hero = Elf(race, player1_hero_name)

    print(f"{player1_name} создал героя расы '{player1_hero_name}', сила: {player1_hero.attack_power}, здоровье: {player1_hero.health}")
    return player1_hero

def create_hero2():
    global player2_hero, player2_hero_name
    race2 = int(input(f"\nИгрок {player2_name} введите номер расы: "))
    if race2 == 1:
        race = "Human"
        player2_hero_name = "Human"
        player2_hero = Human(race, player2_hero_name)
    elif race2 == 2:
        race = "Dwarf"
        player2_hero_name = "Dwarf"
        player2_hero = Dwarf(race, player2_hero_name)
    elif race2 == 3:
        race = "Elf"
        player2_hero_name = "Elf"
        player2_hero = Elf(race, player2_hero_name)

    print(f"Игрок {player2_name} создал героя расы '{player2_hero_name}', сила: {player2_hero.attack_power}, здоровье: {player2_hero.health}")
    return player2_hero

def attack_turn_based(player1_hero, player2_hero):
    while True:
        if player1_hero.health <= 0:
            print(f"Герой игрока {player1_name} пал смертью храбрых!")
            break
        elif player2_hero.health <= 0:
            print(f"Герой игрока {player2_name} побежден, но не будет забыт!!")
            break

        time.sleep(1)
        player1_attack = input(f"\nХод игрока {player1_name}. Атаковать? (Y/N): ").upper()
        if player1_attack == "Y":
            player1_hero.attack_power = get_attack_power(player1_hero.attack_power, player1_hero.attack_power + 3)
            player2_hero.health -= player1_hero.attack_power
            player2_hero.health += player2_hero.defence
            print(f"{player1_name}('{player1_hero_name}') атакует. Удар!")
            time.sleep(1)
            print(f"Урон {player1_hero.attack_power}")
            time.sleep(1)
            print(f"\nСработал щит: {player2_hero.defence}\nОстаток здоровья героя игрока {player2_name} ('{player2_hero_name}'): {player2_hero.health}")

        time.sleep(1)
        player2_attack = input(f"\nХод игрока {player2_name}. Атаковать? (Y/N): ").upper()
        if player2_attack == "Y":
            player2_hero.attack_power = get_attack_power(player2_hero.attack_power, player2_hero.attack_power + 3)
            player1_hero.health -= player2_hero.attack_power
            player1_hero.health += player1_hero.defence
            print(f"{player2_name} ('{player2_hero_name}') атакует. Удар!")
            time.sleep(1)
            print(f"Урон {player2_hero.attack_power}")
            time.sleep(1)
            print(f"\nСработал щит: {player1_hero.defence}\nОстаток здоровья героя {player1_name} ('{player1_hero_name}'): {player1_hero.health}")
        elif player1_attack == "N":
            break

def create_team():
    time.sleep(2)
    global team1, team2
    lst_warriors = [Knight(), Archer(), Spy()]
    team1 = str([random.choice(lst_warriors) for i in range(5)])
    print(f"\nОтряд Игрока {player1_name}: {team1}")

    team2 = str([random.choice(lst_warriors) for i in range(5)])
    print(f"\nОтряд Игрока {player2_name}: {team2}")
    return team1, team2


if __name__ == "__main__":
    main()
    create_hero1()
    create_hero2()
    # create_team()
    attack_turn_based(player1_hero, player2_hero)

