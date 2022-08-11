
records = [
    (7, "Metamon"),
    (4, "Eevee"),
    (8, "Koiking"),
    (5, "Lucario"),
    (5, "Sirnight"),
    (3, "Pikachu")]


def pigeonhole_sort(lst):
    max_key = max(key for key, _ in lst)
    pigeonholes = [[] for _ in range(max_key + 1)]

    for rec in lst:
        pigeonholes[rec[0]] += rec

    print(f'pigeonholes: {pigeonholes}')

    return sum(pigeonholes, [])


sorted_records = pigeonhole_sort(records)
print(f'sorted: {sorted_records}')

