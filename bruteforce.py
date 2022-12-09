"""Creation of the input data for the project"""


def main():
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

    brute_force_KS(input_data)


def brute_force_KS(input_data):

    MAX_POSSIBILITIES = 2**20

    total_cost = 0
    max_output = 0
    item_to_buy = 0

    for i in range(MAX_POSSIBILITIES):
        # For each possibility, we have a binary representation of the possibility
        binary = bin(i)[2:]  # Remove leading "0b"
        position_of_ones = []
        for pos, char in enumerate(
            binary
        ):  # Get all the "1"'s position  which are the item to buy
            if char == "1":
                position_of_ones.append(len(binary) - 1 - pos)
        cost = 0
        profit = 0
        for pos in position_of_ones:
            cost += input_data[pos][
                "cost"
            ]  # Calculate the cost and profit for each possiblity
            if cost > 500:  # If the cost is above 500, we check the next one
                break
            profit += input_data[pos]["profit"]
        if (
            profit > max_output and cost < 500
        ):  # We take the highest profit and a cost below 500
            max_output = profit
            total_cost = cost
            item_to_buy = position_of_ones
            # print(item_to_buy)

    print(
        f"Le bénéfice maximum sur 2 ans est de {max_output}$ pour un coût de {total_cost}$"
    )
    print("Voici la liste des actions à acheter :")
    for item in item_to_buy:
        print(input_data[item]["action"])


if __name__ == "__main__":
    main()
