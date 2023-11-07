def fractional_knapsack():
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        value = int(input(f"Enter value for item {i + 1}: "))
        weight = int(input(f"Enter weight for item {i + 1}: "))
        items.append((value, weight, i + 1))  # Add item number

    capacity = int(input("Enter the maximum weight capacity (W): "))

    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    knapsack = []

    for value, weight, item_number in items:
        if capacity == 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
            knapsack.append((value, weight, item_number))
        else:
            fraction = capacity / weight
            total_value += fraction * value
            knapsack.append((fraction * value, capacity, item_number))
            break

    return knapsack, total_value

if __name__ == "__main__":
    knapsack, max_value = fractional_knapsack()

    print("Items in the Knapsack:")
    for value, weight, item_number in knapsack:
        print(f"Item {item_number}: Value: {value}, Weight: {weight}")

    print("Total Value in the Knapsack:", max_value)
