class Object:
    def __init__(self, id):
        self.id = id
        self.tags = {}

def search_by_tags(key, values, objects):
    results = []
    for obj in objects:
        if obj.tags.get(key) in values:
            results.append(obj)
    return results

def check_subset(subset, objects):
    keys = set()
    values_map = {}
    for obj in subset:
        for key, value in obj.tags.items():
            keys.add(key)
            values_map.setdefault(key, set()).add(value)
    for key in keys:
        values = values_map[key]
        result = search_by_tags(key, values, objects)
        if set(result) != set(subset):
            return "no"
    return "yes"





