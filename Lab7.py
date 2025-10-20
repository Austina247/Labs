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

