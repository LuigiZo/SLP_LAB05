#point1
def calculateAvgList1(lists):
    if len(lists) == 0:
        return "N/C"
    sum = 0
    for list in lists:
        print(list)
        sum += list
    return round(sum/len(lists), 2)

#point2
def calculateAvgNormInputList(low_tres=0, upper_tres=1, *list):
        print(f"list: {list}")
        print(f"tresholds: {low_tres, upper_tres}")
        b = []
        for a in range(len(list)):
            b.append(a)
        for i, elem in enumerate(list):
            b[i] = (elem - min(list)) / (max(list) - min(list))
        print(f"normalized list: {b}")
        for i2, elem2 in enumerate(b):
            if elem2 < low_tres or elem2 > upper_tres:
                b.pop(i2)
        print(f"result output: {b}")
        summ = 0
        for i3 in b:
            summ += i3
        res = round(summ / len(b), 2)
        print(f"Avg from normalized and filtered values: {res}")

#point3.1
def calculateAvgList(*lists):
    if len(lists) == 0:
        return "N/C"
    sum = 0
    for list in lists:
        print(list)
        sum += list
    return round(sum/len(lists), 2)

#point3.2
def calculateAvgFromList(**lists):
    if len(lists) == 0:
        return "N/C"
    sum = 0
    for key, list in lists.items():
        print(key, list)
        sum += list
    return round(sum/len(lists), 2)