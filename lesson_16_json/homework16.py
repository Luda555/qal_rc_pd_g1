import json

folklore_item = {
    "title": "Про правду і кривду",
    "genre": "казка",
    "region": "Поділля",
    "narrator": "Марія Ковальчук",
    "year": 1985,
    "content": "Жили собі двоє братів...",
    "tags": ["добро", "зло", "мораль"],
    "verified": True
}

json_string = json.dumps(folklore_item, ensure_ascii=False, indent = 4)
print(json_string)
print(type(json_string))

from pathlib import Path
script_dir = Path(__file__).parent
file_path = script_dir / "folklore_records.json"
folklore_records = [
    {
        "title": "Ой вилітай, гусю, на тую русію",
        "genre": "пісня",
        "region": "Західне Полісся (село Сварицевичі, Рівненщина)",
        "narrator": "Доминіка Чекун",
        "year": 2008,
        "content": "Архаїчна веснянка-визивалка, де дівчата закликають гуску прилетіти й принести весну, а також пророкують дівчатам майбутнє заміжжя.",
        "tags": ["веснянка", "обрядова", "автентика", "полісся"],
        "verified": True
    },
    {
        "title": "Про козака та змія",
        "genre": "казка",
        "region": "Поділля (Вінниччина)",
        "narrator": "Андрій Скрипник (Казкар)",
        "year": 1954,
        "content": "Казка про бідного козака, який завдяки своїй кмітливості та силі переміг триголового змія, що викрав воду з криниці, та визволив село.",
        "tags": ["козаки", "героїчний епос", "поділля", "чарівна казка"],
        "verified": True
    },
    {
        "title": "Звідки взялися Карпати",
        "genre": "легенда",
        "region": "Гуцульщина (Верховина, Івано-Франківщина)",
        "narrator": "Михайло Зеленчук",
        "year": 1978,
        "content": "Легенда про велетня Карпа, який боровся зі злим володарем Силуяном. Коли Силуян ударив Карпа об землю, земля розкололася, і з уламків виросли гори, які назвали Карпатами.",
        "tags": ["топоніміка", "гори", "велетні", "карпати"],
        "verified": True
    },
    {
        "title": "Козацькому роду нема переводу",
        "genre": "прислів'я",
        "region": "Подніпров'я (Дніпропетровщина)",
        "narrator": "Марія Панасенко",
        "year": 1991,
        "content": "Народний афоризм, який підкреслює безсмертя козацьких традицій, незламність українського народу та спадкоємність поколінь.",
        "tags": ["приказка", "козацтво", "мудрість", "подніпров'я"],
        "verified": True
    },
    {
        "title": "Ой зацвіла калинонька в лузі",
        "genre": "пісня",
        "region": "Слобожанщина (Харківщина)",
        "narrator": "Ганна Сидоренко",
        "year": 2012,
        "content": "Родинно-побутова лірична пісня про тугу дівчини за козаком, який поїхав на війну. Особливістю є виконання з високим протяжним виводом.",
        "tags": ["лірика", "родинно-побутова", "слобожанщина", "калина"],
        "verified": False
    }
]

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(folklore_records, file, indent=4, ensure_ascii=False)

with open(file_path, "r", encoding="utf-8") as file:
    loared_records = json.load(file)

start_len = len(folklore_records)
end_len = len(loared_records)
if start_len == end_len:
    print("Кількість записів збережена")
else:
    print("Помилка збереження")    

for index, record in enumerate(loared_records, start=1):
    print(f"{index}. \"{record['title']}\" ({record['genre']}, {record['region']})")

class FolkloreRecord:
    def __init__(self, title, genre, region, narrator, year, content, tags, verified):
        self.title = title
        self.genre = genre
        self.region = region
        self.narrator = narrator
        self.year = year
        self.content = content
        self.tags = tags
        self.verified = verified

    def to_dict(self):
        return {
            "title" : self.title,
            "genre" : self.genre,
            "region" : self.region,
            "narrator" : self.narrator,
            "year" : self.year,
            "content" : self.content,
            "tags" : self.tags,
            "verified" : self.verified}  

    @classmethod
    def from_dict(cls, data):
        return cls(
            title = data["title"],
            genre = data["genre"],
            region = data["region"],
            narrator = data["narrator"],
            year = data["year"],
            content = data["content"],
            tags = data["tags"],
            verified = data["verified"]  
        ) 
    def __str__(self):
        return f"[{self.genre}] \"{self.title}\" - {self.region}, {self.year} (оповідач: {self.narrator})"     

legenda = FolkloreRecord(
        title= "Про заснування міста Вінниця",
        genre= "легенда",
        region= "Поділля (Вінниччина)",
        narrator= "Петро Войтенко",
        year= 1965,
        content= "Легенда розповідає про племінників князя Ольгерда — братів Коріатовичів, які збудували фортецю на річці Бог (Південний Буг). Назву місто отримало від старослов'янського слова 'вѣно' — дар, або від річки Вінничка.",
        tags= ["поділля", "історія", "топоніміка", "фортеця"],
        verified= True
)
saying = FolkloreRecord(
        title= "Хліб — усьому голова",
        genre= "прислів'я",
        region= "Таврія (Херсонщина)",
        narrator= "Олена Кравченко",
        year= 1982,
        content= "Головна народна мудрість про повагу до праці хлібороба, цінність хліба та його сакральне значення в житті та побуті українського народу.",
        tags= ["приказка", "мудрість", "таврія", "хліб"],
        verified= True
)
song = FolkloreRecord(
        title= "Ой глибокий колодязю, золотії ключі",
        genre= "пісня",
        region= "Волинь",
        narrator= "Ніна Матвієнко",
        year= 1975,
        content= "Давня волинська лірична пісня, в якій колодязь є символом глибоких почуттів та дівочої долі, а втрачені ключі — символом нерозділеного або втраченого кохання.",
        tags= ["лірика", "волинь", "родинно-побутова", "символізм"],
        verified= True
)
total_list = [song, saying, legenda]
list_dict = [i.to_dict() for i in total_list]

with open("records.json", "w", encoding="utf-8") as file:
    json.dump(list_dict, file, indent=4, ensure_ascii=False)

with open("records.json", "r", encoding="utf-8") as file:
    loared_list_dict = json.load(file)

restored_objects = [FolkloreRecord.from_dict(item) for item in loared_list_dict]

for obj in restored_objects:
    print(obj)  

class FieldExpedition:
    def __init__(self, expedition_id, researcher, location, data):
        self.expedition_id = expedition_id 
        self.researcher = researcher
        self.location = location
        self.data = data      
        self.records = []

    def add_record(self, record):
        for item in self.records: 
            if item.title == record.title:  
                return f"Запис '{record.title}' вже є в експедиції"
        self.records.append(record)
        return self.records

    def remove_record(self, title):
        for item in self.records: 
            if item.title == title: 
                 self.records.remove(item) 
                 return self.records
        return f"Запис '{title}' не знайдено"
                
    def find_by_genre(self, genre):
        results = [] 
        for item in self.records: 
            if item.genre == genre: 
                results.append(item)
        return results
    
    def to_dict(self):
        return {
            "expedition_id": self.expedition_id,
            "researcher": self.researcher,
            "location": self.location,
            "data": self.data,
            "records": [item.to_dict() for item in self.records]
        }

    @classmethod
    def from_dict(cls, data):
        expedition = cls(
            expedition_id = data["expedition_id"],  # Додано правильний відступ (4 пробіли від cls)
            researcher = data["researcher"],
            location = data["location"],
            data = data["data"]
        )
        expedition.records = [FolkloreRecord.from_dict(item) for item in data.get("records", [])]
        return expedition

    def save(self, filepath):
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, indent=4, ensure_ascii=False)
        print(f"📁 Експедицію успішно збережено у файл: {filepath}")

    @classmethod
    def load(cls, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
            print(f"📖 Дані успішно прочитано з файлу: {filepath}")
            return cls.from_dict(data)
            
        except FileNotFoundError:
            print(f"❌ Помилка: Файл за шляхом '{filepath}' не знайдено.")
            return None
            
        except json.JSONDecodeError:
            print(f"❌ Помилка: Файл '{filepath}' пошкоджений або має некоректний формат JSON.")
            return None

# === ПЕРЕВІРКА ПОВНОГО ЦИКЛУ ЕКСПЕДИЦІЇ ===

# 1. Створюємо 4 записи різних жанрів
song1 = FolkloreRecord(
    title="Ой глибокий колодязю, золотії ключі",
    genre="пісня",
    region="Волинь",
    narrator="Ніна Матвієнко",
    year=1975,
    content="Давня волинська лірична пісня...",
    tags=["лірика", "волинь"],
    verified=True
)

saying1 = FolkloreRecord(
    title="Хліб — усьому голова",
    genre="прислів'я",
    region="Таврія",
    narrator="Олена Кравченко",
    year=1982,
    content="Народна мудрість про повагу до праці хлібороба...",
    tags=["приказка", "мудрість"],
    verified=True
)

legenda1 = FolkloreRecord(
    title="Про заснування міста Вінниця",
    genre="легенда",
    region="Поділля",
    narrator="Петро Войтенко",
    year=1965,
    content="Легенда розповідає про братів Коріатовичів...",
    tags=["історія", "топоніміка"],
    verified=True
)

kazka1 = FolkloreRecord(
    title="Про правду і кривду",
    genre="казка",
    region="Поділля",
    narrator="Марія Ковальчук",
    year=1985,
    content="Жили собі двоє братів...",
    tags=["добро", "зло", "мораль"],
    verified=True
)

# Створюємо експедицію
expedition = FieldExpedition(
    expedition_id="EXP-2026", 
    researcher="Андрій Шевченко", 
    location="Україна", 
    data="2026-09-06"
)

expedition.add_record(song1)
expedition.add_record(saying1)
expedition.add_record(legenda1)
expedition.add_record(kazka1)
print(f"Додано записів до експедиції: {len(expedition.records)}")


# Зберігаємо у файл 
expedition.save("expedition_data.json")


# Завантажуємо з файлу в НОВИЙ об'єкт
new_expedition = FieldExpedition.load("expedition_data.json")


# Знаходимо всі пісні через find_by_genre()
songs_found = new_expedition.find_by_genre("пісня")
if songs_found:
    for song in songs_found:
        print(f"Знайдено: {song}")
else:
    print("Пісенного жанру не знайдено.")


# Видалимо казку "Про правду і кривду"
delete_result = new_expedition.remove_record("Про правду і кривду")
print(f"Результат видалення: Кількість записів тепер — {len(new_expedition.records)}")

# Зберігаємо оновлену експедицію
new_expedition.save("expedition_data.json")
print("Перевірку завершено")

def merge_archives(filepaths):
    combined_records = []  # Загальний список для всіх FolkloreRecord

    for path in filepaths:
        expedition = FieldExpedition.load(path)
        
        if expedition is not None:
            combined_records.extend(expedition.records)
            print(f"✅ Додано {len(expedition.records)} запис(ів) з файлу '{path}'")
        else:
            print(f"⚠️ Попередження: Файл '{path}' було пропущено через помилку завантаження.")
            
    return combined_records

def filter_records(records, genre=None, region=None, verified=None):

    filtered_results = []
    
    for item in records:
        if genre is not None and item.genre != genre:
            continue
        if region is not None and item.region != region:
            continue
        if verified is not None and item.verified != verified:
            continue
        filtered_results.append(item)
        
    return filtered_results

def export_summary(records, filepath):
   
    summary_data = []
    
    for item in records:
        short_info = {
            "title": item.title,
            "genre": item.genre,
            "region": item.region,
            "verified": item.verified
        }
        summary_data.append(short_info)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(summary_data, file, indent=4, ensure_ascii=False)
        
    print(f"📋 Коротке зведення успішно експоновано у файл: {filepath}")


# Створення файлів експедицій з різними записами 
rec1 = FolkloreRecord("Ой глибокий колодязю", "пісня", "Волинь", "Ніна Матвієнко", 1975, "Текст...", ["лірика"], verified=True)
rec2 = FolkloreRecord("Хліб — усьому голова", "прислів'я", "Таврія", "Олена Кравченко", 1982, "Текст...", ["мудрість"], verified=True)

exp1 = FieldExpedition("EXP-01", "Дослідник А", "Південь-Захід", "2026-05-10")
exp1.add_record(rec1)
exp1.add_record(rec2)
exp1.save("expedition_1.json")  


# Створюємо записи для другої експедиції 
rec3 = FolkloreRecord("Про заснування міста Вінниця", "легенда", "Поділля", "Петро Войтенко", 1965, "Текст...", ["історія"], verified=True)
rec4 = FolkloreRecord("Містичні історії Південного Бугу", "легенда", "Поділля", "Невідоме джерело", 2010, "Текст...", ["містика"], verified=False) # verified=False

exp2 = FieldExpedition("EXP-02", "Дослідник Б", "Центр", "2026-07-22")
exp2.add_record(rec3)
exp2.add_record(rec4)
exp2.save("expedition_2.json")

# Об'єднання архівів
archive_files = ["expedition_1.json", "expedition_2.json"]
all_collected_records = merge_archives(archive_files)
print(f"Усього з усіх архівів завантажено об'єктів: {len(all_collected_records)}")

# Шукаємо записи, які пройшли верифікацію (verified=True)
filtered_records = filter_records(all_collected_records, region="Поділля", verified=True)

print(f"Знайдено записів: {len(filtered_results if 'filtered_results' in locals() else filtered_records)}")
for item in filtered_records:
    print(f"  • {item}")

#Збереження зведення 
output_summary_path = "podillya_verified_summary.json"
export_summary(filtered_records, output_summary_path)


print("🎉 ПЕРЕВІРКУ УСПІШНО ЗАВЕРШЕНО!")

