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






print(reformat([{"type": "Drink", "name": "Tea", "price": 2.5}, {"type": "Drink", "name": "Chocolate Milk", "price": 3.0}, {"type": "Food", "name": "Hotdog", "price": 0.5}, {"type": "Food", "name": "Burger", "price": 4.0},]))