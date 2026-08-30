from abc import ABC, abstractmethod

class MagicCreature(ABC):
    def __init__(self, name, magic_level, health):
        self.name = name
        self.magic_level = magic_level
        self.health = health
        
    @property
    def magic_level(self):
        return self._magic_level

    @magic_level.setter
    def magic_level(self, value: int):
        if value < 1 or value > 10:
            raise ValueError ("Рівень магії має бути від 1 до 10!")
        else:
            self._magic_level = value
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, value: int):
        if value <0 or value > 100:
            raise ValueError("Здоров'я має бути від 0 до 100!")
        if value <= 0:
            self.__health = 0
            self.alive = False
        else:
            self.__health = value
            self.alive = True

    @property
    def is_alive(self):
        return self.alive        

    @abstractmethod
    def use_ability(self):
        """Кожна підістота зобов'язаний реалізувати цей метод"""
        pass  
    @abstractmethod
    def describe(self):
        """повертає опис істоти у довільному форматі — кожен підклас описує себе по-своєму"""
        pass   

    def take_damage(self, amount: int):
        if self.alive == False:
            return f"{self.name} вже переміг смерть... або ні."
        self.health = self.health - amount

    def __str__(self):
        return f"{self.name} | Магія: {self._magic_level} | HP: {self.__health} | Живий: {self.alive}"   


class Molfar(MagicCreature):
    def __init__(self, name, magic_level, health, element: str, spells: int):
        super().__init__(name, magic_level, health)
        self.element = element
        self.spells = spells
       
    @property
    def spells(self):
        return self.__spells

    @spells.setter
    def spells(self, value: int):
        if value < 0:
            raise ValueError("лише невід'ємні числа")
        else:
            self.__spells = value
            
    def use_ability(self):
        if self.spells > 0:
            self.spells -= 1 
            return f"Мольфар {self.name} закликає {self.element}! Залишилось заклинань: {self.spells}"
        if self.spells < 1:
            return f"Мольфар {self.name} виснажений — сила стихій покинула його!"
    
    def describe(self):
        return f"Мольфар {self.name}, повелитель стихії {self.element}. Рівень магії: {self.magic_level}"

class Rusalka(MagicCreature):
    def __init__(self,name, magic_level, health, river, charm_power):
        super().__init__(name, magic_level, health)
        self.river = river
        self.charm_power = charm_power

    @property
    def charm_power(self):
        return self.__charm_power
    @charm_power.setter
    def charm_power(self, value: int):
        if value < 1 or value > 5:
            raise ValueError("Сила причарування має бути від 1 до 5!")
        else:
            self.__charm_power = value

    def use_ability(self):
        if self.charm_power == 5:
            return f"Русалка {self.name} з річки {self.river} зачаровує мандрівника! Сила чар: {self.charm_power}. Ніхто не встоїть!"
        else:
            return f"Русалка {self.name} з річки {self.river} зачаровує мандрівника! Сила чар: {self.charm_power}."        

    def describe(self):
        return f"Русалка {self.name}, мешканка річки {self.river}. Сила чар: {self.charm_power}/5"

class Perelesnyk(MagicCreature):
    def __init__(self,name, magic_level, health, speed):
        super().__init__(name, magic_level, health)
        self.speed = speed
        self.form = "людська" 

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value: int):
        if value < 1 or value > 100:
            raise ValueError("Швидкість має бути від 1 до 100!")
        else:
            self.__speed = value

    def change_form(self): 
        if self.form == "людська":
            self.form = "вогняна куля"
        else:
            self.form = "людська"
        return f"Перелесник перетворився на {self.form}!"   
                

    def use_ability(self):
        if self.form == "людська":
            return f"Перелесник {self.name} мчить крізь ніч зі швидкістю {self.__speed}! Форма: {self.form}. Ніхто не здогадається..."
        else:
            return f"Перелесник {self.name} мчить крізь ніч зі швидкістю {self.__speed}! Форма: {self.form}."        

    def describe(self):
        return f"Перелесник {self.name}. Швидкість: {self.__speed}. Зараз у формі: {self.form}"

class EnchantedForest:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.__creatures = []

    @property
    def creatures_count(self):
        # Рахуємо лише тих істот зі списку, у яких is_alive == True
        live_count = 0
        for creature in self.__creatures:
            if creature.is_alive:  
                live_count += 1
        return live_count

    def add_creature(self, creature):
        if creature in self.__creatures:
            return f"{creature.name} вже мешкає у цьому лісі!"
        elif len(self.__creatures) >= self.capacity:
            return f"Зачарований ліс {self.name} переповнений!"
        elif not creature.is_alive:
            return f"Мертві істоти не можуть оселитись у лісі!"
        else:
            self.__creatures.append(creature)
        return f"{creature.name} успішно додано до лісу {self.name}."
        
    def remove_creature(self, name: str):
        for creature in self.__creatures:
            if creature.name == name:
                self.__creatures.remove(creature)
                return f"Істоту {name} успішно видалено з лісу {self.name}!"
        return f"Істоту {name} не знайдено у лісі!"

    def most_powerful(self):
        if len(self.__creatures) < 1:
            return f"Ліс порожній — нема кому чаклувати!"
        strongest = max(self.__creatures, key=lambda creature: creature.magic_level)
        return strongest
    
    def attack_intruder(self, intruder_name):
        if len(self.__creatures) < 1:
            return f"Ліс беззахисний перед {intruder_name}!"
        results1 = []
        for creature in self.__creatures:  
            if creature.is_alive:  # Тільки живі істоти атакують
                results1.append(creature.use_ability())
        return results1
            

    def census(self):
        if len(self.__creatures) < 1:
            return f"Ліс порожній"  
        results2 = []
        for creature in self.__creatures:  
            results2.append(creature.describe())
        return results2                   
       
            