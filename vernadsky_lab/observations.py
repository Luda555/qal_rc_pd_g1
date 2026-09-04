import datetime
from .minerals import get_mineral
_journal = []

def record(researcher, mineral_name, note):
    if get_mineral(mineral_name) is None:
        return (f"Мінерал {mineral_name} не зареєстровано. Спочатку додайте його до каталогу")
    log_entry = {
        "дослідник": researcher,
        "мінерал": mineral_name,
        "нотатка": note,
        "дата": datetime.date.today()
    }
    _journal.append(log_entry)  
    return (f"Спостереження записано: {researcher} → {mineral_name}") 

def get_observations(mineral_name=None):
    if mineral_name is None:
        return _journal
    filtered_journal = []
    for entry in _journal:
        if entry.get("мінерал") == mineral_name:
            filtered_journal.append(entry)
            
    return filtered_journal