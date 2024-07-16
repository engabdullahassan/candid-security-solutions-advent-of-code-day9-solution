def extrapolate_next_value(sequence):
    history = [sequence]
    while True:
        last_sequence = history[-1]

        # Calculate the differences between consecutive elements
        differences = [last_sequence[i+1] - last_sequence[i] for i in range(len(last_sequence)-1)]
        history.append(differences)
         # Check if all differences are zero
        if all(diff == 0 for diff in differences):
            break

    # Calculate the next value for each level from bottom to top
    for i in range(len(history)-1, 0, -1):
        # Get the next value by adding the last element of the current level
        # to the corresponding difference from the level below
        next_value = history[i-1][-1] + history[i][-1]
        history[i-1].append(next_value)

    # Return the next value of the original sequence
    return history[0][-1]

def main():
    # Define the input sequences
    input_data = [
        [0, 3, 6, 9, 12, 15, 18],
        [1, 3, 6, 10, 15, 21, 28],
        [10, 13, 16, 21, 30, 45, 68]
    ]
    # Calculate the next values for each sequence
    next_values = [extrapolate_next_value(seq) for seq in input_data]

    # Calculate the total sum of the next values
    total_sum = sum(next_values)

    # Print the results
    print("Next values:", next_values)
    print("The sum of the extrapolated next values is:", total_sum)

if __name__ == "__main__":
    main()
