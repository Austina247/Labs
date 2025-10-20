def reformat(data):
    dic1 = {}
    for dict in data:
        dic1[dict["type"]] = {}
    for dict in data:
        dic1[dict["type"]][dict["name"]] = dict["price"]
    return dic1

def nth(data, n):
    if data is None:
        return None
    if n == 0:
        return data[0]
    return nth(data[1], n-1)

def where(data):
    if type(data) == str:
        return 1 if data == "Waldo" else 0
    elif type(data) == list:
        total = 0
        for name in data:
            total += where(name)
        return total
    elif type(data) == dict:
        total = 0
        for key in data:
            total += where(data[key])
            total += where(key)
        return total
    else:
        return 0