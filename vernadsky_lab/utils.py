


def hardest_minerals(n=3):
    from .minerals import MINERAL_CATALOG
    sorted_minerals = sorted(
        MINERAL_CATALOG.items(),
        key=lambda item: item[1]["hardness"],
        reverse=True
    )
    top_minerals_names = [item[0] for item in sorted_minerals[:n]]
    return top_minerals_names

def search_by_origin(origin_keyword):
    from .minerals import MINERAL_CATALOG
    found_minerals = []
    keyword_lower = origin_keyword.lower()
    for name, data in MINERAL_CATALOG.items():
        origin_lower = data.get("origin", "").lower()
        if keyword_lower in origin_lower:
            found_minerals.append(name)
    return found_minerals
