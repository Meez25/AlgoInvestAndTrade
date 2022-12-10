import csv
from datetime import datetime

from optimized import get_best_combinaison


def extract_lists_from_csv(csv_file):
    data_set_values = []
    data_set_weights = []
    data_set_names = []

    with open(csv_file) as fichier_csv:
        reader = csv.reader(fichier_csv)
        next(reader)  # skip the header
        for row in reader:
            if float(row[1]) < 0:  # Remove negative values
                continue
            weight = int(float(row[1]) * 100)  # use cents
            pourcentage = float(row[2])
            value = int(pourcentage / 100 * weight)  # use cents
            data_set_weights.append(weight)
            data_set_values.append(value)
            data_set_names.append(row[0])
    return data_set_values, data_set_weights, data_set_names


def calculate_gain(csv_file, item_to_buy):
    with open(csv_file) as fichier_csv:
        reader = csv.reader(fichier_csv)
        next(reader)  # skip the header
        total_cost = 0
        earnings = 0
        for row in reader:
            for item in item_to_buy:
                if row[0] == item:
                    total_cost += float(row[1])
                    earnings += float(row[1]) / 100 * float(row[2])
                    break
        print(f"L'investissement est de {total_cost}$ pour un gain de {earnings}$.")


def items_in_dataset(h, w, wts, table, dataset_name, dataset_weight):
    i = h - 1  # i is number of actions - 1
    j = w  # k is the investissement size (ie 500$)
    action_to_buy = []

    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            print(f"{dataset_name[i]} pour un prix de {dataset_weight[i]} cents.")
            action_to_buy.append(dataset_name[i])  # Get back the list of action to buy
            j = j - wts[i]
            i = i - 1
        else:
            i = i - 1
    return action_to_buy


def main():
    # csv_file = "dataset1_Python+P7.csv"
    csv_file = "dataset2_Python+P7.csv"
    CAPACITY = 50000  # The capacity is in cents for a better precision

    data_set_values, data_set_weights, data_set_names = extract_lists_from_csv(csv_file)

    # Create the table
    table_data_set = get_best_combinaison(data_set_values, data_set_weights, CAPACITY)
    # Using the table, find the action to buy
    item_to_buy = items_in_dataset(
        len(data_set_weights),
        CAPACITY,
        data_set_weights,
        table_data_set,
        data_set_names,
        data_set_weights,
    )

    # Verify the computation with the csv file
    calculate_gain(csv_file, item_to_buy)


if __name__ == "__main__":
    start = datetime.now()
    main()
    end = datetime.now()
    td = (end - start).total_seconds()
    print(f"Le temps d'exécution est de : {td} secondes")
