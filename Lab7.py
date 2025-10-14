def reformat(data):
    drinks = {}
    foods = {}
    for dict in data:
        if dict["type"] =="Drink":
            drinks[dict["name"]] = dict["price"]
    for dict in data:
        if dict["type"] == "Food":
            foods[dict["name"]] = dict["price"]
    updatedData = {}
    updatedData["Drink"] = drinks
    updatedData["Food"] = foods
    return updatedData
