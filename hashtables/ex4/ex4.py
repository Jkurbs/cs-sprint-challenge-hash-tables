def has_negatives(a):
    result = 0 
    for number in a: 
        if number < 0: 
            result += 1
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
