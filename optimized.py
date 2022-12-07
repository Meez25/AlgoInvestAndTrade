import numpy as np

"""Creation of the input data for the project"""

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

array = np.empty((20, 500))


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
        # Not putting the item in the bag
        tmp1 = recursive_KS(
            input_data,
            n - 1,
            capacity,
        )  # We try putting the item in the bag
        tmp2 = input_data[n]["profit"] + recursive_KS(
            input_data,
            n - 1,
            capacity - input_data[n]["cost"],
        )
        result = max(tmp1, tmp2)
    return result


print(recursive_KS(input_data, len(input_data) - 1, 500))
