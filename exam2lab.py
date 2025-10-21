def print_backwards(string):
    if len(string) == 1:
        print(string)
        return
    else:
        print(string[-1], end="")
        print_backwards(string[:-1])

def format_names(data):
    if data[0].find(",") == -1:
        data[0] = data[0][data[0].find(" ") + 1:] +", " + data[0][:data[0].find(" ")]

    if len(data) == 1:
        return data
    new_data = [data[0]] + format_names(data[1:])
    return new_data

def sum_a(data):
    sum = 0
    for dic in data:
        for key, value in dic.items():
            if key == "a":
                sum += value
    return sum

def process_list(data):
    new_list = []
    for i in data:
        if i % 2 == 0:
            new_list.append(str(i))
            data.pop(data.index(i))
    for i in data:
        new_list.append(i*10)
    return new_list



