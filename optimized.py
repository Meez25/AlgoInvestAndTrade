from datetime import datetime


def create_table(width, height):

    table = [[0 for _ in range(width)] for _ in range(height)]
    return table


def fill_in_the_table(table, profit, width, cost):
    for index in range(len(profit)):
        for weight in range(width):
            # If the item weights more than the capacity at that column?
            # Take above value, that problem was solved
            if cost[index] > weight:
                table[index][weight] = table[index - 1][weight]
                continue

            # if the value of the item < capacity
            option1 = table[index - 1][weight]
            #         val of current item  + val of remaining weight
            option2 = profit[index] + table[index - 1][weight - cost[index]]
            table[index][weight] = max(option1, option2)

    return table


def get_best_combinaison(profit, cost, capacity):
    """From the data, create the table and fill it to get the optimal performance"""
    width, heigth = capacity + 1, len(profit)
    # Make the table (list comprehension)
    table = create_table(width, heigth)  # Create a table for the dynamic_programming
    table = fill_in_the_table(table, profit, width, cost)
    return table


def items_in_optimal(heigth, width, cost, table, input_data):
    """From the table, return the list of action to buy for the best profit"""
    i = heigth - 1
    j = width
    list_of_action_to_buy = []
    total_cost = 0

    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            list_of_action_to_buy.append(input_data[i]["action"])
            total_cost += input_data[i]["cost"]
            j = j - cost[i]
            i = i - 1
        else:
            i = i - 1
    return list_of_action_to_buy, total_cost


def display_result(max_profit, list_of_action_to_buy, total_cost):
    print(
        f"The best profit is {max_profit}$ for a cost of {total_cost}$ and you need to buy those actions :"
    )
    for action in list_of_action_to_buy:
        print(action)


def convert_pourcentage_to_profit(input_data):
    """convert the profit to a decimal value, representing money."""
    for action in input_data:
        action["profit"] = action["profit"] / 100 * action["cost"]
    return input_data


def main():

    CAPACITY = 500

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

    input_data = convert_pourcentage_to_profit(input_data)

    profit = [data["profit"] for data in input_data]
    cost = [data["cost"] for data in input_data]

    table = get_best_combinaison(profit, cost, CAPACITY)
    # The best combination is at the bottom right of the table
    best_profit = table[-1][-1]
    list_of_action_to_buy, total_cost = items_in_optimal(
        len(cost), CAPACITY, cost, table, input_data
    )
    display_result(best_profit, list_of_action_to_buy, total_cost)


if __name__ == "__main__":
    start = datetime.now()
    main()
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"Le temps d'exécution est de : {td:.03f}ms")
