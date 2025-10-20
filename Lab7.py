def reformat(data):
    dic1 = {}
    for dict in data:
        dic1[dict["type"]] = {}
    for dict in data:
        dic1[dict["type"]][dict["name"]] = dict["price"]
    return dic1


