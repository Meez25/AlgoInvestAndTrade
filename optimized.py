input_data = [
    {"action": "Action-1", "cost": 20, "profit": 5},
    {"action": "Action-2", "cost": 30, "profit": 10},
    {"action": "Action-3", "cost": 50, "profit": 15},
    {"action": "Action-4", "cost": 70, "profit": 20},
    {"action": "Action-5", "cost": 60, "profit": 17},
    {"action": "Action-6", "cost": 80, "profit": 25},
    {"action": "Action-7", "cost": 22, "profit": 7},
    {"action": "Action-8", "cost": 26, "profit": 11},
    {"action": "Action-9", "cost": 48, "profit": 13},
    {"action": "Action-10", "cost": 34, "profit": 27},
    {"action": "Action-11", "cost": 42, "profit": 17},
    {"action": "Action-12", "cost": 110, "profit": 9},
    {"action": "Action-13", "cost": 38, "profit": 23},
    {"action": "Action-14", "cost": 14, "profit": 1},
    {"action": "Action-15", "cost": 18, "profit": 3},
    {"action": "Action-16", "cost": 8, "profit": 8},
    {"action": "Action-17", "cost": 4, "profit": 12},
    {"action": "Action-18", "cost": 10, "profit": 14},
    {"action": "Action-19", "cost": 24, "profit": 21},
    {"action": "Action-20", "cost": 114, "profit": 18},
]

"""convert the profit to a decimal value, representing money."""
for data in input_data:
    data["profit"] = data["profit"] / 100 * data["cost"]


def dynamic_programming_KS(vals, wts, capacity):

    # Make the table (list comprehension)

    w, h = capacity + 1, len(vals)

    table = [[0 for _ in range(w)] for _ in range(h)]

    # First iterate over the items (rows)
    # second iterate over the columns which represent weights

    for index in range(len(vals)):
        for weight in range(w):
            # If the item weights more than the capacity at that column?
            # Take above value, that problem was solved
            if wts[index] > weight:
                table[index][weight] = table[index - 1][weight]
                continue

            # if the value of the item < capacity
            prior_value = table[index - 1][weight]
            #         val of current item  + val of remaining weight
            new_option_best = vals[index] + table[index - 1][weight - wts[index]]
            table[index][weight] = max(prior_value, new_option_best)

    return table


def items_in_optimal(h, w, wts, table, input_data):
    i = h - 1
    j = w

    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            print(input_data[i]["action"])
            j = j - wts[i]
            i = i - 1
        else:
            i = i - 1


vals = [data["profit"] for data in input_data]
wts = [data["cost"] for data in input_data]


def main():
    CAPACITY = 500
    table = dynamic_programming_KS(vals, wts, CAPACITY)
    items_in_optimal(len(wts), CAPACITY, wts, table, input_data)


if __name__ == "__main__":
    main()
