def is_strong(password):
    if len(password) < 8 or len(password) > 20:
        return False
    if " "  in password: 
        return False
    if not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
        return False
    return True
passwords = [
    "Cossack1",
    "sich",
    "ZAPORIZHZHIA2024",
    "Sich Gate 5",
    "Mazepa99",
    "короткий1",
    "BohunTheBrave",
    "D0br0nich!",
    "аааааааА1",
    "Valid1Pass",
]
strong_password = list(filter(lambda x: is_strong(x),passwords ))
not_strong_password = list(filter(lambda x: not is_strong(x), passwords))

for i in strong_password:
    print(f"'{i} - надійний'")

for i in not_strong_password:    
    print(F"'{i} - відхилено'")


from functools import reduce
raw_registry = [
    "  іван сірко  | полковник | 150",
    "БОГДАН ХМЕЛЬНИЦЬКИЙ | гетьман | 10000",
    "петро дорошенко|сотник|75",
    "  Іван Мазепа | гетьман | 30000 ",
    "семен палій  |  полковник  | 500",
    "  Григорій Сковорода | філософ | 0",
]
def dict_registry(line):
    new_str = [x.strip() for x in line.split("|")]
    return {
        "name" : new_str[0].capitalize(),
        "rank" : new_str[1].capitalize(),
        "warriors": int(new_str[2])
    }  

parsed_registry = list(map(dict_registry, raw_registry))
parsed_registry1 = list(filter(lambda x: x["warriors"] > 0, parsed_registry))
parsed_registry2 = list(sorted(parsed_registry1, key = lambda x: x["warriors"], reverse=True))
total_warriors = reduce(lambda acc, x: acc + x["warriors"], parsed_registry2, 0)

print(f"{'Ім`я':<25} | {'Посада':<12} | {'Воїни':<8}")
print("-" * 50)
for cossack in parsed_registry2:
    print(f"{cossack['name']:<25} | {cossack['rank']:<12} | {cossack['warriors']:<8}")

print("-" * 50)
print(f"Разом воїнів: {total_warriors}")

def is_palindrome(s):
    if s != s[::-1]:
        return False
    return True

messages = [
    "А роза упала на лапу азора",
    "Козак",
    "Зараз",
    "level",
    "Python",
    "А баба",
    "racecar",
    "Запоріжжя",
    "noon",
    "Мазепа",
]

palindrom_password = list(filter(lambda x: is_palindrome(x.lower().replace(" ", "")), messages))
print(list(map(lambda x: f"{x} → {x.lower().replace(' ', '')[::-1]}", palindrom_password)))


