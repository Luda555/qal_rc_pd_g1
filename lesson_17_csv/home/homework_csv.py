import csv
from pathlib import Path


def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def write_csv(filepath: Path, content:list):
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=content[0].keys())
        writer.writeheader()
        writer.writerows(content)

def find_duplicates(data_1: list, data_2: list):
     items_set1 = {tuple(row.items()) for row in data_1}
     items_set2 = {tuple(row.items()) for row in data_2}
     l1 = len(data_1)
     l2 = len(data_2)
     items_set1_len = len(items_set1)
     items_set2_len = len(items_set2)
     sum_set = items_set1 | items_set2 
     internal_dup1 = len(data_1) - len(items_set1) # кількість дублікатів в першому файлі
     internal_dup2 = len(data_2) - len(items_set2) #кількість дублікатів в другому файлі
     total_duplicates = len(items_set1 & items_set2) + internal_dup1 + internal_dup2 # загальна кількість дублікатів
     clean_rows = [dict(row) for row in sum_set]
     return total_duplicates, clean_rows

def main(data_1, data_2, filepath: Path):
    total_duplicates, clean_users = find_duplicates(data_1, data_2)
    print(f"Знайдено дублікатів: {total_duplicates}")
    print(f"Унікальних записів збережено: {len(clean_users)}")
    
    # 3. Записує результат у файл через вашу write_csv
    write_csv(filepath, clean_users)
    return None


if __name__ == "__main__":
    my_csv = Path(__file__).parent / "users_1.csv"
    content = read_file(my_csv)
    print(content, type(content))
    my_csv_2 = Path(__file__).parent / "users_2.csv"
    content2 = read_file(my_csv_2)
    print(content2, type(content2))
    clean_users_csv = Path(__file__).parent / "users_3.csv"
    main(content, content2, clean_users_csv)
    print(clean_users_csv)