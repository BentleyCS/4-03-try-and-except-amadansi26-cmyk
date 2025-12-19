def sum(arr : list) -> int:
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
    return total
print(sum([1, 1, 2]))


def cleanData(rawData : list) ->list:
    final_list = list()
    for i in range(len(rawData)):
        try:
            float_value = float(rawData[i])
            final_list.append(float_value)
        except ValueError:
            continue
    return final_list
print(cleanData([6, 7, 6, "egg", "menx", "max", 7.111, "yes123", "12345"]))



def unreliableCalculator(divisors : list) -> list:
    final_list = list()
    for i in range(len(divisors)):
        try:
            quotient = 100/divisors[i]
            final_list.append(quotient)
        except Exception as e:
            final_list.append(e)
    return final_list
print(unreliableCalculator([200, 6, "hi", 111.113, 10, 500]))



def upperAll(arr : list) -> None:
    for index, item in enumerate(arr):
        arr[index] = item.upper()
arr = ["im", "tired"]
upperAll(arr)
print(arr)


def firstItems(arr : list) -> list:
    final_list = list()
    for i in range(len(arr)):
        try:
            first_value = arr[i][0]
            final_list.append(first_value)
        except Exception as e:
            final_list.append(arr[i])
    return final_list
print(firstItems([1, [2, 3, 4]]))
