input_data = []
input_data.append({"action": "Action-1", "cost": 20, "profit": 5})
input_data.append({"action": "Action-2", "cost": 30, "profit": 10})
input_data.append({"action": "Action-3", "cost": 50, "profit": 15})
input_data.append({"action": "Action-4", "cost": 70, "profit": 20})
input_data.append({"action": "Action-5", "cost": 60, "profit": 17})
input_data.append({"action": "Action-6", "cost": 80, "profit": 25})
input_data.append({"action": "Action-7", "cost": 22, "profit": 7})
input_data.append({"action": "Action-8", "cost": 26, "profit": 11})
input_data.append({"action": "Action-9", "cost": 48, "profit": 13})
input_data.append({"action": "Action-10", "cost": 34, "profit": 27})
input_data.append({"action": "Action-11", "cost": 42, "profit": 17})
input_data.append({"action": "Action-12", "cost": 110, "profit": 9})
input_data.append({"action": "Action-13", "cost": 38, "profit": 23})
input_data.append({"action": "Action-14", "cost": 14, "profit": 1})
input_data.append({"action": "Action-15", "cost": 18, "profit": 3})
input_data.append({"action": "Action-16", "cost": 8, "profit": 8})
input_data.append({"action": "Action-17", "cost": 4, "profit": 12})
input_data.append({"action": "Action-18", "cost": 10, "profit": 14})
input_data.append({"action": "Action-19", "cost": 24, "profit": 21})
input_data.append({"action": "Action-20", "cost": 114, "profit": 18})

for data in input_data:
    data["profit"] = data["profit"] / 100 * data["cost"]


def recursive_KS(input_data, n, capacity):
    """In this function, we brute force the computation of the KS problem. Each item
    is either put in the bag or not"""
    # If the bag is full or the last item is reached, return 0
    if n == -1 or capacity == 0:
        result = 0
    # If the item is bigger than the remaining capacity
    elif input_data[n]["cost"] > capacity:
        result = recursive_KS(
            input_data,
            n - 1,
            capacity,
        )
    # We try putting the item in the bag, and not putting it in the bag
    else:
        tmp1 = recursive_KS(
            input_data,
            n - 1,
            capacity,
        )
        tmp2 = input_data[n]["profit"] + recursive_KS(
            input_data,
            n - 1,
            capacity - input_data[n]["cost"],
        )
        result = max(tmp1, tmp2)
    return result


print(recursive_KS(input_data, len(input_data) - 1, 500))


def iterative_KS(input_data):

    max_possibilities = 2**20

    total_cost = 0
    max_output = 0
    item_to_buy = 0
    for i in range(max_possibilities):
        binary = bin(i)[2:]
        position = [pos for pos, char in enumerate(binary) if char == "0"]
        cost = 0
        profit = 0
        for pos in position:
            cost += input_data[pos]["cost"]
            if cost > 500:
                break
            profit += input_data[pos]["profit"]
        if profit > max_output and cost < 500:
            max_output = profit
            total_cost = cost
            item_to_buy = position

    print(max_output)
    print(total_cost)
    print(item_to_buy)
    """
        for item in item_to_buy:
        print(input_data[item]["action"])
        print(input_data[item]["cost"])
        print(input_data[item]["profit"])
    """


iterative_KS(input_data)
