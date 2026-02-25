from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def attack(self, lawan):
        pass

    @abstractmethod
    def diserang(self, damage):
        pass


class Hero(Interface):
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.__hp = hp

    def info(self):
        return f"{self.name} \n Power: {self.power} \n HP: {self.__hp}"  
    
    def attack(self, lawan):
        damage = self.power
        lawan.diserang(damage)
        return f"{self.name} menyerang {lawan.name} dengan kekuatan {damage}."
    
    def diserang(self, damage):
         self.__hp -= damage
         print(f"{self.name} terkena damage {damage}. Sisa HP: {self.__hp}")


    def get_hp(self):
        return self.__hp
    
    def set_hp(self, hp):
        if hp < 0:
            print("HP tidak bisa negatif.")
        elif hp > 1000:
            print("HP tidak bisa lebih dari 1000.")
        else:
            self.__hp = hp     


class monster(Interface):
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.__hp = hp         

    def info(self):
        return f"{self.name} \n Power: {self.power} \n HP: {self.get_hp()}"
    
    def attack(self, hero):
        damage = self.power
        hero.diserang(damage)
        return f"{self.name} menyerang balik {hero.name} dengan kekuatan {damage}."
    
    def diserang(self, damage):
         self.set_hp(self.get_hp() - damage)
         print(f"{self.name} terkena damage {damage}. Sisa HP: {self.get_hp()}")

    def get_hp(self):
        return self.__hp
    
    def set_hp(self, hp):
        if hp < 0:
            print("HP tidak bisa negatif.")
        elif hp > 1000:
            print("HP tidak bisa lebih dari 1000.")
        else:
            self.__hp = hp


class assasin(Hero):
    def __init__(self, name, power, hp, speed):
        super().__init__(name, power, hp)
        self.speed = speed

    def info(self):
        return f"{super().info()} \n Speed: {self.speed}"   
    
    def ultimate(self, lawan):
        damage = self.power * 2
        lawan.diserang(damage)
        return f"{self.name} menggunakan ultimate pada {lawan.name} dengan kekuatan {damage}."
    


class marksman(Hero):
    def __init__(self, name, power, hp, range):
        super().__init__(name, power, hp)
        self.range = range

    def info(self):
        return f"{super().info()} \n Range: {self.range}"   
    
    def arrowfire(self, lawan):
        damage = self.power * 1.5
        lawan.diserang(damage)
        return f"{self.name} menggunakan panah pada {lawan.name} dengan kekuatan {damage}."
    


class healer(Hero):
    def __init__(self, name, power, hp, heal_amount):
        super().__init__(name, power, hp)
        self.heal_amount = heal_amount

    def info(self):
        return f"{super().info()} \n Heal Amount: {self.heal_amount}"   
    
    def heal(self, target):
        hp = target.get_hp() 
        target.set_hp(hp + self.heal_amount)
        return f"{self.name} menyembuhkan {target.name} sebesar {self.heal_amount} HP."    

hero1 = Hero("Yu-zhong", 100, 1000)
hero2 = Hero("Ixia", 80, 800)
print(hero1._Hero__hp)
hero1.set_hp(-100)
print(hero1._Hero__hp)

abs = Interface()



# assasin1 = assasin("Hayabusa", 70, 600, 90)
# marksman1 = marksman("Granger", 90, 700, 150)
# monster1 = monster("Thamuz", 50, 500)
# healer1 = healer("Angela", 30, 400, 200)

# print("---Informasi Awal---")
# print(hero1.info())
# print(hero2.info())
# print(monster1.info())
# print(assasin1.info())
# print(marksman1.info())
# print(healer1.info())
# print("\n")


# print("---Pertarungan Dimulai---")
# print(hero1.attack(monster1))
# print(monster1.attack(hero1))
# print(hero1.info())
# print(hero2.info())
# print(monster1.info())
# print(assasin1.ultimate(monster1))
# print(monster1.info())
# print(marksman1.arrowfire(monster1))
# print(monster1.info())
# print(healer1.heal(monster1))
# print(monster1.info())