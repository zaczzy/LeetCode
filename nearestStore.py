# the inputs are two arrays of 1d location of stores and houses
# return an array of 1d location of closest stores for each house.

def nearestStore(stores, houses):
    nearest = {}
    curr_store = None  # the closest store with smaller location
    i = 0
    j = 0
    ls = len(stores)
    lh = len(houses)
    stores.sort()
    s_houses = sorted(houses)
    while i < ls and j < lh:
        house = s_houses[j]
        store = stores[i]
        if house <= store:
            if curr_store:
                nearest[house] = nearest_of_two(house, curr_store, store)
            else:
                nearest[house] = store
            j += 1
        else:
            curr_store = store
            i += 1
    if j < lh:
        while j < lh:
            house = s_houses[j]
            nearest[house] = curr_store
            j += 1
    return [nearest[house] for house in houses]


def nearest_of_two(house, store1, store2):
    # returns store 1 if equally distant
    if abs(house - store1) > abs(house - store2):
        return store2
    else:
        return store1


def nearest_store_test():
    input1s = [[16, 30, 38, 32, 14]]
    input2s = [[3, 43, 1, 5, 26, 26]]
    outputs = [[14, 38, 14, 14, 30, 30]]
    for i in range(len(outputs)):
        assert nearestStore(input1s[i], input2s[i]) == outputs[i], "failed test %i" % i
    return "all tests pass"


if __name__ == "__main__":
    print(nearest_store_test())
