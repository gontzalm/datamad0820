import random
import platform
import os
from vikingsClasses import Saxon, Viking, War

HP_POOL_SAXON = list(range(50, 101))
STR_POOL_SAXON = list(range(10, 21))
NAME_POOL = ["Bjorn", "Helga", "Flokki", "Ragnar", "Lagertha", "Frode"]
HP_POOL_VIKING = list(range(250, 351))
STR_POOL_VIKING = list(range(50, 101))

def clear():
    """Clear terminal."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class MyWar(War):
    """My customized war class"""

    def __init__(self, name=""):
        super().__init__()
        self.name = name
        self.saxons = 0
        self.vikings = 0

    def add_random(self, qtty, **pool):
        """Generic function to add random soldiers"""

        for i in range(qtty):
            attributes = [random.choice(pool[attr]) for attr in pool]
            if "name" in pool.keys():
                viking = Viking(*attributes)
                print(f"{viking.name} has joined the army!")
                print(viking.battleCry())
                super().addViking(viking)
            else:
                saxon = Saxon(*attributes)
                super().addSaxon(saxon)

    def add_random_saxons(self, qtty=1, hp_pool=HP_POOL_SAXON, str_pool=STR_POOL_SAXON):
        """Function to add Saxons with random attributes"""

        self.add_random(qtty, hp=hp_pool, str=str_pool)
        if qtty == 1:
            print("A frightened Saxon has joined the Saxon Army.")
        else:
            print(f"{qtty} frightened Saxons have joined the Saxon Army.")
    
    def add_random_vikings(self, qtty=1, name_pool=NAME_POOL, hp_pool=HP_POOL_VIKING, str_pool=STR_POOL_VIKING):
        """Function to add Vikings with random attributes"""

        self.add_random(qtty, name=name_pool, hp=hp_pool, str=str_pool)
        if qtty != 1:
            print(f"{qtty} brave Vikings have joined the Viking Army.")
    
    def battle(self):
        """Function to produce a battle"""

        print("Battle Results".center(80, "-"))
        print(self.saxonAttack())
        if self.vikingArmy:
            print(self.vikingAttack())

    def show_army(self, soldier_type):
        """Function that shows army"""

        print(f"{soldier_type.title()} army".center(80, "-"))
        for i, soldier in enumerate(getattr(self, soldier_type + "Army")):
            if hasattr(soldier, "name"):
                print(f"{soldier.name} HP: {soldier.health} STR: {soldier.strength}".center(80))
            else:
                print(f"Soldier {i+1} HP: {soldier.health} STR: {soldier.strength}".center(80))

    def showStatus(self):
        print(f"{self.name.title()}'s Status:".center(80, "-"))
        print(super().showStatus().center(80))
        print(f"Total Saxons left: {len(self.saxonArmy)}".center(80))
        print(f"Total Vikings left: {len(self.vikingArmy)}".center(80))
        self.show_army("saxon")
        self.show_army("viking")


class Game():
    """Game class"""

    def __init__(self):
        self.name = "VIKING WAR SIMULATOR"
        self.author = "Gontz"
        self.version = "1.0"
        self.saxons = 0
        self.vikings = 0
        self.war = MyWar()

    def show_header(self):
        """Show the game header"""

        clear()
        header = f"[{self.name} v{self.version} by {self.author}]"
        print(header.center(80, "_"))
        print()

    def prompt_name(self):
        """Function to prompt the name"""

        while True:
            self.show_header()
            prompt = f"Select war name: "
            try:
                name = input(prompt)
                if name.isnumeric():
                    raise ValueError
                if name.lower() == "war":
                    raise Exception
            except ValueError:
                print("Please, input a valid name")
                input()
            except Exception:
                print("Please, be more creative with the name!!")
                input()
            else:
                setattr(self.war, "name", name)
                break

    def prompt_army(self, soldier_type):
        """Function to prompt army size"""

        while True:
            self.show_header()
            prompt = f"Select number of {soldier_type.title()}: "
            try:
                n = int(input(prompt))
            except ValueError:
                print("Please, input an integer")
                input()
            else:
                setattr(self.war, soldier_type, n)
                break
    
    def execute(self):
        """Function to produce the final clash"""

        self.show_header()
        print(f"{self.war.name} has started...")
        self.war.add_random_saxons(self.war.saxons)
        self.war.add_random_vikings(self.war.vikings)
        input(f"\nPress ENTER to start {self.war.name}")
        while True:
            self.show_header()
            if self.war.saxonArmy and self.war.vikingArmy:
                self.war.battle()
            self.war.showStatus()
            if not self.war.saxonArmy or not self.war.vikingArmy:
                break
            else:
                input(f"\nPress ENTER to continue {self.war.name}")
        input("\nPress ENTER to exit the Game")