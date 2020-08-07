def get_indices_of_item_weights(weights, length, limit):
    # Setup cache
    cache = {}
    # Loop over the lenght of the weights
    for i in range(len(weights)):
        # Cache the result
        cache[weights[i]] = i
    for i in range(len(weights)):
        value = limit - weights[i]
        print("VALUE: ", value)
        if value in cache:
            print("Value in cache")
            return (max(i, cache[value]), min(i, cache[value]))
    return None

weights_1 = [9]
print(get_indices_of_item_weights(weights_1, 1, 9))
