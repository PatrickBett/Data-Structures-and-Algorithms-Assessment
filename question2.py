def remove_duplicates(sequence):
    #initialize empty set
    registered_numbers = set()
    #change sequence to list
    sequence = list(sequence)
    index = 0
    for number in sequence:
        if number in registered_numbers:
            sequence.pop(index)
        else:
            registered_numbers.add(number)
        index += 1
    return sequence

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
