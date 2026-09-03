class ChainOfOrders:
    def __init__(self, names):
        self.names = list(names)
        self.index = 0
    def __iter__(self):
        return self

    def __next__(self):
        if not self.names or self.index >= len(self.names):
            raise StopIteration 
        elif len(self.names) == 1:
            self.index += 1
            return f"{self.names} каже: теля прив'язав!" 
        elif self.index == 0:
            self.index += 1
            return f"Старший каже Михайлику: передай далі!"
        elif self.index == len(self.names) - 1:
            self.index += 1
            return f"Василько каже: теля прив'язав!"
        else:
            self.index += 1
            return f"Михайлик каже Василькові: передай далі!"            
    


def village_rumor(start_message, people):
    peoples = list(people)
    for index, name in enumerate(peoples):
        if index == 0:
            yield start_message

        elif index == len(peoples) - 1:
            start_message += f" (і всі дізналися!)"
            yield start_message
        else:
            start_message += f" (переказав {name})"
            yield start_message

events = [
    "Михайлик передав доручення",
    "Василько відмовився",
    "Грицько передав доручення",
    "Оленка прив'язала теля",
    "Данилко передав доручення",
]
count = sum(1 for event in events if "передав доручення" in event and event.split()[0])
print(f"Доручення передавали {count} рази")



import itertools


def toloka_queue(people):
    while True:
        for name in people:
            yield f"Черга: {name}"

peoples = ["Іван", "Марія", "Степан"]
queue = toloka_queue(peoples)

for turn in itertools.islice(queue, 7):
    print(turn)


def find_calf(log):
    
    for sentence in log:
        if "прив'яз" in sentence:
            yield sentence
journal = [
    "Михайлик отримав доручення",
    "Михайлик передав Василькові",
    "Василько загрався",
    "Василько передав Оленці",
    "Оленка прив'язала теля біля хліва",
    "Оленка пішла додому",
    "Дід заспокоївся",
]
result = next(find_calf(journal))
print(result)

