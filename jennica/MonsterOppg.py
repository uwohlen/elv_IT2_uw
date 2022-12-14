import sys 
import os
import random
import pickle

#definerer vaapen som en konstant
vaapen = {"krystallsverd":40}

class Spiller: #klasse for spiller, med ulike konstruktører
    def __init__(self, navn):
        self.navn = navn
        self.maxHP = 100
        self.HP = self.maxHP1
        self.base_attack = 10
        self.gull = 40
        self.pots = 0
        self.vaap = ["bronsesverd"]
        self.curvaap = ["bronsesverd"]

    @property #bruker en property decorator som
    def attack(self):
        attack = self.base_attack
        if self.curvaap == "bronsesverd":
            attack += 5

        if self.curvaap == "krystallsverd":
            attack += 15

        return attack


class Monster: #klasse for monster, med ulike konstruktører
    def __init__(self, navn):
        self.navn = navn
        self.maxHP = 50
        self.HP = self.maxHP
        self.attack = 5
        self.goldgain = 10
MonsterIG = Monster("Monster")

class Zombie: #klasse for zombie, med ulike konstruktører (kan evt gjøres om til sub-klasse under monsterklassen
    def __init__(self, navn):
        self.navn = navn
        self.maxHP = 70
        self.HP = self.maxHP
        self.attack = 7
        self.goldgain = 15
ZombieIG = Zombie("Zombie")

# 
def main():
    os.system('clear')
    print("Velkommen til jennis eventyrspill!\n")
    print("I dette spillet kommer du i møte med farer og trusler som du strategisk må håndtere")
    print("Lykke til å eventyret!!")
    print("1.) Start")
    print("2.) Lagre")
    print("3.) Avslutt")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('clear')
            with open('savefile', 'rb') as f:
                global SpillerIG
                SpillerIG = pickle.load(f)
            print("Lagrer...")
            option = input(' ')
            start1()
        else:
            print("Du har ikke noe å lagre i dette spillet ennå.")
            option = input(' ')
            main()

    elif option == "3":
        sys.exit()
    else:
        main()

def start():
    os.system('clear')
    print("Heihei, hva heter du?")
    option = input("--> ")
    global SpillerIG #en global variabel inni en funksjon
    SpillerIG = Spiller(option)
    start1()

def start1():
    os.system('clear')
    print("Navn: %s" % SpillerIG.navn)
    print("Attack: %i" % SpillerIG.attack)
    print("Gull: %d" % SpillerIG.gull)
    print("Dine vaapen: %s" % SpillerIG.curvaap)
    print("Potions: %d" % SpillerIG.pots)
    print("HP: %i/%i\n" % (SpillerIG.HP, SpillerIG.maxHP))
    print("1.) Attack")
    print("2.) Butikk")
    print("3.) Lagre")
    print("4.) Avslutt")
    print("5.) Inventory")
    option = input("--> ")
    if option == "1":
        prefight()
    elif option == "2":
        butikk()
    elif option == "3":
        os.system('clear')
        with open('savefile', 'wb') as f:
            pickle.dump(SpillerIG, f)
            print ("\nSpillet!\n")
        option = input(' ')
        start1()
    elif option == "4":
        sys.exit()
    elif option == "5":
        inventory()
    else:
        start1()

def inventory(): #metode for å sjekke hva du har i inventory, blir enten
    os.system('clear')
    print("Hva vil du gjøre?")
    print("1.) Equip Weapon")
    print("b.) gå tilbake")
    option = input(">>> ")
    if option == "1":
        utruste()
    elif option == 'b':
        start1()

def utruste(): #metode for å utruste seg
    os.system('clear')
    print("Hva vil du utruste?")
    for vaapen in SpillerIG.vaap:
        print(vaapen)
    print("b får å gå tilbake")
    option = input(">>> ")
    if option == SpillerIG.curvaap:
        print("Du har allerede utrustet dette våpenet")
        option = input(" ")
        utruste()
    elif option == "b":
        inventory()
    elif option in SpillerIG.vaap:
        SpillerIG.curvaap = option
        print("Du har nå utrustet deg med %s." % option)
        option = input(" ")
        utruste()
    else:
        print("Du har ikke %s i ditt inventory" % option)




def prefight():
    global monster
    monsternum = random.randint(1, 2)
    if monsternum == 1:
        monster = MonsterIG
    else:
        monster = ZombieIG
    fight()

def fight():
    os.system('clear')
    print("%s     vs      %s" % (SpillerIG.navn, monster.navn))
    print("%s's HP: %d/%d    %s's HP: %i/%i" % (SpillerIG.navn, SpillerIG.HP, SpillerIG.maxHP, monster.navn, monster.HP, monster.maxHP))
    print("Potions %i\n" % SpillerIG.pots)
    print("1.) Attack")
    print("2.) Drikk potion")
    print("3.) Løp")
    option = input(' ')
    if option == "1":
        attack()
    elif option == "2":
        drinkpot()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    os.system('clear')
    SAttack = random.randint(SpillerIG.attack / 2, SpillerIG.attack)
    MAttack = random.randint(monster.attack / 2, monster.attack)
    if SAttack == SpillerIG.attack / 2:
        print("Du bommet!")
    else:
        monster.HP -= SAttack
        print("Du utgjorde %i damage!" % SAttack)
    option = input(' ')
    if monster.HP <=0:
        win()
    os.system('clear')
    if MAttack == monster.attack/2:
        print("Fienden bommet!")
    else:
        SpillerIG.HP -= MAttack
        print("Fienden utgjør %i damage!" % MAttack)
    option = input(' ')
    if SpillerIG.HP <= 0:
        dead()
    else:
        fight()

def drinkpot():
    os.system('clear')
    if SpillerIG.pots == 0:
        print("Du har ikke noen potions!")
    else:
        SpillerIG.HP += 50
        if SpillerIG.HP > SpillerIG.maxHP:
            SpillerIG.HP = SpillerIG.maxHP
        print("Du drakk en potion!")
    option = input(' ')
    fight()

def run():
    os.system('clear')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("Du klarte å komme unna!")
        option = input(' ')
        start1()
    else:
        print("Du klarte ikke å komme deg unna!")
        option = input(' ')
        os.system('clear')
        MAttack = random.randint(monster.attack / 2, monster.attack)
        if MAttack == monster.attack/2:
            print("Fienden bommet!")
        else:
            SpillerIG.HP -= MAttack
            print("Fienden utgjør %i damage!" % MAttack)
        option = input(' ')
        if SpillerIG.HP <= 0:
            dead()
        else:
            fight()

def win():
    os.system('clear')
    monster.HP = monster.maxHP
    SpillerIG.gull += monster.goldgain
    print("Du har overvunnet %s" % monster.navn)
    print("Du fant %i gull!" % monster.goldgain)
    option = input(' ')
    start1()

def dead():
    os.system('clear')
    print("Du døde")
    option = input(' ')

def butikk():
    os.system('clear')
    print("Velkommen til butikken!")
    print("\nHva vil du kjøpe?\n")
    print("1.) krystallsverd")
    print("2.) tilbake")
    print(" ")
    option = input(' ')

    if option in vaapen:
        if SpillerIG.gull >= vaapen[option]:
            os.system('clear')
            SpillerIG.gull -= vaapen[option]
            SpillerIG.vaap.append(option)
            print("Du har kjøpt %s" % option)
            option = input(' ')
            butikk()

        else:
            os.system('clear')
            print("Du har ikke nok gull.")
            option = input(' ')
            butikk()

    elif option == "tilbake":
        start1()

    else:
        os.system('clear')
        print("Denne gjenstanden finnes ikke.")
        option = input(' ')
        butikk()

main()


# for å videreutvikle spillet:
# hvordan vinner man, premie?
# er en bug i butikken, der man ikke kan bruke tallene, men må skrive "tilbake" eller "krystallsverd"
# samme bug i inventory, bare at man avslutter spillet om man skriver et tall