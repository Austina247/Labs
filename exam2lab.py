def print_backwards(string):
    if len(string) == 1:
        print(string,end="")
        return
    else:
        print(string[-1], end="")
        print_backwards(string[:-1])

def format_names(data):
    formated = data[0]
    if data[0].find(",") == -1:
        formated = data[0][data[0].find(" ") + 1:] +", " + data[0][:data[0].find(" ")]

    if len(data) == 1:
        return [formated]
    new_data = [formated] + format_names(data[1:])
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
    for i in range(0,len(data)):
        if i % 2 == 0:
            new_list.append(str(data[i]))
    for i in range(0,len(data)):
        if i % 2 == 1:
            new_list.append(data[i]*10)
    return new_list

