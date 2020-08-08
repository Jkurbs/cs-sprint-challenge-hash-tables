# def has_negatives(a):
#     result = 0 
#     for number in a: 
#         if number < 0: 
#             result += 1
#     return result

# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# def has_negatives(a):
    
#     cache = {}
#     result = []

#     # Verify if number is in cache, if it's not add it
#     for number in a: 
#         if number not in cache:
#             cache[number] = number

#     # Loop over the numbers in the cache
#     # Verify if the number is below zero
#     # Verify if the number is in the cache

#     for number in cache: 
#         if number > 0 and abs(cache[number]) in cache:
#             result.append(abs(cache[number]))
#     return result

def has_negatives(a):

    cache = {}
    result = []

    # Verify if number is in cache, if it's not add it
    for i in a:
        if i not in cache:
            cache[i] = i

    # Loop over the numbers in the cache
    # Verify if the number is below zero
    # Verify if the number is in the cache
    
    for x in cache:
        if x < 0 and abs(cache[x]) in cache:
            result.append(abs(cache[x]))

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
