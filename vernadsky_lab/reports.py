def summary():
    from .minerals import MINERAL_CATALOG
    from .observations import get_observations
    minerals_count = len(MINERAL_CATALOG)
    all_obs = get_observations()
    observations_count = len(all_obs)
    if observations_count == 0:
        active_researcher = "Спостережень ще немає"
    else:
        counts = {}
        for entry in all_obs:
            name = entry.get("дослідник")
            if name:
                counts[name] = counts.get(name, 0) + 1
        active_researcher = max(counts, key=counts.get)
    return (
        f"Кількість мінералів у каталозі: {minerals_count}\n"
        f"Кількість спостережень у журналі: {observations_count}\n"
        f"Найактивніший дослідник: {active_researcher}"
    )

def mineral_report(name):
    from .minerals import get_mineral
    from .observations import get_observations
    mineral_data = get_mineral(name)

    if mineral_data is None:
        return f"Мінерал {name} відсутній у каталозі"
    mineral_observations = get_observations(name)
    report = {
        "мінерал": name,
        "дані": mineral_data,
        "спостереження": mineral_observations
    }

    return report