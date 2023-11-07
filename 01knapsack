def solve_knapsack():
    val = []  # Value array
    wt = []   # Weight array

    # Taking user input for values and weights
    n = int(input("Enter the number of items: "))
    for i in range(n):
        val.append(int(input(f"Enter value for item {i + 1}: ")))
        wt.append(int(input(f"Enter weight for item {i + 1}: ")))

    W = int(input("Enter the maximum weight capacity (W): "))

    def knapsack(W, n):
        if n < 0 or W <= 0:
            return 0, []

        if wt[n] > W:
            return knapsack(W, n - 1)

        include_value, include_items = knapsack(W - wt[n], n - 1)
        include_value += val[n]

        exclude_value, exclude_items = knapsack(W, n - 1)

        if include_value > exclude_value:
            include_items.append(n + 1)  # Add 1 to convert to 1-based indexing
            return include_value, include_items
        else:
            return exclude_value, exclude_items

    max_value, selected_items = knapsack(W, n - 1)
    print("Maximum Value:", max_value)
    print("Selected Items (Item Number):", selected_items)

if __name__ == "__main__":
    solve_knapsack()
