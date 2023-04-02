def sugar(weight):
    if not (weight % 5):
        return weight // 5

    kg_5 = weight // 5
    kg_3 = 0
    while kg_5 > -1:
        rest_weight = weight - 5 * kg_5
        if rest_weight % 3 == 0:
            kg_3 = rest_weight // 3
            return kg_5 + kg_3
        else:
            kg_5 -= 1
    return -1


print(sugar(int(input())))